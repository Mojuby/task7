from html.entities import html5
from operator import mod
from socket import htons
from django.db import models

# Create your models here.

# people address doctor product bio model
# people-address, doctor, bio dbr

class People(models.Model):
   username = models.CharField(max_length=50)
   firstname = models.CharField(max_length=50)
   lastname = models.CharField(max_length=50)
   phone = models.CharField


class Product(models.Model):
    product_name = models.CharField(max_length=30)
    product_price = models.CharField


class Address(models.Model):
    country = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    user = models.OneToOneField(People, on_delete=models.CASCADE)
    

class Doctor(models.Model):
    patients = models.ForeignKey(People, on_delete=models.CASCADE)


class Bio(models.Model):
    bio = models.CharField(max_length=50)
    user = models.OneToOneField(People, on_delete=models.CASCADE)
    