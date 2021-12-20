from django.db.models import fields
from rest_framework import serializers
from home.models import Task,threads

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'

    # class Meta1:
    #     model = threads
    #     fields = '__all__'
        # fields = 'Title'

class threadsSerializer(serializers.ModelSerializer):

    class Meta:
        model = threads
        fields = '__all__'