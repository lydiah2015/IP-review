from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile, Project, Comment


class ProjectForm(forms.ModelForm):
    '''
    New project creation form.
    '''

    title = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Project Title'}))
    description = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Description'}))
    url = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Project Link'}))
    rating = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Project rating'}))

    class Meta:
        model = Project
        fields = ['title', 'image', 'description', 'url', 'rating']


class ProfileForm(forms.ModelForm):
    '''
    New project creation form.
    '''

    bio = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Input Bio, something catchy'}))

    class Meta:
        model = Profile
        fields = ['bio', 'profile_photo']
