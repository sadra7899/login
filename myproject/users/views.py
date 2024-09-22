from django.shortcuts import render
# users/views.py
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # تولید توکن JWT
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        # داده‌های پاسخ
        response_data = {
            'user': serializer.data,
            'access_token': access_token,
            'refresh_token': str(refresh),
        }

        return Response(response_data, status=status.HTTP_201_CREATED)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
