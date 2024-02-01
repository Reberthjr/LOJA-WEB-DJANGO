from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [
    path('myaccount/', views.my_account, name='myaccount'),
    path('register/', views.register, name='register'),
    path('mystore/', views.my_store, name='mystore'),
    path('mystore/add_product/', views.add_product, name='add_product'),
    path('mystore/edit_product/<int:pk>/', views.edit_product, name='edit_product'),
    path('mystore/delete_product/<int:pk>/', views.delete_product, name='delete_product'),
    path('login/', auth_views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('vendors/', views.vendor_details, name='vendor_details'),
]