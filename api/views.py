from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User, Post
from .serializers import UserSerializer, LogoutSerializer, PostSerializer
from .permissions import PostUserWritePermission

class UserViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def login(self, request):
        serializer = TokenObtainPairSerializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def logout(self, request):
        try:
            refresh_token = request.data.get('refresh_token')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Logout successful."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)

class PostViewSet(ModelViewSet):
    permission_classes = [PostUserWritePermission]
    serializer_class = PostSerializer
    queryset = Post.postobjects.all()

    @action(detail=False, methods=['get'], url_path='list-by-slug/(?P<slug>[^/.]+)')
    def list_by_slug(self, request, slug=None):
        posts = self.queryset.filter(slug__icontains=slug)
        serializer = self.get_serializer(posts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)