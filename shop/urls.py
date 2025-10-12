from django.urls import path

app_name = 'shop'

urlpatterns = [
    # لاحقًا سنضيف الصفحة الرئيسية للمتجر مثل:
    # path('', views.home, name='home'),
    # path('product/<int:id>/', views.product_detail, name='product_detail'),
]
from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),  # ✅ الصفحة الرئيسية
]
