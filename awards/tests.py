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

