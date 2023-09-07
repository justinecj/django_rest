from django.db import models

# Create your models here.

class Products(models.Model):
    product_id = models.IntegerField()
    name = models.CharField(max_length=50)
    price = models.IntegerField()

class Customer_preference(models.Model):
    preference_id = models.CharField(max_length=5)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)

class Orders(models.Model):
    customer_id = models.CharField(max_length=10)
    preference = models.ForeignKey(Customer_preference, on_delete=models.CASCADE)
    date = models.DateField()