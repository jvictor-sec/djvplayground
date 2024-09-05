from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone

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

    objects = models.Manager
    postobjects = PostObjects()

    class Meta:
        ordering = ('-published',)
    
    def __str__(self):
        return self.title