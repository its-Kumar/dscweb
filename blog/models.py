import itertools
import os

from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
User = settings.AUTH_USER_MODEL


def get_upload_path(instance, filename):
    return os.path.join(
        "user_%d" % instance.user.id, "blog_%s" % instance.slug, filename
    )


class BlogPostManager(models.Manager):
    """def published(self):
    now = timezone.now()
    return self.get_queryset().filter(publish_date__lte=now)
    """

    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)


class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(draft=False).filter(publish_date__lte=now)

    def search(self, query):
        lookup = (
            Q(title__icontains=query)
            | Q(content__contains=query)
            | Q(slug__icontains=query)
        )
        return self.filter(lookup)


class BlogPost(models.Model):
    user = models.ForeignKey("auth.User", default=1,
                             on_delete=models.SET_DEFAULT)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    slug = models.SlugField(unique=True, default="",
                            editable=False, blank=False)
    # content = models.TextField(null=True, blank=True)
    content = RichTextUploadingField(blank=True, null=True)
    draft = models.BooleanField(default=False)
    publish_date = models.DateTimeField(auto_now_add=False, auto_now=False)
    timestamp = models.DateTimeField(default=timezone.now, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    objects = BlogPostManager()

    def _generate_slug(self):
        value = self.title
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if not BlogPost.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = "{}-{}".format(slug_original, i)

        self.slug = slug_candidate

    def save(self, *args, **kwargs):
        if not self.pk:
            self._generate_slug()

        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-publish_date", "-updated", "-timestamp"]

    def get_absolute_url(self):
        return reverse('blog:view', kwargs={"slug": self.slug})

    def get_edit_url(self):
        return reverse('blog:edit', kwargs={"slug": self.slug})

    def get_delete_url(self):
        return reverse('blog:del', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class Blog:
    title = "hello world"
    content = "something cool"


class Comment(models.Model):
    post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name="comments"
    )
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)
