from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='image/')
    biography = models.CharField(max_length=50)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')


class Projects(models.Model):
    user = models.ForeignKey(User, related_name="posts", blank=True)
    image = ImageField(blank=True, manual_crop="")
    description = models.CharField(max_length=50)
    comments = models.CharField(max_length=50)
