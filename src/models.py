from django.db import models
# Create your models here.
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse
from django.shortcuts import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"{ self.name}"
    
class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length = 50)
    image = models.ImageField(upload_to="product/")
    price  = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{ self.name}"
    
class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    orderer = models.BooleanField(default=False)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    quatity  = models.IntegerField(default=1)
    
    

    
    def __str__(self):
        return f"{self.quatity} of {self.products.name}"
    
class Order(models.Model):
   user =models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   products= models.ManyToManyField(OrderItem)
   start_date  = models.DateTimeField( auto_now_add=True)
   ordere_date = models.DateField(blank=True, null=True)
   
  
    
           
   
   
   def __str__(self):
       return f"{self.user.username}"

 
   
   
   
        

    
    
    
    
    
     
          
    
    
    
    
    
    

