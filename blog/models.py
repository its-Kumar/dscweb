from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import Q


# Create your models here.
User = settings.AUTH_USER_MODEL

class BlogPostManager(models.Manager):
    '''def published(self):
        now = timezone.now()
        return self.get_queryset().filter(publish_date__lte=now)
    '''
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
        return self.filter(publish_date__lte=now)

    def search(self, query):
        lookup = (
            Q(title__icontains=query) | 
            Q(content__contains = query) |
            Q(slug__icontains = query)
                )
        return self.filter(lookup)


class BlogPost(models.Model):
    user = models.ForeignKey(User, default=1, null = True, on_delete = models.SET_NULL)
    title = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=False)
    content = models.TextField(null=True,blank=True)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True )
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = BlogPostManager()

    class Meta:
        ordering = ['-publish_date', '-updated', '-timestamp']

    def get_absolute_url(self):
        return f"/blog/{self.slug}"

    def get_edit_url(self):
        return f"/blog/{self.slug}/edit"

    def get_delete_url(self):
        return f"/{self.get_absolute_url()}/delete"


class Blog:
    title = "hello world"
    content = "something cool"
