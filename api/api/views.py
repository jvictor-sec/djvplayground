from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from django_filters import rest_framework as filters

from .models import User, Post
from .serializers import UserSerializer, PostSerializer
from .permissions import PostUserWritePermission
from .filters import PostFilter

class UserViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def login(self, request):
        serializer = TokenObtainPairSerializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def logout(self, request):
        try:
            refresh_token = request.data.get('refresh_token')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Logout successful."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": f"Invalid token. Error: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

class PostViewSet(ModelViewSet):
    permission_classes = [PostUserWritePermission, IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.postobjects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = PostFilter