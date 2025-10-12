from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)

    class Meta:
        verbose_name = "فئة"
        verbose_name_plural = "الفئات"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('name',)
    ordering = ('-created_at',)

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"
