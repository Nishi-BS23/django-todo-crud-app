"""
Django Admin Configuration - এডমিন প্যানেল কাস্টমাইজেশন
"""

from django.contrib import admin
from .models import Todo


@admin.register(Todo)  # Todo মডেলকে এডমিনে রেজিস্টার করা
class TodoAdmin(admin.ModelAdmin):
    """
    Todo Admin - এডমিন প্যানেলে টুডু কিভাবে দেখাবে
    """
    
    # লিস্ট পেজে কোন কোন ফিল্ড দেখাবে
    list_display = ['title', 'completed', 'created_at', 'updated_at']
    
    # কোন ফিল্ড দিয়ে ফিল্টার করা যাবে
    list_filter = ['completed', 'created_at']
    
    # কোন ফিল্ডে সার্চ করা যাবে
    search_fields = ['title', 'description']
    
    # লিস্ট পেজ থেকেই এডিট করা যাবে এই ফিল্ড
    list_editable = ['completed']
    
    # যে ফিল্ড এডিট করা যাবে না (শুধু দেখা যাবে)
    readonly_fields = ['created_at', 'updated_at']
