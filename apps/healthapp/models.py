from django.db import models

# Create your models here.


class PostPrepayment(models.Model):
email=models.CharField(max_length=255, blank=false, null=false)
nameUser=models.CharField(max_length=255, blank=false, null=false)
fullName=models.CharField(max_length=255, blank=false, null=false)
birthDay=models.models.DateField(null=false)
weight=models.IntegerField(default=0)
height=models.IntegerField(default=0)
occupation=models.CharField(max_length=255,blank=false,null=false)

