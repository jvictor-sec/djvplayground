from rest_framework.routers import DefaultRouter

from .views import User, Post

router = DefaultRouter()

router.register('post', Post, basename='posts')
router.register('user', User, basename='users')

urlpatterns = router.urls
