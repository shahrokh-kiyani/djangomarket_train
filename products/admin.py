from django.contrib import admin

from .models import Product, Comment


class CommentInline(admin.StackedInline):
    model = Comment
    fields = ['author', 'text', 'stars', 'active']
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'price']
    inlines = [CommentInline, ]
