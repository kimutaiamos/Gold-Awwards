from django.contrib import admin

from awards.models import Profile, Project, Review
from .models import Profile,Project,Review
# Register your models here.
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Review)