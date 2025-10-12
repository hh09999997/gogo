from django.db import models
from django.utils.translation import gettext_lazy as _


# نموذج أولي بسيط كمثال (قابل للتوسّع لاحقًا)
class Profile(models.Model):
    name = models.CharField(_("الاسم الكامل"), max_length=100)
    email = models.EmailField(_("البريد الإلكتروني"), unique=True)
    created_at = models.DateTimeField(_("تاريخ الإنشاء"), auto_now_add=True)

    class Meta:
        verbose_name = _("ملف مستخدم")
        verbose_name_plural = _("ملفات المستخدمين")

    def __str__(self):
        return self.name
