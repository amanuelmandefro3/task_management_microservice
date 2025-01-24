from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Task
from .serializers import TaskSerializer
from .rabbitmq_utils import publish_event

class TaskViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for tasks.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]  # Ensure all endpoints require JWT

    def perform_create(self, serializer):
        task = serializer.save()
        publish_event(
            exchange_name='task_events',
            routing_key='task_created',
            message_body={
                'task_id': task.id,
                'title': task.title,
                'assigned_user_id': task.assigned_user_id
            }
        )

    @swagger_auto_schema(
        method='post',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['user_id'],
            properties={
                'user_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the user to assign the task to.')
            },
        ),
        responses={
            200: openapi.Response(
                description="Task assigned successfully.",
                examples={"application/json": {"id": 1, "title": "Task Title", "assigned_user_id": 2, "status": "Assigned"}}
            ),
            400: "Bad Request",
            404: "Not Found"
        }
    )
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def assign(self, request, pk=None):
        """
        Assign a task to a user.
        """
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response({"detail": "Task not found."}, status=status.HTTP_404_NOT_FOUND)

        user_id = request.data.get('user_id')
        if not user_id:
            return Response({"detail": "user_id is required."}, status=status.HTTP_400_BAD_REQUEST)

        task.assigned_user_id = user_id
        task.status = 'Assigned'
        task.save()

        publish_event(
            exchange_name='task_events',
            routing_key='task_assigned',
            message_body={
                'task_id': task.id,
                'assigned_user_id': user_id
            }
        )

        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
