from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=225)
    content = models.CharField(max_length=225)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
