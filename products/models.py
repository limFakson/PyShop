from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)



class Offer(models.Model):
    code = models.CharField(max_length=12)
    description = models.CharField(max_length=233)
    discount = models.FloatField()
    
    
class NewProduct(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)