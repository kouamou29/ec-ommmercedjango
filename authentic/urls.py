from django.urls import path

from . import views
urlpatterns = [
    
   path('user/', views.auths,  name='auths'),
   path('user_login', views.user_login,  name='user_login'),
   path('user_logout', views.user_logout,  name='user_logout'),
   path('checkout/', views.checkout,  name='checkout'),
   
]
