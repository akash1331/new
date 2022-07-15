from django.db import models
from django.db.models.deletion import SET_NULL

# Create your models here.

class threads(models.Model):
    Title=models.CharField(max_length=40)
    
    def __str__(self):
        return self.Title

class Task(models.Model):
    taskDesc = models.TextField('Task Description')
    time = models.DateTimeField('Time created',auto_now_add=True)
    thread = models.ForeignKey(threads,on_delete=SET_NULL,null=True)

    def __str__(self):
        return self.taskDesc
