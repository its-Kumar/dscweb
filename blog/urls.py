from django.urls import path

from .views import (blog_post_delete_view, blog_post_detail_view,
                    blog_post_list_view, blog_post_update_view)

app_name = "blog"
urlpatterns = [
    path("", blog_post_list_view, name="blogs"),
    path("<str:slug>/", blog_post_detail_view, name="view"),
    path("<str:slug>/edit/", blog_post_update_view, name="edit"),
    path("<str:slug>/delete/", blog_post_delete_view, name="del"),
]
