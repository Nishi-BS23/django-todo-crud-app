from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer


# ============================================
# REST API ViewSet - API এর জন্য
# ============================================

class TodoViewSet(viewsets.ModelViewSet):
    """
    Todo ViewSet - REST API এর জন্য সব CRUD অপারেশন
    
    এই ক্লাস অটোমেটিক্যালি নিচের API endpoint তৈরি করবে:
    - GET /api/todos/           → সব টুডু দেখার জন্য
    - POST /api/todos/          → নতুন টুডু তৈরির জন্য
    - GET /api/todos/{id}/      → একটি টুডু দেখার জন্য
    - PUT /api/todos/{id}/      → টুডু আপডেট করার জন্য
    - PATCH /api/todos/{id}/    → টুডু আংশিক আপডেট করার জন্য
    - DELETE /api/todos/{id}/   → টুডু মুছার জন্য
    """
    
    # ডাটাবেস থেকে সব টুডু নিয়ে আসা
    queryset = Todo.objects.all()
    
    # কোন সিরিয়ালাইজার ব্যবহার করবো (JSON কনভার্শনের জন্য)
    serializer_class = TodoSerializer
    
    @action(detail=True, methods=['post'])
    def toggle_complete(self, request, pk=None):
        """
        কাস্টম এক্শন - টুডু কমপ্লিট/ইনকমপ্লিট টগল করার জন্য
        URL: POST /api/todos/{id}/toggle_complete/
        """
        todo = self.get_object()  # ID দিয়ে টুডু খুঁজে বের করা
        todo.completed = not todo.completed  # উল্টো করা (True->False বা False->True)
        todo.save()  # ডাটাবেসে সেভ করা
        
        serializer = self.get_serializer(todo)  # JSON এ কনভার্ট করা
        return Response(serializer.data)  # রেসপন্স পাঠানো


# ============================================
# Traditional Django Views - ওয়েব ইন্টারফেসের জন্য
# ============================================

def todo_list(request):
    """
    সব টুডু দেখানোর ভিউ
    URL: GET /todos/
    """
    todos = Todo.objects.all()  # ডাটাবেস থেকে সব টুডু নিয়ে আসা
    return render(request, 'todos/todo_list.html', {'todos': todos})


def todo_create(request):
    """
    নতুন টুডু তৈরি করার ভিউ
    URL: GET/POST /todos/create/
    """
    if request.method == 'POST':
        # ফর্ম সাবমিট হলে (POST request)
        title = request.POST.get('title')  # ফর্ম থেকে টাইটেল নেওয়া
        description = request.POST.get('description', '')  # বর্ণনা নেওয়া
        
        if title:  # টাইটেল থাকলে
            # নতুন টুডু তৈরি করা এবং ডাটাবেসে সেভ করা
            Todo.objects.create(
                title=title,
                description=description
            )
            # টুডু লিস্টে রিডাইরেক্ট করা
            return redirect('todo_list')
    
    # GET request হলে ফর্ম দেখানো
    return render(request, 'todos/todo_form.html', {'action': 'Create'})


def todo_update(request, pk):
    """
    টুডু আপডেট করার ভিউ
    URL: GET/POST /todos/{id}/update/
    pk = Primary Key (টুডুর ID)
    """
    # ID দিয়ে টুডু খুঁজে বের করা, না পেলে 404 error
    todo = get_object_or_404(Todo, pk=pk)
    
    if request.method == 'POST':
        # ফর্ম সাবমিট হলে আপডেট করা
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description', '')
        
        # চেকবক্স চেক করা থাকলে 'on' আসবে
        todo.completed = request.POST.get('completed') == 'on'
        
        todo.save()  # ডাটাবেসে সেভ করা
        return redirect('todo_list')  # লিস্টে ফিরে যাওয়া
    
    # GET request হলে ফর্ম দেখানো (বর্তমান ডাটা সহ)
    return render(request, 'todos/todo_form.html', {
        'todo': todo,
        'action': 'Update'
    })


def todo_delete(request, pk):
    """
    টুডু মুছার ভিউ (কনফার্মেশন সহ)
    URL: GET/POST /todos/{id}/delete/
    """
    todo = get_object_or_404(Todo, pk=pk)  # টুডু খুঁজে বের করা
    
    if request.method == 'POST':
        # কনফার্ম করলে মুছে ফেলা
        todo.delete()
        return redirect('todo_list')
    
    # GET request হলে কনফার্মেশন পেজ দেখানো
    return render(request, 'todos/todo_confirm_delete.html', {'todo': todo})


def todo_toggle(request, pk):
    """
    টুডু কমপ্লিট/ইনকমপ্লিট টগল করা (দ্রুত)
    URL: GET /todos/{id}/toggle/
    """
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = not todo.completed  # উল্টো করা
    todo.save()
    return redirect('todo_list')  # লিস্টে ফিরে যাওয়া
