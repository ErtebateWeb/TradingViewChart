# serializers.py
from rest_framework import serializers

from .models import Event
import time


class EventSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model= Event
        fields =('id','url','name','date','timestamp','text','color','position','shape')
        # fields = '__all__'