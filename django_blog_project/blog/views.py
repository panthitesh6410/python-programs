from django.shortcuts import render
from django.http import HttpResponse        # import http 
from .models import Posts

# Create your views here.

# posts = [           # list of dictionary
#     {
#         'author' : 'hitesh',
#         'title' : 'blog post 1',
#         'content' : 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Architecto nobis quos molestias dolorum quo omnis delectus esse quasi rem, tenetur quod repellat? Amet minima, dolor ipsam deserunt fuga similique quas veniam illum culpa quae, rerum ab ad quia molestias debitis non ducimus hic sunt iste. Autem saepe fugit delectus officiis',
#         'date_posted' : 'august 27, 2020'
#     },
#     {
#         'author' : 'admin',
#         'title' : 'blog post 2',
#         'content' : 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Architecto nobis quos molestias dolorum quo omnis delectus esse quasi rem, tenetur quod repellat? Amet minima, dolor ipsam deserunt fuga similique quas veniam illum culpa quae, rerum ab ad quia molestias debitis non ducimus hic sunt iste. Autem saepe fugit delectus officiis.',
#         'date_posted' : 'august 28, 2020'
#     }
# ]

def home(request):
    context = {
        'posts': Posts.objects.all()
    }
    return render(request, 'blog/home.html', context)     # connect to the template

def about(request):
    return render(request, 'blog/about.html',{'title': 'about'})

# directory structure : blog -> templates -> blog -> files.html






