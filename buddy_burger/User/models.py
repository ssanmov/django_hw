from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.TextField(blank=False, null=True)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    created = models.DateField(auto_now_add=True)