from django.db import models

# Create your models here
from django.db.models import ForeignKey

class Kategory(models.Model):
    name = models.TextField(blank=False, null=True)


class Product(models.Model):
    name = models.TextField(blank=False, null=True)
    image = models.ImageField(upload_to='portfolio', blank=True, default='empty.png')
    description = models.TextField(blank=False, null=True)
    price = models.IntegerField(blank=False,null=False)
    kategory = models.ForeignKey(Kategory, on_delete=models.SET_NULL, null=True, related_name="product")


