from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Order, OrderItem
from .cart import Cart
from .forms import OrderForm







def add_to_cart(request,product_id):
    cart = Cart(request)
    cart.add(product_id)
    
    return redirect('cart_view')

def remove_to_cart(request,product_id):
    cart = Cart(request)
    cart.delete(product_id)
    
    return redirect('cart_view')


def change_quantity(request, product_id):
    action = request.GET.get('action','')
    if action:
        quantity = 1
        if action == 'decrease': 
            quantity = -1
        cart = Cart(request)
        cart.add(product_id,quantity, True)
    return redirect('cart_view')      

@login_required
def checkout_buy(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            
            total_price = 0
            for item in cart:
                product = item['product']
                total_price += product.price * int(item['quantity'])
            
            order = form.save(commit=False)
            order.created_by = request.user
            order.total_price = total_price  
            order.save()
            
            for item in cart:
                product = item['product']
                quantity = int(item['quantity'])
                price = product.price * quantity
                
                item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)
                
            cart.clear()
            return redirect('myaccount')

    else:
        form = OrderForm() 

    return render(request, 'loja/checkout_buy.html', {'cart': cart, 'form': form})
            
 
def cart_view(request):
    cart = Cart(request)
    return render(request, 'loja/cart_view.html', {'cart': cart})
    
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