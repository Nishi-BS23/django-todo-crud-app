"""
URL Configuration - টুডু এপ্লিকেশনের সব URL
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# ============================================
# REST API Router - API URL অটোমেটিক তৈরি করবে
# ============================================
router = DefaultRouter()

# 'todos' prefix দিয়ে ViewSet রেজিস্টার করা
# এটি অটোমেটিক্যালি নিচের URL গুলো তৈরি করবে:
# - /api/todos/
# - /api/todos/{id}/
# - /api/todos/{id}/toggle_complete/
router.register(r'todos', views.TodoViewSet, basename='todo')

# ============================================
# URL Patterns - সব রুট এখানে ডিফাইন করা
# ============================================
urlpatterns = [
    # ওয়েব ইন্টারফেস URLs
    path('', views.todo_list, name='todo_list'),                    # হোম পেজ - সব টুডু দেখাবে
    path('create/', views.todo_create, name='todo_create'),         # নতুন টুডু তৈরি
    path('<int:pk>/update/', views.todo_update, name='todo_update'), # টুডু আপডেট (pk = todo এর ID)
    path('<int:pk>/delete/', views.todo_delete, name='todo_delete'), # টুডু মুছা
    path('<int:pk>/toggle/', views.todo_toggle, name='todo_toggle'), # টুডু টগল (complete/incomplete)
    
    # REST API URLs - router থেকে সব API URL যোগ করা
    path('api/', include(router.urls)),
]
