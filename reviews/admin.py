from django.contrib import admin
from .models import Review, Reply

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'stars', 'created_at')

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('review', 'user', 'created_at')