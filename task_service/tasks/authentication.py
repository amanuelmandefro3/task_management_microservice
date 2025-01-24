# task-service/tasks/authentication.py

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed
from rest_framework import exceptions

class CustomJWTAuthentication(JWTAuthentication):
    """
    Custom JWT Authentication that does not require the user to exist in the local database.
    It decodes the JWT token and sets `request.user` to a simple object with token claims.
    """

    def get_user(self, validated_token):
        # Instead of fetching the user from the database, create a simple user-like object
        try:
            user_id = validated_token["user_id"]
            username = validated_token.get("username", "Unknown")
            email = validated_token.get("email", "unknown@example.com")
        except KeyError:
            raise InvalidToken("Token contained no recognizable user identification")

        # Create a simple user-like object
        class SimpleUser:
            def __init__(self, id, username, email):
                self.id = id
                self.username = username
                self.email = email

            def __str__(self):
                return self.username

            def __repr__(self):
                return f"<SimpleUser: {self.username}>"

        return SimpleUser(
            id=user_id,
            username=username,
            email=email
        )
