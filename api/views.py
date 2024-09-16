from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Post
from .serializers import UserSerializer, LogoutSerializer, PostSerializer
from .permissions import PostUserWritePermission


class UserCreate(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

class LogoutUser(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = LogoutSerializer

    def perform_create(self, serializer):
        refresh_token = serializer.validated_data.get('refresh_token')

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            raise ValueError("Token inválido ou não encontrado")

class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [PostUserWritePermission]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    