from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    #   profile_picture = CloudinaryField('image')
    bio = models.TextField(max_length=600, default="My Bio", blank=True)
    contact = models.CharField(max_length=60, blank=True)
    timestamp = models.DateTimeField(timezone.now())
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", primary_key=True)
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
            if created:
                Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
            instance.profile.save()

    def __str__(self):
         return self.user.username

    def save_profile(self):
            self.save()

    def delete_profile(self):
            self.delete()  

class Project(models.Model):
    title = models.CharField(max_length=60, blank=True)
    # image = CloudinaryField('image')
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



