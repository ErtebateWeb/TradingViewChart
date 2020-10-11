from django.shortcuts import render
# from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework import viewsets

# Create your views here.
# views.py

from .serializers import EventSerializer
from .models import Event


# class HeroViewSet(viewsets.ModelViewSet):
#     queryset = Hero.objects.all().order_by('name')
#     serializer_class = HeroSerializer
class EventViewSet(viewsets.ModelViewSet):
    
    queryset = Event.objects.all().order_by('id')
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)