from django.db import models
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    # 🧍 الاسم الكامل للمستخدم
    name = models.CharField(
        verbose_name=_("الاسم الكامل"),
        max_length=100
    )

    # 📧 البريد الإلكتروني
    email = models.EmailField(
        verbose_name=_("البريد الإلكتروني"),
        unique=True
    )

    # 🕒 تاريخ إنشاء الحساب
    created_at = models.DateTimeField(
        verbose_name=_("تاريخ الإنشاء"),
        auto_now_add=True
    )

    class Meta:
        verbose_name = _("ملف المستخدم")
        verbose_name_plural = _("ملفات المستخدمين")
        ordering = ['-created_at']  # ترتيب تنازلي حسب الأحدث

    def __str__(self):
        return f"{self.name} ({self.email})"
