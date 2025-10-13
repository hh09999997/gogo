from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile


# 🧩 إنشاء حساب جديد
def register_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        # ✅ التحقق من وجود البريد مسبقًا
        if Profile.objects.filter(email=email).exists():
            messages.error(request, "هذا البريد الإلكتروني مسجل مسبقًا ❌")
            return redirect('account:register')

        # 🆕 إنشاء حساب جديد
        Profile.objects.create(name=name, email=email)
        messages.success(request, "تم إنشاء الحساب بنجاح 🎉")
        return redirect('account:login')

    return render(request, 'account/register.html')


# 🔑 تسجيل الدخول
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            profile = Profile.objects.get(email=email)
            messages.success(request, f"مرحبًا بك {profile.name} 👋")
            return render(request, 'account/welcome.html', {'profile': profile})
        except Profile.DoesNotExist:
            messages.error(request, "البريد الإلكتروني غير موجود ❌")
            return redirect('account:login')

    return render(request, 'account/login.html')
