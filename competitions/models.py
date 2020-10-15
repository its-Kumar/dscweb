from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.


class Competition(models.Model):

    title = models.CharField(max_length=255,
                             unique=True,
                             blank=False,
                             null=False)
    slug = models.SlugField(default='',
                            editable=False,
                            blank=False,
                            max_length=255)

    image = models.ImageField()
    description = RichTextUploadingField(blank=True, null=True)
    date = models.DateField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date']

    def get_absolute_url(self):
        kwargs = {'pk': self.id, 'slug': self.slug}
        return f"/competitions/{self.id}-{self.slug}/"

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
