from django import forms

from .models import Product, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model= Product
        fields = ('category','title','description','price','image','status')
        widgets = {
            'category': forms.Select(attrs={
                'class': ' w-full form-control border border-gray-200'}),
            'title': forms.TextInput(attrs={
                'class': ' w-full form-control border border-gray-200'}),
            'description': forms.Textarea(attrs={
                'class': ' w-full form-control border border-gray-200'}),
            'price': forms.NumberInput(attrs={
                'class': ' w-full form-control border border-gray-200'}),
            'image': forms.FileInput(attrs={
                'class': ' w-full form-control '}),
            'status': forms.Select(attrs={
                'class': ' w-full form-control border border-gray-200'}),
        }
        
        
        
        
class OrderForm(forms.ModelForm):
    class Meta:
        model= Order
        fields = ('f_name','l_name','phone_number','city','zip_code','address','complement',)