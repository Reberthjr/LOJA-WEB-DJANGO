from django.db import models
from django.contrib.auth.models import User
import locale
from django.core.files import File
from io import BytesIO
from PIL import Image

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
    thumb_image = models.ImageField(upload_to='uploads/product_images/thumb_image', blank= True, null= True)
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
    
    
    
    def get_thumbnail(self):
        if self.thumb_image:
            return self.thumb_image.url
        else:
            if self.image:
                self.thumb_image =self.create_thumb_img(self.image)
                self.save()
                return self.thumb_image.url
            else: 
                return 'https://via.placeholder.com/240x240.jpg'
        
            
    
    
    def create_thumb_img(self, image, size=(300, 300)):
        img = Image.open(image)
        img = img.convert('RGB')
        img.thumbnail(size)
    
        thum_io = BytesIO()
        img.save(thum_io, 'JPEG', quality=85)
        name = image.name.replace('uploads/product_images/', '')
    
        thumbnail = File(thum_io, name=name)
    
        return thumbnail
    
    
class Order(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    adrres = models.CharField(max_length=255)
    complement = models.CharField(max_length=255)
    total_payable = models.IntegerField(blank=True, null=True)
    paid = models.BooleanField(default=False)
    payment_intent = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='orders', on_delete=models.SET_NULL, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add= True)
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    
    
    def get_total_price(self):
        return self.price / 100
    
    
    