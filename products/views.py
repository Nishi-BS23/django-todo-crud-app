from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from .forms import ProductForm, CategoryForm, ProductSearchForm


class ProductListView(ListView):
    """Display list of all products with search and filter functionality"""
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Product.objects.select_related('category').all()
        
        # Search functionality
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(sku__icontains=search_query)
            )
        
        # Category filter
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category_id=category)
        
        # Status filter
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = ProductSearchForm(self.request.GET)
        context['total_products'] = Product.objects.count()
        return context


class ProductDetailView(DetailView):
    """Display detailed information about a single product"""
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(SuccessMessageMixin, CreateView):
    """Create a new product"""
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_message = "Product '%(name)s' was created successfully!"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Create New Product'
        context['button_text'] = 'Create Product'
        return context


class ProductUpdateView(SuccessMessageMixin, UpdateView):
    """Update an existing product"""
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_message = "Product '%(name)s' was updated successfully!"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Update Product'
        context['button_text'] = 'Update Product'
        return context


class ProductDeleteView(SuccessMessageMixin, DeleteView):
    """Delete a product"""
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('products:product_list')
    success_message = "Product was deleted successfully!"
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


# Category Views
class CategoryListView(ListView):
    """Display list of all categories"""
    model = Category
    template_name = 'products/category_list.html'
    context_object_name = 'categories'
    paginate_by = 10


class CategoryDetailView(DetailView):
    """Display detailed information about a category with its products"""
    model = Category
    template_name = 'products/category_detail.html'
    context_object_name = 'category'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.object.products.all()
        return context


class CategoryCreateView(SuccessMessageMixin, CreateView):
    """Create a new category"""
    model = Category
    form_class = CategoryForm
    template_name = 'products/category_form.html'
    success_url = reverse_lazy('products:category_list')
    success_message = "Category '%(name)s' was created successfully!"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Create New Category'
        context['button_text'] = 'Create Category'
        return context


class CategoryUpdateView(SuccessMessageMixin, UpdateView):
    """Update an existing category"""
    model = Category
    form_class = CategoryForm
    template_name = 'products/category_form.html'
    success_url = reverse_lazy('products:category_list')
    success_message = "Category '%(name)s' was updated successfully!"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Update Category'
        context['button_text'] = 'Update Category'
        return context


class CategoryDeleteView(SuccessMessageMixin, DeleteView):
    """Delete a category"""
    model = Category
    template_name = 'products/category_confirm_delete.html'
    success_url = reverse_lazy('products:category_list')
    success_message = "Category was deleted successfully!"
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


def home(request):
    """Home page view"""
    context = {
        'total_products': Product.objects.count(),
        'total_categories': Category.objects.count(),
        'featured_products': Product.objects.filter(is_featured=True)[:6],
        'recent_products': Product.objects.all()[:6],
    }
    return render(request, 'home.html', context)
