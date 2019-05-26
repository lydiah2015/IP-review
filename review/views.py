from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url='/accounts/login/')
def posts(request):
    return render(request, 'all-posts/posts.html')
