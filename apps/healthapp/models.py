from django.db import models

# Create your models here.


class ProductCompareHealth(models.Model):
    images = models.CharField(max_length=255)
    product_name = models.TextField(max_length=255)
    cover = models.IntegerField(default=0)
    features = models.IntegerField(default=0)
    premium = models.IntegerField(default=0)


class PostPrepayment(models.Model): 
    email = models.CharField(max_length=255)
    nameUser = models.CharField(max_length=255)
    fullName = models.CharField(max_length=255)
    birthDay = models.DateField(auto_now=True)
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    occupation = models.CharField(max_length=255)
