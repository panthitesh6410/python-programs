from django.contrib.auth.models import User       # importing authr to get user info
from django.db import models
from django.utils import timezone           # to get date and time

# we are going to create a "post" model i.e. a class that inherits from django models class :

# each class is going to be a table in DB

# each attribute will be a seperate field in DB

class Posts(models.Model):
    
    # declaring fields (i.e. columns of table) :

    title = models.CharField(max_length=100)        # CharField must contain an arguement of max_length
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)    # check ones 
    author = models.ForeignKey(User, on_delete=models.CASCADE)        # a foriegn key to connect to users table

# we create a dunder(double underscore) str method __str__(), to make Posts object descriptive :
def __str__(self):
	return self.title
