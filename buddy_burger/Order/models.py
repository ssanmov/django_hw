from django.db import models
from User.models import Profile
from product.models import Product
# Create your models here.

class Order(models.Model):
    date = models.DateField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)


class Order_details(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    count = models.IntegerField(blank=True, null=True, default=0)
