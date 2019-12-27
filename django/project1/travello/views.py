from django.shortcuts import render
# import class from models.py:
from .models import destination

# Create your views here.
def index(request):
    # creating object of destination class to render data dynamically on webpage :
    dest1 = destination()
    dest1.name = 'mumbai'
    dest1.desc = 'dream city'
    dest1.price = 700
    dest1.offer = False
    dest2 = destination()
    dest2.name = 'polluted city'
    dest2.desc = 'delhi'
    dest2.price = 500
    dest1.offer = True
    dest3 = destination()
    dest3.name = 'gotham'
    dest3.desc = 'crime city'
    dest3.price = 1000
    dest1.offer = False
    # creating a single object and passthem at once :
    dests = [dest1, dest2, dest3]
    return render(request, 'index.html', {'dests': dests})     # this name can be from anywhere like BD, internet, etc dynamiclly
