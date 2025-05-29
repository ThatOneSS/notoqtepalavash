from django.contrib import admin

# Register your models here.
from .models import Category, Product , Branch


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('status', 'name')
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('status', 'name', 'price', 'category')
    search_fields = ('name',)
    list_filter = ('category','status')

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('status', 'name', )
    search_fields = ('name',)
    list_filter = ('status',)