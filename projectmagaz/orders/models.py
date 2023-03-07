from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Bucket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    products = models.ManyToManyField(Product)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    status = models.IntegerField()
    name_surname = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    post = models.IntegerField(blank=True, null=True)


# Create your models here.
