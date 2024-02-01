from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from django.db.models import Q
from .cart import Cart


def add_to_cart(request,product_id):
    cart = Cart(request)
    cart.add(product_id)
    
    return redirect('frontpage')

def cart_view(request):
    cart = Cart(request)
    return render (request, 'loja/cart_view.html',{'cart':cart})
    
def search(request):
    query = request.GET.get('query','')
    products = Product.objects.filter(status=Product.ACTIVE).filter(Q(title__icontains= query) | Q(description__icontains= query))
    return render(request,'loja/search.html',{'query':query, 'products':products})

def category_detalhes(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(status=Product.ACTIVE)
    return render(request, 'loja/category_detalhes.html',{'category':category,'products':products})

def product_detalhes(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug, status=Product.ACTIVE)
    return render(request, 'loja/product_detalhes.html',{'product':product})


def get_status_color(status):
    if status == 'AT':  # Ativado
        return 'text-green-500'
    elif status == 'DI':  # Desativado
        return 'text-red-500'
    elif status == 'AG':  # Aguardando
        return 'text-yellow-500'
    else:
        return ''