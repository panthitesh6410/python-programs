from django.shortcuts import render
# import class from models.py:
from .models import destination

# Create your views here.
def index(request):
    # creating object of destination class to render data dynamically on webpage :
    # creating a single object and passthem at once :
    dests = {'destination':destination.objects.all()}
    return render(request, 'index.html', dests)     # this name can be from anywhere like BD, internet, etc dynamiclly
def __str__(self):
    return self.name
