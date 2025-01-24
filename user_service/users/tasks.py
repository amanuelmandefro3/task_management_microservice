from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_otp_email(email, otp):
    subject = "Your OTP Code"
    message = f"Use this code to verify your email: {otp}"
    send_mail(subject, message, 'amanuelmandefrow@gmail.com', [email])
    return True