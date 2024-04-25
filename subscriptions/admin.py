from django.contrib import admin

from subscriptions.models import Packets

# admin.site.register(Packets)


@admin.register(Packets)
class packetsAdmin(admin.ModelAdmin):
    # Убедитесь, что используете существующие поля
    list_display = ('name', 'price', 'duration')  # Добавьте поля, которые хотите видеть в админ-панели
    # prepopulated_fields = {"slug": ("name",)}  # Пример, если бы у вас было поле slug
