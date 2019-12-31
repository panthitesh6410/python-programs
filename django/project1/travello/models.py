from django.db import models

# Create your models here.

class destination(models.Model):
    # fields :
    # id: int
    # name: str
    # img: str
    # desc: str
    # price: int
    # offer: bool
    name = models.CharField(max_length=50)
    desc = models.TextField()
    price = models.IntegerField()
