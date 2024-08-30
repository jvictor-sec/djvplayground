from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def hello_world(request):
    return Response('hello, world!', status.HTTP_201_CREATED)