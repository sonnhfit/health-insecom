from django.db import models

# Create your models here.


class ProductCompareHealth(models.Model):
    images = models.CharField(max_length=255)
    product_name = models.TextField(max_length=255)
    cover = models.IntegerField(default=0)
    features = models.IntegerField(default=0)
    premium = models.IntegerField(default=0)


class CustomerParent(models.Model): 
    age = models.IntegerField(default=0)
    id_products = models.ForeignKey(ProductCompareHealth, on_delete=models.CASCADE, null=True)
    email = models.CharField(max_length=255)
    name_user = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    sex = models.BooleanField()
    city = models.CharField(max_length=255)
    birth_day = models.DateField(auto_now=True)
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    occupation = models.CharField(max_length=255)


class ChildPayment(models.Model): 
    age = models.IntegerField(default=0)
    relationship = models.ForeignKey(CustomerParent, on_delete=models.CASCADE, null=True)
    name_user = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    birth_day = models.DateField(auto_now=True)
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    occupation = models.CharField(max_length=255,blank=True)
    