from django.db.models import fields
from rest_framework import serializers
from todoapp.models import *

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class threadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = threads
        fields = '__all__'