
from django.urls import path
from .import views


urlpatterns = [
    path('<slug:slug>/', views.category_detalhes, name='category_detalhes'),
    path('<slug:category_slug>/<slug:slug>/', views.product_detalhes, name='product_detalhes'),
]
