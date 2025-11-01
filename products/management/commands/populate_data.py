from django.core.management.base import BaseCommand
from products.models import Category, Product
from decimal import Decimal
import random


class Command(BaseCommand):
    help = 'Populate database with sample products and categories'

    def handle(self, *args, **kwargs):
        # Clear existing data
        self.stdout.write('Clearing existing data...')
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Create categories
        self.stdout.write('Creating categories...')
        categories_data = [
            {'name': 'Electronics', 'description': 'Electronic devices and accessories'},
            {'name': 'Clothing', 'description': 'Apparel and fashion items'},
            {'name': 'Books', 'description': 'Books and publications'},
            {'name': 'Home & Garden', 'description': 'Home improvement and gardening supplies'},
            {'name': 'Sports', 'description': 'Sports equipment and accessories'},
            {'name': 'Toys', 'description': 'Toys and games for all ages'},
        ]

        categories = []
        for cat_data in categories_data:
            category = Category.objects.create(**cat_data)
            categories.append(category)
            self.stdout.write(self.style.SUCCESS(f'  ✓ Created category: {category.name}'))

        # Create products
        self.stdout.write('Creating products...')
        products_data = [
            # Electronics
            {'name': 'Laptop Pro 15', 'description': 'High-performance laptop with 16GB RAM and 512GB SSD', 
             'price': Decimal('1299.99'), 'quantity': 25, 'sku': 'ELEC-LAP-001', 'is_featured': True},
            {'name': 'Wireless Mouse', 'description': 'Ergonomic wireless mouse with precision tracking',
             'price': Decimal('29.99'), 'quantity': 150, 'sku': 'ELEC-MOU-002'},
            {'name': 'USB-C Hub', 'description': '7-in-1 USB-C hub with HDMI and card reader',
             'price': Decimal('49.99'), 'quantity': 80, 'sku': 'ELEC-HUB-003'},
            {'name': 'Bluetooth Headphones', 'description': 'Noise-cancelling over-ear headphones',
             'price': Decimal('199.99'), 'quantity': 45, 'sku': 'ELEC-HEAD-004', 'is_featured': True},
            
            # Clothing
            {'name': 'Cotton T-Shirt', 'description': 'Premium quality cotton t-shirt, multiple colors',
             'price': Decimal('19.99'), 'quantity': 200, 'sku': 'CLOTH-TSH-001'},
            {'name': 'Denim Jeans', 'description': 'Classic blue denim jeans, slim fit',
             'price': Decimal('59.99'), 'quantity': 120, 'sku': 'CLOTH-JNS-002'},
            {'name': 'Winter Jacket', 'description': 'Warm winter jacket with hood',
             'price': Decimal('129.99'), 'quantity': 5, 'sku': 'CLOTH-JAC-003'},
            
            # Books
            {'name': 'Python Programming', 'description': 'Complete guide to Python programming',
             'price': Decimal('44.99'), 'quantity': 60, 'sku': 'BOOK-PRG-001', 'is_featured': True},
            {'name': 'Django for Beginners', 'description': 'Learn web development with Django',
             'price': Decimal('39.99'), 'quantity': 40, 'sku': 'BOOK-WEB-002'},
            {'name': 'Data Science Handbook', 'description': 'Essential data science techniques',
             'price': Decimal('54.99'), 'quantity': 30, 'sku': 'BOOK-SCI-003'},
            
            # Home & Garden
            {'name': 'Garden Tools Set', 'description': '10-piece garden tools set with carrying case',
             'price': Decimal('79.99'), 'quantity': 35, 'sku': 'HOME-GRD-001'},
            {'name': 'LED Desk Lamp', 'description': 'Adjustable LED desk lamp with USB port',
             'price': Decimal('34.99'), 'quantity': 90, 'sku': 'HOME-LMP-002'},
            
            # Sports
            {'name': 'Yoga Mat', 'description': 'Non-slip yoga mat with carrying strap',
             'price': Decimal('24.99'), 'quantity': 100, 'sku': 'SPRT-YOG-001'},
            {'name': 'Dumbbell Set', 'description': 'Adjustable dumbbell set, 20kg total',
             'price': Decimal('89.99'), 'quantity': 0, 'sku': 'SPRT-DUM-002', 'status': 'out_of_stock'},
            {'name': 'Running Shoes', 'description': 'Lightweight running shoes with cushioning',
             'price': Decimal('79.99'), 'quantity': 75, 'sku': 'SPRT-SHO-003'},
            
            # Toys
            {'name': 'Building Blocks Set', 'description': '500-piece building blocks for creative play',
             'price': Decimal('34.99'), 'quantity': 110, 'sku': 'TOY-BLK-001'},
            {'name': 'Remote Control Car', 'description': 'High-speed RC car with rechargeable battery',
             'price': Decimal('69.99'), 'quantity': 8, 'sku': 'TOY-CAR-002'},
        ]

        status_choices = ['active', 'inactive']
        
        for i, prod_data in enumerate(products_data):
            # Assign category based on product type
            if i < 4:
                category = categories[0]  # Electronics
            elif i < 7:
                category = categories[1]  # Clothing
            elif i < 10:
                category = categories[2]  # Books
            elif i < 12:
                category = categories[3]  # Home & Garden
            elif i < 15:
                category = categories[4]  # Sports
            else:
                category = categories[5]  # Toys
            
            # Set status if not specified
            if 'status' not in prod_data:
                prod_data['status'] = 'active' if prod_data['quantity'] > 0 else 'out_of_stock'
            
            # Set is_featured if not specified
            if 'is_featured' not in prod_data:
                prod_data['is_featured'] = False
            
            product = Product.objects.create(
                category=category,
                **prod_data
            )
            self.stdout.write(self.style.SUCCESS(f'  ✓ Created product: {product.name}'))

        total_products = Product.objects.count()
        total_categories = Category.objects.count()
        
        self.stdout.write(self.style.SUCCESS(f'\n✅ Successfully created:'))
        self.stdout.write(self.style.SUCCESS(f'   - {total_categories} categories'))
        self.stdout.write(self.style.SUCCESS(f'   - {total_products} products'))
        self.stdout.write(self.style.SUCCESS(f'\n🚀 Your database is now populated with sample data!'))
