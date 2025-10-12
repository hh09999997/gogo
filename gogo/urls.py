"""
URL configuration for gogo project.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # 🧭 لوحة تحكم Django الافتراضية
    path('admin/', admin.site.urls),

    # 👥 تطبيق الحسابات (account)
    path('account/', include('account.urls')),

    # 🛍️ تطبيق المتجر (shop)
    path('', include('shop.urls')),  # الصفحة الرئيسية من المتجر

    # 📊 تطبيق لوحة التحكم (dashboard)
    path('dashboard/', include('dashboard.urls')),
]


# 🖼️ إعداد عرض الملفات الإعلامية أثناء التطوير فقط
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
