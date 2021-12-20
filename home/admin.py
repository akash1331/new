from django.contrib import admin
from home.models import Task, threads
from home.views import tasks

# Register your models here.


class TaskAdminSite(admin.ModelAdmin):
    # list_display = ('taskTitle','taskDesc','thread','complete','time')
    list_display = ('taskDesc','thread','complete','time')


admin.site.register(Task,TaskAdminSite)
admin.site.register(threads)


