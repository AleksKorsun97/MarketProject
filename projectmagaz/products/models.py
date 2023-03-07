from django.db import models

class Typeproduct(models.Model):
    title = models.CharField(max_length=255)

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    price = models.IntegerField()
    image = models.ImageField()
    typeproduct = models.ForeignKey(Typeproduct, on_delete=models.CASCADE)
    size = models.CharField(max_length=5, default='M')
    material = models.CharField(max_length=255, default='Бавовна')
    mayker = models.CharField(max_length=255, default='Китай')

# Create your models here.
