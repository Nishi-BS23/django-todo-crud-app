from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    """
    Todo Serializer - টুডু ডাটা JSON এ কনভার্ট করার জন্য
    
    এটি Django Model কে JSON ফরম্যাটে পরিবর্তন করে যাতে API তে ব্যবহার করা যায়
    এবং JSON থেকে Model এ কনভার্ট করে ডাটাবেসে সেভ করতে পারে
    """
    
    class Meta:
        model = Todo  # কোন মডেল ব্যবহার করবো
        
        # কোন কোন ফিল্ড API তে দেখাবে
        fields = ['id', 'title', 'description', 'completed', 'created_at', 'updated_at']
        
        # যে ফিল্ডগুলো শুধু পড়া যাবে, পরিবর্তন করা যাবে না
        # (id, created_at, updated_at অটোমেটিক তৈরি হয়)
        read_only_fields = ['id', 'created_at', 'updated_at']
