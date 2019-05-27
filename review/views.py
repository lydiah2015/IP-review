from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Project, Profile, Comment
from .forms import ProjectForm, ProfileForm
# Create your views here.


@login_required(login_url='/accounts/login/')
def posts(request):
    projects = Project.objects.all()
   #  comments =
    return render(request, 'all-posts/posts.html', {"projects": projects})


def my_profile(request):
    user = request.user
    user_id = request.user.id
    return render(request, "my_profile.html", {"user": user, "current_user": request.user})


def update_profile(request):
    user = request.user
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            new_biography = form.cleaned_data['bio']
            new_photo = form['profile_photo'].data
            profile = Profile.objects.get(user=request.user)
            profile.biography = new_biography
            profile.profile_photo = new_photo
            profile.save()
            final_url = "/accounts/profile/"
            return redirect(final_url)
    else:
        form = ProfileForm()
    return render(request, "update_profile.html", {"form": form})


def comment(request):
    image_id = request.POST["project.id"]
    project = Project.objects.get(id=image_id)
    Comment.objects.create(user=request.user, project=project,
                           comm=request.POST.get("comment"))

    user = request.user.username
    comment = request.POST.get("comment")

    data = {"user": user, "comment": comment, "project-title": project.title,
            "project-description": project.description, "ratings": project.rating}
    return JsonResponse(data)


@login_required(login_url='/accounts/login/')
def new_project(request):

    current_user = request.user.id
    the_user = User.objects.get(id=current_user)
    print(current_user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            form.instance.user = Profile.objects.get(id=current_user)
            # project.author = current_user
            form.save()
            return redirect('/')
    else:
        form = ProjectForm()

    return render(request, 'all-posts/project_form.html', {'form': form})
