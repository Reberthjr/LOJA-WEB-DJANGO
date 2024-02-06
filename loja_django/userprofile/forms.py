from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'w-full p-2 mb-2 border border-gray-200 rounded', 'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'w-full p-2 mb-2 border border-gray-200 rounded', 'placeholder': 'Confirm Password'}),
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'w-full p-2 mb-2 border border-gray-200 rounded', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'w-full p-2 mb-2 border border-gray-200 rounded', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'w-full p-2 mb-2 border border-gray-200 rounded', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'w-full p-2 mb-2 border border-gray-200 rounded', 'placeholder': 'Email'}),
        }
