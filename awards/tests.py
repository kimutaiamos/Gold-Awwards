from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
import datetime as dt
from django.utils import timezone
# Create your tests here.

class ProfileTestClass(TestCase):
    def setUp(self):
        '''
        test case for profiles
        '''
        self.user = User(username='Kiprotich')
        self.user.save()
        self.profile = Profile( profile_picture='black and orange',bio='programmer',contact="0701111780",user=self.user)
        self.profile.save_profile()

    def tearDown(self):
        Profile.objects.all().delete()
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
    
    def test_delete_method(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) == 0)


        #project test class

class ProjectTestClass(TestCase):
    def setUp(self):
        self.project = Project(title = 'baboon', image='baboon.jpg', description="baboon",link="https://en.wikipedia.org/wiki/Tiger")

    def tearDown(self):
        Project.objects.all().delete()

    def test_instance(self):
         self.assertTrue(isinstance(self.project, Project))
    def test_save_method(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)>0)
    def test_delete_method(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.project.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)==0)


class ReviewTestclass(TestCase):
    def setUp(self):
        self.user = User(username='amos')
        self.user.save()
        self.project = Project(title='baboon', image='boboon.jpg', description="baboon", link="https://en.wikipedia.org/wiki/Tiger")
        self.project.save_project()

        self.new_review=Review(design="9",usability="9",conent="10",user=self.user,project=self.project)
        self.new_review.save_review()
    def tearDown(self):
        Review.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_review,Review))

    def test_save_comment(self):
        reviews = Review.objects.all()
        self.assertTrue(len(reviews)>0)

    def test_delete_comment(self):
        self.new_review.save_review()
        self.new_review.delete_review()
        reviews = Review.objects.all()
        self.assertTrue(len(reviews)==0)


