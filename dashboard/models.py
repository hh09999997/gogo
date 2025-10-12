from django.db import models
from django.utils.translation import gettext_lazy as _


class AdminNotification(models.Model):
    """
    🧭 نموذج يمثل التنبيهات الإدارية في لوحة التحكم.
    يحتوي على نص التنبيه، وتاريخ الإضافة، وحالته (مقروء أم لا).
    """

    message = models.CharField(
        verbose_name=_("نص التنبيه"),
        max_length=255,
        help_text=_("اكتب نص التنبيه الذي سيظهر في لوحة التحكم.")
    )

    created_at = models.DateTimeField(
        verbose_name=_("تاريخ الإضافة"),
        auto_now_add=True
    )

    is_read = models.BooleanField(
        verbose_name=_("تمت القراءة؟"),
        default=False,
        help_text=_("فعّل هذا الخيار إذا تمت قراءة التنبيه.")
    )

    class Meta:
        verbose_name = _("تنبيه إداري")
        verbose_name_plural = _("التنبيهات الإدارية")
        ordering = ['-created_at']  # الأحدث يظهر أولاً

    def __str__(self):
        return f"{self.message} ({'مقروء' if self.is_read else 'غير مقروء'})"
