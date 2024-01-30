from django.db import models
from django.contrib.auth.models import User
import locale

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    
    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self) :
        return self.title
    
    

class Product(models.Model):
    user = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.TextField(blank= True)
    price = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add= True)
    update_at = models.DateTimeField(auto_now= True)
    
    class Meta:
        verbose_name_plural = 'Products'


    def __str__(self) :
        return self.title
        
        
    def get_display_price(self):
        # Assuming self.price is in cents
        price_in_brl = self.price / 100
        # Set the locale to Brazilian Portuguese
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        formatted_price = locale.currency(price_in_brl, grouping=True)

        return formatted_price 
    
    