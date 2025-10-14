from django.shortcuts import render
from .models import Product


# 🏠 الصفحة الرئيسية (تظهر فيها آخر المنتجات)
def home(request):
    # 🔹 جلب آخر 6 منتجات مضافة
    latest_products = Product.objects.all().order_by('-created_at')[:6]
    return render(request, 'home.html', {'latest_products': latest_products})


# 🧸 صفحة عرض كل المنتجات
def product_list(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'shop/products.html', {'products': products})
