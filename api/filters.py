from django_filters import rest_framework as filters
from .models import Post

class PostFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    author = filters.CharFilter(field_name='author__user_name', lookup_expr='icontains')
    published = filters.DateFilter(field_name='published', lookup_expr='lte')
    
    class Meta:
        model = Post
        fields = ['title', 'author', 'published']