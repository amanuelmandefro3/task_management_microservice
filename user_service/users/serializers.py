# users/serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    """Used for /register/ endpoint."""
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = User.objects.create(**validated_data)
        user.set_otp()  # generate OTP code
        user.save()
        return user


class VerifyOTPSerializer(serializers.Serializer):
    """Used for /verify_otp/ endpoint."""
    email = serializers.EmailField()
    otp_code = serializers.CharField()

    def validate(self, data):
        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            raise serializers.ValidationError("User does not exist.")
        data['user'] = user
        return data


# class LoginSerializer(serializers.Serializer):
#     """Used for /login/ endpoint."""
#     username = serializers.CharField()
#     password = serializers.CharField()


class ResendOTPSerializer(serializers.Serializer):
    """Used for /resend_otp/ endpoint."""
    email = serializers.EmailField()


class UserSerializer(serializers.ModelSerializer):
    """Used for GET /profile/ or any read-only fields about user."""
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'email_verified']
