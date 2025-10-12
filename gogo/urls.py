"""
URL configuration for gogo project.

Documentation:
https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# ----------------------------------------
# 🧭 تعريف المسارات الأساسية للمشروع
# ----------------------------------------
urlpatterns = [
    # 🎛️ لوحة تحكم Django الافتراضية
    path('admin/', admin.site.urls),

    # 👥 تطبيق الحسابات (Account)
    path('account/', include('account.urls')),

    # 🛍️ تطبيق المتجر (Shop) — الصفحة الرئيسية للموقع
    path('', include('shop.urls')),

    # 📊 تطبيق لوحة التحكم الداخلية (Dashboard)
    path('dashboard/', include('dashboard.urls')),
]


# ----------------------------------------
# 🖼️ عرض ملفات الوسائط والإستايل أثناء التطوير
# ----------------------------------------
if settings.DEBUG:
    # ملفات الوسائط (مثل صور المنتجات)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # ملفات static (CSS / JS) أثناء التطوير
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# ----------------------------------------
# 📘 تخصيص عنوان لوحة الإدارة باللغة العربية
# ----------------------------------------
admin.site.site_header = "لوحة إدارة متجر ألعاب الأطفال 🎠"
admin.site.site_title = "إدارة الموقع"
admin.site.index_title = "مرحبًا بك في لوحة التحكم"
