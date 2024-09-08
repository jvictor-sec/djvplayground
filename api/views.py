from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import Post
from .serializers import PostSerializer
from .permissions import PostUserWritePermission

class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [PostUserWritePermission]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    