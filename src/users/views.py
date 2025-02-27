from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from django.db import IntegrityError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from users.serializers import UserRegistrationSerializer

class UserRegistrationView(CreateAPIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            user = serializer.save()
        except IntegrityError:
            return Response(status=status.HTTP_409_CONFLICT)

        refresh_token = RefreshToken.for_user(user)
        access_token = str(refresh_token.access_token)

        response_data = {
            **serializer.data,
            'refresh': str(refresh_token),
            'access': access_token,
        }

        return Response(response_data, status=status.HTTP_201_CREATED)

