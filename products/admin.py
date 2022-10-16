from django.contrib import admin

from .models import Product, Comment

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'price']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product' ,'author', 'active']
