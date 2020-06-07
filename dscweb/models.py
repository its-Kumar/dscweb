from django.db import models

class Member(models.Model):
    pic         = models.ImageField(upload_to='images/members/')
    first_name  = models.CharField(max_length=50, null=False)
    last_name   = models.CharField(max_length=50, null=False)
    mobile      = models.CharField(max_length=12, null=False)
    email       = models.EmailField()
    title       = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=100)
    facebook    = models.URLField(null=True, blank=True)
    linkedin    = models.URLField(null=True, blank=True)
    github      = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return f"/member/{self.first_name}"
    
