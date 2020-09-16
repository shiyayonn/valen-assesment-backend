from django.db import models

# Create your models here.
class Car(models.Model):
    name=models.CharField(max_length=20,blank=False,default='')
    color=models.CharField(max_length=10,blank=False,default='')

    def __str__(self):
        return self.name