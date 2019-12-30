from django.db import models

# Create your models here.


class ProductCompareHealth(models.Model):
    images = models.CharField(max_length=255)
    product_name = models.TextField(max_length=255)
    cover = models.IntegerField(default=0)
    features = models.IntegerField(default=0)
    premium = models.IntegerField(default=0)

