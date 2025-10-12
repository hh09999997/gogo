from django.db import models
from django.utils.translation import gettext_lazy as _


# نموذج فئة أولي لتصنيف الألعاب
class Category(models.Model):
    name = models.CharField(_("اسم الفئة"), max_length=100)
    description = models.TextField(_("الوصف"), blank=True, null=True)

    class Meta:
        verbose_name = _("فئة")
        verbose_name_plural = _("الفئات")

    def __str__(self):
        return self.name


# نموذج منتج بسيط مبدئي
class Product(models.Model):
    name = models.CharField(_("اسم اللعبة"), max_length=150)
    price = models.DecimalField(_("السعر"), max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(_("تاريخ الإضافة"), auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")

    class Meta:
        verbose_name = _("منتج")
        verbose_name_plural = _("المنتجات")

    def __str__(self):
        return self.name
