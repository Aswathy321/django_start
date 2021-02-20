from django.db import models

# Create your models here.
class item(models.Model):
    name= models.CharField(max_length=50)
    descri=models.CharField(max_length=100)
    price=models.IntegerField()
    brand=models.CharField(max_length=50,default='not available')


    def __str__(self):
        return str(self.id) + ':' + self.name