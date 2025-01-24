from rest_framework import viewsets
from .models import NotificationLog
from .serializers import NotificationLogSerializer

class NotificationLogViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-only logs for demonstration.
    """
    queryset = NotificationLog.objects.all()
    serializer_class = NotificationLogSerializer
