
from django.conf.urls.static import static
from django.urls import path
from .import views


urlpatterns = [
    path('search/', views.search, name='search'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('change_quantity/<str:product_id>/', views.change_quantity, name='change_quantity'),
    path('remove_to_cart/<str:product_id>/', views.remove_to_cart, name='remove_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('<slug:slug>/', views.category_detalhes, name='category_detalhes'),
    path('<slug:category_slug>/<slug:slug>/', views.product_detalhes, name='product_detalhes'),
]
