from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_notification_email(event_type, payload):
    """
    Example Celery task for sending notification emails.
    """
    if event_type == 'user_registered':
        # user_registered payload might contain otp_code, email, etc.
        otp_code = payload.get('otp_code', '')
        email = payload.get('email', '')
        subject = "Your Verification OTP (From Notification Service)"
        message = f"Your OTP code is {otp_code}. Please verify within 5 minutes."
        send_mail(subject, message, 'no-reply@example.com', [email])
    elif event_type == 'task_created':
        # Notify assigned user if assigned_user_id is known (or do something else).
        pass
    elif event_type == 'task_assigned':
        # Notify user about new assignment, etc.
        pass
    return True
