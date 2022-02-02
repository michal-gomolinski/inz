
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, status
from .models import Rejestr
from . import serializers
from .permissions import IsAuthenticatedOrWriteOnly
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
def index(request, path=''):
    return render(request, 'index.html')


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.AllowAny,)

@api_view(['GET'])
def getRejestry(request):
    permissions_classes = (permissions.AllowAny)

    if request.user.is_anonymous:
        return Response('User not logged in',status=status.HTTP_401_UNAUTHORIZED)

    rejestr = Rejestr.objects.filter(user=request.user)
    
    serializer = serializers.RejestrSerializer(rejestr,many=True)

    if(serializer.data):
        return Response(serializer.data)
    return Response({'error':'No user profile'},status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getRejestrById(request,pk):
    permissions_classes = (permissions.AllowAny)

    if request.user.is_anonymous:
        return Response('User not logged in',status=status.HTTP_401_UNAUTHORIZED)

    rejestr = Rejestr.objects.filter(pk=pk)

    serializer = serializers.RejestrSerializer(rejestr,many=True)
    if(serializer.data):
        return Response(serializer.data)
    return Response({'error':'Nie wykryto rejestru o podanym pk'},status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def postRejestr(request):
    if request.user.is_anonymous:
        return Response('User not logged in',status=status.HTTP_401_UNAUTHORIZED)

    serializer = serializers.RejestrSerializer(data=request.data)
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    if(serializer.is_valid() and 'pk' in request.data):
        Rejestr.objects.get(pk=request.data.get('pk')).delete()
        serializer.save(user=request.user,pk=request.data.get('pk'))
        return Response('serializer.data', status=status.HTTP_201_CREATED)


    if(serializer.is_valid()):
        serializer.save(user=request.user)
        return Response('serializer.data', status=status.HTTP_201_CREATED)
    return Response('Błąd',status=status.HTTP_400_BAD_REQUEST)
    