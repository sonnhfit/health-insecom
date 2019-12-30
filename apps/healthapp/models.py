from django.db import models

# Create your models here.


class GetCompareHealth(models.Models):
    images = models.CharField(max_length=255,blank=false,null=false)
    product_name = models.TextField(max_length=255,blank=false,null=false)
    cover = models.IntegerField(default=0)
    features = models.IntegerField(default=0)
    premium = models.IntegerField(default=0)
