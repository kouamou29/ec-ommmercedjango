from django.contrib import admin

# Register your models here.
from .models import Products, OrderItem, Order, Category

admin.site.register(Products)
admin.site.register(Category)
admin.site.register(OrderItem)
admin.site.register(Order)