from django.contrib import admin

from subscriptions.models import Packets

# admin.site.register(Packets)


@admin.register(Packets)
class packetsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"description": ("name",)}
