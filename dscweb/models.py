from django.db import models

class Member(models.Model):
    username    = models.CharField(max_length=25, null=False)
    first_name  = models.CharField(max_length=50, null=False)
    last_name   = models.CharField(max_length=50, null=False)
    mobile      = models.CharField(max_length=12, null=False)
    email       = models.EmailField()
    password    = models.CharField(max_length=18, null=False, blank=False)

