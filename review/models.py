from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='image/')
    biography = models.TextField(max_length=50)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')

class Project(models.Model):
    user = models.ForeignKey(Profile, related_name='projects',  on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/')
    description = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    rating = models.IntegerField(blank=True)
    url = models.CharField(max_length=140)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comm = models.TextField(max_length=100)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    project = models.ForeignKey(Project,
                                related_name="project_comments",
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.comm



