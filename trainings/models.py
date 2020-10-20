from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.


class Training(models.Model):
    title = models.CharField(max_length=255,
                             unique=True,
                             blank=False,
                             null=False)
    image = models.ImageField()
    description = RichTextUploadingField(blank=True, null=True)
    date = models.DateField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date']

    def __str__(self) -> str:
        return self.title
