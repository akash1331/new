from django.contrib import admin
from .models import *
from .views import *

# Register your models here.


class TaskAdminSite(admin.ModelAdmin):
    list_display = ('taskDesc','thread','time')


admin.site.register(Task,TaskAdminSite)
admin.site.register(threads)
admin.site.site_header = 'ToDoList Admin'


