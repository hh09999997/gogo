from django.contrib import admin
from .models import AdminNotification


@admin.register(AdminNotification)
class AdminNotificationAdmin(admin.ModelAdmin):
    list_display = ('message', 'is_read', 'created_at')
    list_filter = ('is_read',)
    search_fields = ('message',)
    ordering = ('-created_at',)

    class Meta:
        verbose_name = "تنبيه إداري"
        verbose_name_plural = "التنبيهات الإدارية"
