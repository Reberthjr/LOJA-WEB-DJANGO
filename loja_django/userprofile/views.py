from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify
from django.contrib import messages

from .models import Userprofile

from loja.models import Product
from loja.forms import ProductForm
from loja.models import Product, Category, Order, OrderItem


def vendor_details(request):

    return render(request,'userprofile/vendor_details.html')

@login_required
def my_account(request):
    
    return render(request,'userprofile/myaccount.html')

def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            login(request,user)
            userprofile = Userprofile.objects.create(user=user)
            
            return redirect('frontpage')
        
    else:
        form = UserCreationForm()
        
    return render(request,'userprofile/register.html', {'form':form})

@login_required
def my_store(request):
    products =  request.user.products.exclude(status=Product.delete)
    order_items = OrderItem.objects.filter(product__user=request.user)
    return render(request,'userprofile/mystore.html',{'products':products, 'order_items':order_items})





@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            title = request.POST.get('title')
            product = form.save(commit=False)
            product.user = request.user
            product.slug = slugify(title)
            product.save()
            
            messages.success(request,'Product registered successfully!!')
            
            return redirect('mystore')
    else:    
        form = ProductForm()
    return render(request,'userprofile/product_form.html',{'title':'Add Product','form':form})


@login_required
def edit_product(request,pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    if request.method =='POST':
        form= ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            
            messages.success(request,'Product registered successfully!!')
        return redirect('mystore')
    else:
        form = ProductForm(instance=product)
    return render(request,'userprofile/product_form.html',{'title':'Edit Product','product':product, 'form':form})


@login_required
def delete_product(request,pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    product.status = Product.DELETE
    product.save()
    messages.success(request,'Product deleted successfully!!')
    return redirect('mystore')
    
    

def my_shopping_cart(request):
    return render(request,'userprofile/shoppingcart.html')





##----------------------------------------------------------------
def popup_message_view(request):
    # Sua lógica para obter as mensagens aqui (substitua esta linha conforme necessário)
    messages = ['Seu texto de mensagem aqui.']

    return render(request, 'popup_message.html', {'messages': messages})


