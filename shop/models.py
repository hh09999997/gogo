from django.db import models
from django.utils.translation import gettext_lazy as _


# 🏷️ نموذج الفئة (تصنيف الألعاب)
class Category(models.Model):
    name = models.CharField(_("اسم الفئة"), max_length=100)
    description = models.TextField(_("الوصف"), blank=True, null=True)

    class Meta:
        verbose_name = _("فئة")                 # يظهر في لوحة التحكم
        verbose_name_plural = _("الفئات")       # جمع الاسم في لوحة التحكم
        ordering = ["name"]                     # ترتيب الفئات أبجديًا

    def __str__(self):
        return self.name


# 🧸 نموذج المنتج (اللعبة)
class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name=_("الفئة"),                # اسم الحقل في لوحة التحكم
    )
    name = models.CharField(_("اسم اللعبة"), max_length=150)
    description = models.TextField(_("الوصف"), blank=True, null=True)
    price = models.DecimalField(_("السعر"), max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField(_("الكمية في المخزون"), default=0)
    created_at = models.DateTimeField(_("تاريخ الإضافة"), auto_now_add=True)

    class Meta:
        verbose_name = _("منتج")                # يظهر في لوحة التحكم
        verbose_name_plural = _("المنتجات")     # جمع الاسم في لوحة التحكم
        ordering = ["-created_at"]              # الأحدث أولاً

    def __str__(self):
        return f"{self.name} - {self.category.name}"
