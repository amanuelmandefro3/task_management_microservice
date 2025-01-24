from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
import random
import datetime

class User(AbstractUser):
    email_verified = models.BooleanField(default=False)
    otp_code = models.CharField(max_length=6, blank=True, null=True)
    otp_expires_at = models.DateTimeField(null=True, blank=True)

    def set_otp(self):
        """Generates a 6-digit OTP and sets an expiration time (10 minutes)."""
        code = f"{random.randint(0, 999999):06d}"
        self.otp_code = code
        self.otp_expires_at = timezone.now() + datetime.timedelta(minutes=10)

    def verify_otp(self, code):
        """Checks if code matches and is not expired."""
        if self.otp_code != code:
            return False
        if timezone.now() > self.otp_expires_at:
            return False
        self.email_verified = True
        self.otp_code = None
        self.otp_expires_at = None
        self.save()
        return True

    def __str__(self):
        return self.username