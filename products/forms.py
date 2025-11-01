from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """Form for creating and updating products with Bootstrap styling"""
    
    class Meta:
        model = Product
        fields = [
            'name', 'description', 'category', 'price', 
            'quantity', 'status', 'sku', 'image', 'is_featured'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter product name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter product description'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': '0.00'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'placeholder': '0'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
            'sku': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter SKU'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'is_featured': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
    
    def clean_price(self):
        """Validate that price is positive"""
        price = self.cleaned_data.get('price')
        if price and price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price
    
    def clean_quantity(self):
        """Validate that quantity is not negative"""
        quantity = self.cleaned_data.get('quantity')
        if quantity and quantity < 0:
            raise forms.ValidationError("Quantity cannot be negative.")
        return quantity


class CategoryForm(forms.ModelForm):
    """Form for creating and updating categories"""
    
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter category name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter category description'
            }),
        }


class ProductSearchForm(forms.Form):
    """Form for searching and filtering products"""
    
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search products...'
        })
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        empty_label='All Categories',
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    status = forms.ChoiceField(
        choices=[('', 'All Status')] + Product.STATUS_CHOICES,
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
