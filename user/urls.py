from django.urls import path
from . import views
from .views import  UserDetailAPIView


urlpatterns = [
    path('api/users/', views.UserListAPIView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
]
