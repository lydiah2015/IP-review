from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Project,Profile,Comment
# from .forms import ProfileForm
# Create your views here.

@login_required(login_url='/accounts/login/')
def posts(request):
    project = Project.objects.all()
    return render(request, 'all-posts/posts.html',{"projects":project})

def my_profile(request):
    user = request.user
    return render(request, "my_profile.html", {"user": user, "current_user": request.user})  

# def update_profile(request):
#     user = request.user
#     if request.method == "POST":
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             new_biography = form.cleaned_data['biography']
#             new_photo = form.cleaned_data['profile_photos'] 
#             profile = Profile.objects.get(user=request.user)
#             profile.biography = new_biography
#             profile.profile_photos = new_photo
#             profile.save()
#             final_url = "/profile/" + str(request.user.id) + "/"
#             return redirect(final_url)
#     else:
#         form = ProfileForm()
#     return render(request, "update_profile.html", {"form": form})

