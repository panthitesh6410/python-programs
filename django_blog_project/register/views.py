from django.shortcuts import render, redirect          # to redirect to another page
from django.contrib.auth import login,authenticate                #importing built-in django form
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()         # saveing form details into DB
        return redirect('/home')   # redirect to home
    else:
        form = UserCreationForm()          # creating empty form.
    return render(request, "register/register.html", {'form': form})