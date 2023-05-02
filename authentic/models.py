from django.db import models
from django.conf import settings 
# Create your models here.


CONTRY_USER = [
        ('FRANCE' , 'FRANCE'),
        ('ALLEMAGNE' , 'ALLEMAGNE'),
        ('CAMEROUN' , 'CAMEROUN'),
        ('GABON' , 'GABON'),
    ]

class AdressUser(models.Model):
  
    contry      = models.CharField(max_length=10, choices=CONTRY_USER, default='CAMEROUN')
    city        = models.CharField(max_length=150, unique=True)
    adress      = models.TextField(max_length=100, unique=True)
    code_postal  = models.IntegerField(unique=True)
    
    
    def __str__(self):
        return f"{self.city}"
    