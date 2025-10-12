from django.db import models
from django.utils.translation import gettext_lazy as _


# نموذج مبدئي بسيط لعرض التنبيهات في لوحة التحكم
class AdminNotification(models.Model):
    message = models.CharField(_("نص التنبيه"), max_length=255)
    created_at = models.DateTimeField(_("تاريخ الإضافة"), auto_now_add=True)
    is_read = models.BooleanField(_("تمت القراءة؟"), default=False)

    class Meta:
        verbose_name = _("تنبيه إداري")
        verbose_name_plural = _("التنبيهات الإدارية")

    def __str__(self):
        return self.message
