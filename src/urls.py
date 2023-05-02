from django.urls import path

from . import views
urlpatterns = [
    
   path('', views.index,  name='index'),
   path('details/<str:slug>/', views.details,   name='details'),
   path('cart/', views.cart, name="cart"), 
   path('add_to_cart/<str:slug>/', views.add_to_cart,   name='add_to_cart'),
   path('removecart/', views.removecart,   name='removecart'),
   path('reduce_cart_prodcut/<str:id>/', views.reduce_cart_prodcut,   name='reduce_cart_prodcut'),
   path('cart_prodcut/<str:id>/', views.cart_prodcut,   name='cart_prodcut'),
   
   
]