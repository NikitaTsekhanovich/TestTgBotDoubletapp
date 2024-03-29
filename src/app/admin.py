from django.contrib import admin
from app.internal.models.telegram_user import TelegramUser
from app.internal.admin.admin_user import AdminUserAdmin

admin.site.site_title = "Backend course"
admin.site.site_header = "Backend course"


class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('external_id', 'phone_number', 'username')


admin.site.register(TelegramUser, TelegramUserAdmin)
