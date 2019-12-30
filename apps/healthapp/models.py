from django.db import models

# Create your models here.


class PostPrepayment(models.Model);

email=models.CharField(max_length=200,blank=False,null=False)
nameUser=models.CharField(max_length=200,blank=False,null=False)
fullName=models.CharField(max_length=200,blank=False,null=False)
birthDay=models.models.DateField(blank=False,null=False)
weight=models.IntegerField(default=0)
height=models.IntegerField(default=0)
occupation=models.CharField(max_length=200,blank=False,null=False)

