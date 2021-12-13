from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profilepics/', default='Image')

    bio = models.TextField(max_length=600, default="bio", blank=True)
    contact = models.CharField(max_length=60, blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)

    def save_profile(self):
        self.save()
    
    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains = name)
        return profile
    
    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile

class Project(models.Model):
    title = models.CharField(max_length=60, blank=True)
    project_photo = models.ImageField(upload_to = 'projectpics/', default='Image')
    description = models.TextField(max_length=500)
    link = models.URLField(blank=True)
    user = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,null=True,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def project_by_id(cls,id):
        project = Project.objects.filter(id =id)
        return project

    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects
        
class Review(models.Model):
    REVIEW_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    design = models.IntegerField(choices=REVIEW_CHOICES,default=0,blank=False)
    usability = models.IntegerField(choices=REVIEW_CHOICES,default=0,blank=False)
    content = models.IntegerField(choices=REVIEW_CHOICES,default=0,blank=False)
    average =  models.DecimalField(default=1,blank=False,decimal_places=2,max_digits=40)
    project = models.ForeignKey(Project,null=True,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.user

    def save_review(self):
        self.save()

    def delete_review(self):
        self.delete()




