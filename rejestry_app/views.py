from django.http import response
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, status
from .models import BlogPost, Pet, Rejestr
from . import serializers
from .permissions import IsAuthenticatedOrWriteOnly
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
def index(request, path=''):
    return render(request, 'index.html')


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.AllowAny,)

class RejestrViewSet(viewsets.ModelViewSet):
    queryset = Rejestr.objects.all()
    serializer_class = serializers.RejestrSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BlogPostViewSet(viewsets.ModelViewSet):

    queryset = BlogPost.objects.all()
    serializer_class = serializers.BlogPostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PetViewSet(viewsets.ModelViewSet):

    queryset = Pet.objects.all()
    serializer_class = serializers.PetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




@api_view(['GET'])
def getUserPets(request):
    permissions_classes = (permissions.IsAuthenticated)

    if request.user.is_anonymous:
        return Response('User not logged in',status=status.HTTP_401_UNAUTHORIZED)
    
    
    pets = Pet.objects.filter(user=request.user)
    serializer = serializers.PetSerializer(pets,many=True)
    return Response(serializer.data)



@api_view(['GET'])
def getUser(request,username):
    try:
        user = User.objects.get(username=username)
    except :
        return Response('no such user',status=status.HTTP_401_UNAUTHORIZED)

