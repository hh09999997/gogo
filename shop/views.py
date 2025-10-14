from django.shortcuts import render
from .models import Product


# 🏠 الصفحة الرئيسية المؤقتة
def home(request):
    return render(request, 'home.html')


# 🧸 عرض جميع المنتجات في صفحة خاصة
def product_list(request):
    # 🔹 جلب كل المنتجات من قاعدة البيانات
    products = Product.objects.all()

    # 🔹 تمريرها إلى القالب
    return render(request, 'shop/products.html', {'products': products})
