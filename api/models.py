from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import timezone

class User(AbstractBaseUser, PermissionsMixin):
    class CustomUserManager(UserManager):
        def _create_user(self, email, user_name, first_name, password, **extra_fields):
            if not email:
                raise ValueError('You must provide an email address')

            email = self.normalize_email(email)

            user = self.model(email=email, user_name=user_name, first_name=first_name, **extra_fields)
            user.set_password(password)
            user.save()

            return user

        def create_user(self, email=None, user_name=None, first_name=None, password=None, **extra_fields):
            extra_fields.setdefault('is_staff', False)
            extra_fields.setdefault('is_superuser', False)
            extra_fields.setdefault('is_active', True)

            return self._create_user(email, user_name, first_name, password, **extra_fields)
        
        def create_superuser(self, email=None, user_name=None, first_name=None, password=None, **extra_fields):
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_superuser', True)
            extra_fields.setdefault('is_active', True)

            if extra_fields.get('is_staff') is not True:
                raise ValueError('Superuser must be staff')
            
            if extra_fields.get('is_superuser') is not True:
                raise ValueError('Superuser must be superuser')

            return self._create_user(email, user_name, first_name, password, **extra_fields)

    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=125, unique=True)
    first_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=125)
    about = models.TextField(max_length=500, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    def __str__(self):
        return self.user_name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __stf__(self):
        return self.name

class Post(models.Model):
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    STATUS_OPTIONS = (
        ('draft', 'Rascunho'),
        ('published', 'Publicado')
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_OPTIONS, default='published')
    slug = models.SlugField(max_length=250, unique_for_date=published)

    objects = models.Manager
    postobjects = PostObjects()

    class Meta:
        ordering = ('-published',)
    
    def __str__(self):
        return self.title