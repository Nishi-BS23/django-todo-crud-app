from django.db import models
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    """Category model for organizing products"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('products:category_detail', kwargs={'pk': self.pk})


class Product(models.Model):
    """Product model with all necessary fields for CRUD operations"""
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('out_of_stock', 'Out of Stock'),
    ]
    
    name = models.CharField(max_length=200, help_text="Product name")
    description = models.TextField(help_text="Product description")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='products'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Price in USD"
    )
    quantity = models.PositiveIntegerField(default=0)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active'
    )
    image = models.ImageField(
        upload_to='products/%Y/%m/%d/',
        blank=True,
        null=True,
        help_text="Product image"
    )
    sku = models.CharField(
        max_length=100,
        unique=True,
        help_text="Stock Keeping Unit"
    )
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['sku']),
            models.Index(fields=['-created_at']),
        ]
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('products:product_detail', kwargs={'pk': self.pk})
    
    @property
    def is_in_stock(self):
        """Check if product is in stock"""
        return self.quantity > 0
    
    @property
    def stock_status(self):
        """Get stock status message"""
        if self.quantity == 0:
            return "Out of Stock"
        elif self.quantity < 10:
            return "Low Stock"
        else:
            return "In Stock"
