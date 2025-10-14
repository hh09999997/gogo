from django.urls import path

app_name = 'shop'

urlpatterns = [
]
from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),  # ✅ الصفحة الرئيسية
    path('products/', views.product_list, name='product_list'),
]

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
