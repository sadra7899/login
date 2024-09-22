
from django.contrib import admin
from django.urls import path
from users.views import RegisterView, MyTokenObtainPairView

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]