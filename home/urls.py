"""todoList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('',views.tasks, name='tasks'),
    path('tasks',views.tasks, name='tasks'),
    # path('tasks/<int:id>',views.tasks, name='tasks'),
    path('tasks/<str:time>',views.tasks, name='tasks'),
    path('list',views.list,name='list'),
    path('login',views.loginUser,name='login'),
    path('loggedout',views.logoutUser,name='loggedout'),
    path('signup',views.signup,name='signup'),
    path('registered',views.registered,name='registered'),
    path('superuser',views.superuser,name='superuser'),
    path('update_task/<int:pk>',views.update_task,name = 'update_task'), #update task url
    path('delete_task/<int:pk>',views.delete,name = 'delete_task'), #delete task url
    path('update_list/<int:pk>',views.updatel,name = 'update_list'), #update list url
    path('delete_list/<int:pk>',views.deletel,name = 'delete_list'), #delete list url

]