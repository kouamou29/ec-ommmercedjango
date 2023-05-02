from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required 
# Create your views here.
from . models import Products, OrderItem, Order, Category
from django.contrib import messages 
from django.urls import reverse

from django.db.models import Q

def index(request):
    prodcuts = Products.objects.all()
    category = Category.objects.all()
    categoryID = request.GET.get('category')
    reach_post = request.GET.get('reach')
    
    if reach_post:
        post = Products.objects.filter(Q(name__icontains=reach_post) &
                                       Q(description__icontains=reach_post))
    else:
        post = "no prodducts"
    
    if categoryID:
        prodcuts = Products.objects.filter(category=categoryID)
    else:
        prodcuts = Products.objects.all()
        
    context = {"products": prodcuts, 'category': category, 'post':post}
    return render(request, 'page/index.html', context)

@login_required(login_url='user_login')
def details(request, slug):
    products = get_object_or_404(Products, slug=slug)
    
    return render(request, 'page/details.html', {"products": products, })

#add to cart product

def add_to_cart(request, slug):
   
    products =  get_object_or_404(Products, slug=slug)
    cart , _ = Order.objects.get_or_create(user=request.user)
    
    order , created = OrderItem.objects.get_or_create(user=request.user,
                                                      products=products,
                                                     )
    if created:
        cart.products.add(order)
        cart.save()
    else:
        
        order.quatity +=1
        order.save()
            
        
    return redirect(reverse("details", kwargs={"slug": slug}))


def cart(request):
    cart =  get_object_or_404(Order, user=request.user)
    
    order = OrderItem.objects.filter()
    total = 0
    
    for order_item in order:
       total =  order_item.quatity * order_item.products.price + total
     
    
    
    
    return render(request, 'page/cart.html', {"orders": cart.products.all(),
                                              'total': total}
                  )
#removecart
def removecart(request):
    cart = request.user.order
    cart.products.all().delete()
    cart.delete()
    return redirect('index')
    

#reduce_cart_prodcut
def reduce_cart_prodcut(request, id):
    products = get_object_or_404(Products, id=id)
    cart , _ = Order.objects.get_or_create(user=request.user)
    
    
    order , created = OrderItem.objects.get_or_create(user=request.user,
                                                      products=products,
                                                      orderer=False
                                                     )
    
    if order.quatity >1 or created:
        order.quatity -= 1
        order.save()
        return redirect('cart')
    else:
        order.delete()
        return redirect('cart')
    
def cart_prodcut(request, id):
    products = get_object_or_404(Products, id=id)
    cart , _ = Order.objects.get_or_create(user=request.user)
    
    
    order , created = OrderItem.objects.get_or_create(user=request.user,
                                                      products=products,
                                                     )
    
    if created:
        cart.products.add(order)
        cart.save()
    else:
        
        order.quatity +=1
        order.save()
            
    return redirect('cart')
          
    
      