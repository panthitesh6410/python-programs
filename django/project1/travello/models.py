from django.db import models

# Create your models here.

class destination:
    # fields :
    id: int
    name: str
    img: str
    desc: str
    price: int
    offer: bool