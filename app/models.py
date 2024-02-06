from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.TextField(max_length=100,null=True)
    password=models.TextField(max_length=100,null=True)