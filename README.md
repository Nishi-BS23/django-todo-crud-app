# Django Todo App - Simple CRUD with REST API

A minimalist **Todo application** built with Django that demonstrates CRUD operations with both traditional web interface and REST API following best practices.

## 🌟 Features

- ✅ **Simple CRUD Operations** (Create, Read, Update, Delete)
- 🔌 **REST API** with Django REST Framework
- 📱 **Responsive Design** with Bootstrap 5
- ✓ **Toggle Todo Completion** with one click
- 🎨 **Clean, Minimal UI**
- 🔐 **Admin Panel** for management

## 📁 Project Structure

```
Django CRUD Project/
│
├── core/                  # Main project settings
│   ├── settings.py       # Django settings + DRF config
│   └── urls.py           # Main URL routing
│
├── todos/                # Todo app
│   ├── models.py        # Todo model (5 fields)
│   ├── views.py         # Views + ViewSet
│   ├── serializers.py   # DRF serializers
│   ├── urls.py          # App URLs + API router
│   └── admin.py         # Admin configuration
│
├── templates/todos/     # Simple templates
│   ├── base.html
│   ├── todo_list.html
│   ├── todo_form.html
│   └── todo_confirm_delete.html
│
└── manage.py
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Migrations

```bash
python manage.py migrate
```

### 3. Create Admin User (Optional)

```bash
python manage.py createsuperuser
```

### 4. Start Server

```bash
python manage.py runserver
```

### 5. Access the App

- **Web Interface**: http://127.0.0.1:8000/
- **REST API**: http://127.0.0.1:8000/todos/api/todos/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## 📖 Usage

### Web Interface

1. **View Todos**: Navigate to http://127.0.0.1:8000/
2. **Create Todo**: Click "+ Add Todo" button
3. **Update Todo**: Click ✎ (edit) button on any todo
4. **Delete Todo**: Click 🗑 (delete) button
5. **Toggle Complete**: Click ✓ button to mark complete/incomplete

### REST API Endpoints

#### List All Todos

```http
GET /todos/api/todos/
```

#### Create Todo

```http
POST /todos/api/todos/
Content-Type: application/json

{
    "title": "Learn Django",
    "description": "Complete Django tutorial",
    "completed": false
}
```

#### Get Single Todo

```http
GET /todos/api/todos/{id}/
```

#### Update Todo

```http
PUT /todos/api/todos/{id}/
Content-Type: application/json

{
    "title": "Learn Django REST Framework",
    "description": "Complete DRF tutorial",
    "completed": true
}
```

#### Partial Update

```http
PATCH /todos/api/todos/{id}/
Content-Type: application/json

{
    "completed": true
}
```

#### Delete Todo

```http
DELETE /todos/api/todos/{id}/
```

#### Toggle Completion (Custom Action)

```http
POST /todos/api/todos/{id}/toggle_complete/
```

## 🎯 Model Structure

```python
class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

## 🔧 API Testing

### Using cURL

**Create Todo:**

```bash
curl -X POST http://127.0.0.1:8000/todos/api/todos/ \
  -H "Content-Type: application/json" \
  -d '{"title": "My First Todo", "description": "Test description"}'
```

**List Todos:**

```bash
curl http://127.0.0.1:8000/todos/api/todos/
```

**Update Todo:**

```bash
curl -X PUT http://127.0.0.1:8000/todos/api/todos/1/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Updated Todo", "completed": true}'
```

**Delete Todo:**

```bash
curl -X DELETE http://127.0.0.1:8000/todos/api/todos/1/
```

### Using Python Requests

```python
import requests

BASE_URL = "http://127.0.0.1:8000/todos/api/todos/"

# Create
response = requests.post(BASE_URL, json={
    "title": "Learn Python",
    "description": "Complete Python course"
})

# List
response = requests.get(BASE_URL)
todos = response.json()

# Update
response = requests.put(f"{BASE_URL}1/", json={
    "title": "Learn Python & Django",
    "completed": True
})

# Delete
response = requests.delete(f"{BASE_URL}1/")
```

## 🛠️ Best Practices Implemented

### 1. **REST API Design**

- ✅ RESTful URL patterns
- ✅ HTTP methods (GET, POST, PUT, PATCH, DELETE)
- ✅ Proper status codes
- ✅ JSON responses
- ✅ Pagination support

### 2. **Django Best Practices**

- ✅ Class-based views (ViewSet)
- ✅ Model Meta options
- ✅ URL namespacing
- ✅ Environment variables
- ✅ Clean code structure

### 3. **Security**

- ✅ CSRF protection
- ✅ CORS headers configuration
- ✅ SQL injection prevention
- ✅ XSS protection

### 4. **Code Quality**

- ✅ DRY principle
- ✅ Separation of concerns
- ✅ Docstrings
- ✅ Clean, readable code

## 📦 Dependencies

- **Django 5.2.7** - Web framework
- **djangorestframework** - REST API toolkit
- **django-cors-headers** - CORS handling
- **python-decouple** - Environment variables
- **Bootstrap 5.3** - UI framework (CDN)

## 🎨 Features Breakdown

### Web Interface

- Simple, clean design
- Responsive layout
- Inline todo editing
- Visual feedback (completed state)
- Quick actions (toggle, edit, delete)

### REST API

- Full CRUD operations
- Browsable API interface
- Pagination (10 items/page)
- Custom action (toggle_complete)
- JSON responses

### Admin Panel

- List display with filters
- Search functionality
- Inline editing
- Readonly timestamps

## 📚 Project Highlights

**Simplicity**:

- Only 1 model
- 5 fields
- Minimal dependencies
- Clean code

**REST API**:

- Django REST Framework ViewSet
- Serializers for validation
- Router for automatic URL generation
- Browsable API interface

**Best Practices**:

- Class-based views
- Environment configuration
- Proper error handling
- Clean URL structure

## 🔍 API Response Format

**List Response:**

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Learn Django",
      "description": "Complete Django tutorial",
      "completed": false,
      "created_at": "2025-11-01T10:30:00Z",
      "updated_at": "2025-11-01T10:30:00Z"
    }
  ]
}
```

**Single Todo Response:**

```json
{
  "id": 1,
  "title": "Learn Django",
  "description": "Complete Django tutorial",
  "completed": false,
  "created_at": "2025-11-01T10:30:00Z",
  "updated_at": "2025-11-01T10:30:00Z"
}
```

## 🎯 URL Patterns

**Web Interface:**

- `/` → Redirects to `/todos/`
- `/todos/` → List todos
- `/todos/create/` → Create todo
- `/todos/<id>/update/` → Update todo
- `/todos/<id>/delete/` → Delete todo
- `/todos/<id>/toggle/` → Toggle completion

**REST API:**

- `/todos/api/todos/` → List/Create
- `/todos/api/todos/<id>/` → Retrieve/Update/Delete
- `/todos/api/todos/<id>/toggle_complete/` → Toggle

## 🚀 Next Steps

You can extend this app by adding:

- User authentication
- Due dates
- Priority levels
- Categories/Tags
- Search & filter
- Bulk operations
- File attachments

## 📝 License

Open source - Free to use for learning

---

**Simple. Clean. Functional.** 🎉

## 🌟 Features

- ✅ **Full CRUD Operations** for Products and Categories
- 🎨 **Modern UI** with Bootstrap 5 and Bootstrap Icons
- 🔍 **Search & Filter** functionality for products
- 📱 **Responsive Design** - works on all devices
- 🖼️ **Image Upload** support for products
- 📊 **Product Status** management (Active, Inactive, Out of Stock)
- ⭐ **Featured Products** section
- 📈 **Stock Management** with visual indicators
- 🏷️ **Category Management** system
- 💬 **Success Messages** for user feedback
- 🔐 **Django Admin** panel for advanced management
- 📄 **Pagination** for large datasets

## 📁 Project Structure

```
Django CRUD Project/
│
├── core/                      # Main project settings
│   ├── __init__.py
│   ├── settings.py           # Project settings with best practices
│   ├── urls.py               # Main URL configuration
│   └── wsgi.py
│
├── products/                  # Products app
│   ├── migrations/           # Database migrations
│   ├── __init__.py
│   ├── admin.py             # Admin panel configuration
│   ├── apps.py
│   ├── forms.py             # Product and Category forms
│   ├── models.py            # Product and Category models
│   ├── urls.py              # App-specific URLs
│   └── views.py             # Class-based views for CRUD
│
├── templates/                # HTML templates
│   ├── base.html            # Base template with navbar & footer
│   ├── home.html            # Homepage
│   └── products/            # Product templates
│       ├── product_list.html
│       ├── product_detail.html
│       ├── product_form.html
│       ├── product_confirm_delete.html
│       ├── category_list.html
│       ├── category_detail.html
│       ├── category_form.html
│       └── category_confirm_delete.html
│
├── static/                   # Static files
│   └── css/
│       └── style.css        # Custom CSS
│
├── media/                    # User uploaded files (created automatically)
│   └── products/
│
├── .env.example             # Environment variables template
├── .gitignore              # Git ignore file
├── manage.py               # Django management script
└── requirements.txt        # Python dependencies
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (optional)

### Installation

1. **Clone or navigate to the project directory:**

   ```bash
   cd "c:\Users\BS00956\OneDrive - Brain Station 23\Desktop\BS1813 Personal\Django CRUD Project"
   ```

2. **Activate the virtual environment:**

   ```bash
   .venv\Scripts\Activate.ps1
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create environment file:**

   ```bash
   copy .env.example .env
   ```

5. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (for admin access):**

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create your admin account.

7. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

8. **Open your browser and visit:**
   - Homepage: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## 📖 Usage Guide

### Managing Products

1. **View All Products**

   - Navigate to "Products" from the navbar
   - Use search and filters to find specific products
   - Click on any product to view details

2. **Create New Product**

   - Click "Add New Product" button
   - Fill in the required fields:
     - Name (required)
     - Description (required)
     - SKU (required, unique)
     - Price (required)
     - Quantity (required)
     - Category (optional)
     - Status (Active/Inactive/Out of Stock)
     - Image (optional)
     - Featured (checkbox)
   - Click "Create Product"

3. **Update Product**

   - Go to product detail page
   - Click "Edit Product" button
   - Update the fields
   - Click "Update Product"

4. **Delete Product**
   - Go to product detail page
   - Click "Delete Product" button
   - Confirm the deletion

### Managing Categories

1. **View All Categories**

   - Navigate to "Categories" from the navbar
   - View all categories with product counts

2. **Create New Category**

   - Click "Add New Category" button
   - Enter category name and description
   - Click "Create Category"

3. **View Category Products**

   - Click on any category card
   - View all products in that category

4. **Update/Delete Category**
   - Similar to product management

### Search & Filter

- **Search**: Enter keywords to search in product name, description, or SKU
- **Filter by Category**: Select a category from dropdown
- **Filter by Status**: Select status (Active, Inactive, Out of Stock)
- Click "Search" to apply filters

## 🎨 Key Features Explained

### Models

**Product Model:**

- Name, Description, SKU
- Price (Decimal field)
- Quantity (Integer)
- Category (Foreign Key)
- Status (Choice field)
- Image (File upload)
- Featured flag
- Timestamps (auto)

**Category Model:**

- Name (Unique)
- Description
- Related products
- Timestamps (auto)

### Views (Class-Based Views)

- `ListView` - Display all items with pagination
- `DetailView` - Show single item details
- `CreateView` - Form for creating new items
- `UpdateView` - Form for updating existing items
- `DeleteView` - Confirmation before deletion

### Forms

- Bootstrap-styled forms
- Client-side validation
- Custom validation rules
- File upload handling

### Templates

- Template inheritance with `base.html`
- Bootstrap 5 responsive design
- Bootstrap Icons
- Django template tags and filters
- Context processors for messages

## 🔧 Configuration

### Environment Variables (.env)

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Settings Highlights

- **INSTALLED_APPS**: Includes `products` app
- **TEMPLATES**: Configured for `templates/` directory
- **STATIC_FILES**: Configured for development and production
- **MEDIA_FILES**: Configured for user uploads
- **TIME_ZONE**: Set to 'Asia/Dhaka'
- **MESSAGES**: Bootstrap-compatible message tags

## 🛡️ Best Practices Implemented

1. **Code Organization**

   - Separate apps for different functionalities
   - Clean separation of concerns (MVT pattern)
   - Reusable components

2. **Security**

   - Secret key in environment variables
   - CSRF protection enabled
   - SQL injection prevention (Django ORM)
   - XSS protection

3. **Database**

   - Model indexing for performance
   - Proper field types and constraints
   - Cascade delete handling

4. **Forms & Validation**

   - Server-side validation
   - Clean data methods
   - User-friendly error messages

5. **UI/UX**

   - Responsive design
   - Consistent styling
   - Loading states
   - Success/Error messages
   - Breadcrumb navigation

6. **Performance**
   - `select_related()` to reduce queries
   - Pagination for large datasets
   - Efficient querysets

## 📦 Dependencies

- **Django 5.2.7** - Web framework
- **python-decouple** - Environment variable management
- **Pillow** - Image processing
- **Bootstrap 5.3** - Frontend framework (CDN)
- **Bootstrap Icons** - Icon library (CDN)

## 🎯 Future Enhancements

- [ ] User authentication and authorization
- [ ] API endpoints (Django REST Framework)
- [ ] Advanced search with filters
- [ ] Export data to CSV/Excel
- [ ] Product reviews and ratings
- [ ] Inventory alerts
- [ ] Order management system
- [ ] Payment integration
- [ ] Multi-language support
- [ ] Docker containerization

## 🐛 Troubleshooting

### Common Issues

1. **Port already in use:**

   ```bash
   python manage.py runserver 8001
   ```

2. **Static files not loading:**

   ```bash
   python manage.py collectstatic
   ```

3. **Database issues:**
   ```bash
   # Delete db.sqlite3 and migrations (except __init__.py)
   python manage.py makemigrations
   python manage.py migrate
   ```

## 📝 License

This project is open-source and available for educational purposes.

## 👨‍💻 Author

Built with ❤️ using Django

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📧 Support

If you have any questions or need help, please open an issue in the repository.

---

**Happy Coding! 🚀**
