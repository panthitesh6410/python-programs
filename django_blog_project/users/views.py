from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages         # to add send messages  
from .forms import UserRegisterForm


def register(request):
    # creating a form :
    if request.method == 'POST':            # form submitted via post requests here ans check if there is any post or not.
        form = UserRegisterForm(request.POST)   # it creates a predefined-form that has data within 'request.POST'
        if form.is_valid():                     # form validation and checks 
            form.save()                         # saving form data into database.
            username = form.cleaned_data.get('username')    
            messages.success(request, f'Account Created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()            # it creates an empty predefined-form
    return render(request, 'users/register.html', {'form': form})


# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error
