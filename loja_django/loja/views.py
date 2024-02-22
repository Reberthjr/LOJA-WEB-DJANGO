from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Order, OrderItem
from .cart import Cart
from .forms import OrderForm
from django.conf import settings
import json
import stripe
from django.http import JsonResponse






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
        data = json.loads(request.body)
        total_price = 0
        items = []
        for item in cart:
            product = item['product']
            total_price += product.price * int(item['quantity'])
            items.append({
                'price_data': {
                    'currency': 'brl',
                    'product_data': {
                        'name': product.title,
                    },
                    'unit_amount': product.price
                },
                'quantity': item['quantity']
            })

        stripe.api_key = settings.STRIPE_SECRET_KEY
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=items,
            mode='payment',
            success_url='https://127.0.0.1:8000/cart/success',
            cancel_url='https://127.0.0.1:8000/cart/',
        )

        payment_intent = session.payment_intent

        order = Order.objects.create(
            f_name = data['f_name'],
            l_name = data['l_name'],
            phone_number = data['phone_number'],
            city = data['city'],
            zip_code = data['zip_code'],
            address = data['address'],
            complement = data['complement'],
            created_by = request.user,
            paid = True,
            payment_intent = payment_intent,
            total_payable = total_price,   
        )
        
        for item in cart:
            product = item['product']
            quantity = int(item['quantity'])
            price = product.price * quantity

            item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)

        cart.clear()
        return JsonResponse({'session': session, 'order': payment_intent})

    else:
        form = OrderForm()

    return render(request, 'loja/checkout_buy.html', {'cart': cart, 'form': form, 'pub_key': settings.STRIPE_PUB_KEY,})
          
 
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