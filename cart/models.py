from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    shape = models.CharField(max_length=30)
    size = models.DecimalField(max_digits=5, decimal_places=2)
    location = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=7, decimal_places=2)


class Recommendation(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)