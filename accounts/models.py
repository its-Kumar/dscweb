from django.db import models

from blog.models import User

GENDER_CHOICES = (("M", "Male"), ("F", "Female"))


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128)
    email = models.EmailField()
    profile_pic = models.ImageField(
        upload_to="images", default="images/profile1.png", null=True, blank=True
    )
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.first_name
