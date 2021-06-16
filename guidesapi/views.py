from django.shortcuts import render
from rest_framework import generics
from .models import Guide
from .serializers import GuideSerializer

from rest_framework import viewsets

class GuideList(viewsets.ModelViewSet):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer