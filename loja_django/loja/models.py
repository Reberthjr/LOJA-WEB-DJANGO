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
    SKETCH = 'sketh'
    WAITING_FOR_APPROVAL = 'waiting for approval'
    ACTIVE = 'active'
    DISABLE = 'disable'
    DELETE = 'deleted'
    
    CHOICES_STATUS = (
        (SKETCH, 'Sketh'),
        (WAITING_FOR_APPROVAL, 'Waiting for approval'),
        (ACTIVE, 'Activated'),
        (DISABLE,'Disable'),
        (DELETE, 'Deleted'),
    )
   
    
    
    user = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.TextField(blank= True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='uploads/product_images/', blank= True, null= True)
    create_at = models.DateTimeField(auto_now_add= True)
    update_at = models.DateTimeField(auto_now= True)
    status = models.CharField(max_length=50, choices=CHOICES_STATUS,default=ACTIVE)
    
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
    
    