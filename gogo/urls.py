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
# 🖼️ إعداد عرض الملفات الثابتة والإعلامية أثناء التطوير
# ----------------------------------------
if settings.DEBUG:
    # 📸 عرض ملفات الوسائط (Media) — مثل صور المنتجات والمستخدمين
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # 🎨 عرض ملفات Static (CSS / JS / Images) أثناء التطوير
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# ----------------------------------------
# 🧩 تخصيص واجهة لوحة الإدارة (Admin Interface)
# ----------------------------------------
admin.site.site_header = "🎠 لوحة إدارة متجر ألعاب الأطفال"
admin.site.site_title = "إدارة موقع Gogo"
admin.site.index_title = "مرحبًا بك في لوحة التحكم الإدارية"


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
