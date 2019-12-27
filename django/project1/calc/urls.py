from django.urls import path

from . import views     # from same directory import views.py file data

urlpatterns = [
    path('', views.home, name="home"),           # home can be altered by index also and home is a function inside it
    path('add', views.add, name='add')
]