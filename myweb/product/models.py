from django.db import models

# Create your models here.
class cstmrdata(models.Model):
    name=models.CharField(max_length=15)
    place=models.CharField(max_length=10)
    email=models.EmailField(max_length=30)
    mobile=models.IntegerField()
    password=models.CharField(max_length=10)