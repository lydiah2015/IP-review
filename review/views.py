from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Project,Profile,Comment
# Create your views here.

@login_required(login_url='/accounts/login/')
def posts(request):
    project = Project.objects.all()
    return render(request, 'all-posts/posts.html',{"projects":project})
