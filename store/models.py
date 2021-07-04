from django.db import models
from django.db.models.fields import DateField, DecimalField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    createdDate = models.DateField(auto_now_add=True)
    updatedDate = models.DateField(auto_now=True)
