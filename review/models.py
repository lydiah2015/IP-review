from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='image/')
    biography = models.CharField(max_length=50)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)

class Project(models.Model):
    user = models.ForeignKey(User, blank=True)
    image = models.ImageField(upload_to='image/')
    description = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    rating = models.IntegerField()

    def __str__(self):
        return self.comm

class Comment(models.Model):
    comm = models.TextField(max_length=100)
    user = models.ForeignKey(User,
                             blank=True, on_delete=models.CASCADE)
    project = models.ForeignKey(Project,
                                related_name="project_comments",
                                null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comm



