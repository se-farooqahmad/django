from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.TextField(null =True, blank= True)
    roll = models.IntegerField()

class Product(models.Model):
    productName = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=3, max_digits=10)

class Car(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.IntegerField()

def __str__(self):
    return self.brand