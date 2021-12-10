from awards.permissions import IsAdminOrReadOnly
from awards.serializer import ProfileSerializer, ProjectSerializer
from django.http.response import HttpResponseRedirect
from awards.models import Profile, Project, Review
from awards.forms import ProfileForm, ProjectForm, ReviewForm, SignUpForm, UserUpdateForm
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.




def index(request):
    profiles = Profile.objects.all()
    projects = Project.objects.all()
    reviews = Review.objects.all()

    context ={"profiles":profiles,"projects":projects,"reviews":reviews}

    return render(request,'index.html',context)


def registration(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=user_password)
            login(request, user)
            return redirect('login')
        else:
            form= SignUpForm()
            return render(request, 'registration/registration_form.html', {"form":form})



@login_required(login_url='/accounts/login/')
def search_projects(request):
    if 'title' in request.GET and request.GET["title"]:

        search_term = request.GET.get("title")
        found_projects =  Project.search_by_title(search_term)
        message = f"{search_term}"
        print(search_term)
        context = {"found_projects":found_projects,"message":message}

        return render(request, 'search.html',context)

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

