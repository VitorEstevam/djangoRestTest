from django.shortcuts import render
from rest_framework import generics
from .models import Music
from .serializers import MusicSerializer

from rest_framework import viewsets

class MusicList(viewsets.ModelViewSet):

     queryset = Music.objects.all()
     serializer_class = MusicSerializer