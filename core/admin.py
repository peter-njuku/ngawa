from django.contrib import admin
from .models import ContactMessage, Products

# Register your models here.
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display=('name','email','submitted_at')
    search_fields=('name','email','message')
    list_filter=('submitted_at',)\

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','category','price','created_at')
    search_fiels=('name',)
    list_filter=('category',)
