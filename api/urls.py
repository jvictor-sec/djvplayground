from django.contrib import admin
from django.urls import path

from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view()),
    path('get-token/', TokenObtainPairView.as_view()),
    path('refresh-token/', TokenRefreshView.as_view())
]
