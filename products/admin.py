from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin configuration for Category model"""
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['name', 'description']
    list_filter = ['created_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin configuration for Product model"""
    list_display = ['name', 'category', 'price', 'quantity', 'status', 'is_featured', 'created_at']
    list_filter = ['status', 'category', 'is_featured', 'created_at']
    search_fields = ['name', 'description', 'sku']
    list_editable = ['status', 'is_featured']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'category', 'sku')
        }),
        ('Pricing & Inventory', {
            'fields': ('price', 'quantity', 'status')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Additional Options', {
            'fields': ('is_featured',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    list_per_page = 25
