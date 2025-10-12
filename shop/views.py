from django.shortcuts import render

# 🏠 الصفحة الرئيسية للمتجر
def home(request):
    return render(request, 'home.html')
