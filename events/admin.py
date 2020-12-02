from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'date', 'is_active']
    list_display_links = ['description', 'date']
    list_editable = ['title', 'is_active']
    list_filter = ['title', 'date', 'is_active']
    search_fields = ['title', 'slug', 'description']
    actions = ['activate']

    def activate(self, request, queryset):
        queryset.update(is_active=True)


# Register your models here.
admin.site.register(Event, EventAdmin)
