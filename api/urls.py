from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view())
]
