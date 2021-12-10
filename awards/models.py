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


