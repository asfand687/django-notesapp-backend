from django.urls import path, include
from rest_framework.authtoken import views
from .views import RegisterAPI, LoginAPI

urlpatterns = [
    path('api/auth', views.obtain_auth_token),
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view()),
]
