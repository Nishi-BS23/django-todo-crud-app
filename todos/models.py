from django.db import models


class Todo(models.Model):
    """
    Todo Model - একটি সিম্পল টুডু মডেল
    
    এই মডেলে একজন ইউজার তার কাজের তালিকা রাখতে পারবে
    """
    
    # টাইটেল ফিল্ড - টুডুর নাম (সর্বোচ্চ ২০০ অক্ষর)
    title = models.CharField(max_length=200)
    
    # বিস্তারিত বর্ণনা (ঐচ্ছিক - blank=True মানে খালি রাখা যাবে)
    description = models.TextField(blank=True)
    
    # টুডু সম্পন্ন হয়েছে কিনা (ডিফল্ট: False মানে সম্পন্ন হয়নি)
    completed = models.BooleanField(default=False)
    
    # কখন তৈরি হয়েছে (অটোমেটিক সেভ হবে)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # সর্বশেষ কখন আপডেট হয়েছে (অটোমেটিক আপডেট হবে)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        # ডাটাবেসে কিভাবে সাজানো হবে (নতুন আগে দেখাবে)
        ordering = ['-created_at']
        
        # এডমিন প্যানেলে একবচন নাম
        verbose_name = 'Todo'
        
        # এডমিন প্যানেলে বহুবচন নাম
        verbose_name_plural = 'Todos'
    
    def __str__(self):
        """
        অবজেক্ট প্রিন্ট করলে কি দেখাবে
        রিটার্ন করবে টুডুর টাইটেল
        """
        return self.title
