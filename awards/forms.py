from django.forms import fields
from awards.models import Profile, Project, Review
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'passwprd1', 'password2']
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','timestamp']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','profile','timestamp']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['user','project','average']