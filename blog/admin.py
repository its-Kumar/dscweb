from django.contrib import admin

# Register your models here.
from .models import BlogPost, Comment


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish_date', 'updated', 'draft']
    list_filter = ['title', 'publish_date', 'draft']
    list_display_links = ['title', 'publish_date']
    search_fields = ['title', 'content', 'slug', 'publish_date']
    actions = ['draft', 'publish']

    def draft(self, request, queryset):
        queryset.update(draft=True)

    def publish(self, request, queryset):
        queryset.update(draft=False)


admin.site.register(BlogPost, BlogPostAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "body", "post", "created_on", "active")
    list_filter = ("active", "created_on")
    search_fields = ("name", "email", "body")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
