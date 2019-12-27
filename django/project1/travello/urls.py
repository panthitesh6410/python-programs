from . import views     # from same directory import views.py file data
from django.urls import path

urlpatterns = [
    path('', views.index, name="index")           # home can be altered by index also and home is a function inside it
]