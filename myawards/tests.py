from django.test import TestCase
from .models import Project, Profile, Review

# Create your tests here.
class ProjectTestClass(TestCase):
    def setUp(self):
        self.git= Project(title = 'git',landing_page = 'photos/Delani_Studio.jpg',description ='qwerty',live_link ='https://github.com ',design ='6',usability='4',content = '5', overall = '3', posted= '2019-08-05 16:05:47.026576+03',user = '1')

    def test_instance(self):
        self.assertTrue(isinstance(self.git,Project))

    def test_save_method(self):
        self.git.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)>0)

    def test_delete_method(self):
        self.git.save_project()
        projects = Project.objects.all()
        self.assertFalse(len(projects) == 0)

    def test_get_project(self):
        projects = Project.objects.all()
        self.assertFalse(len(projects)>0)

    def tearDown(self):
        Project.objects.all().delete()
        Review.objects.all().delete()
        Profile.objects.all().delete()

    
class ProfileTestClass(TestCase):
    def setUp(self):
        self.john = Profile(user = '1', profile_photo = '', bio = 'coding',contact ='072212')

    def test_instance(self):
        self.assertTrue(isinstance(self.john, Profile))

    def test_save_method(self):
        self.john.save_profile()
        profiles = Profile.objects.all()
        self.assertFalse(len(profiles) > 0)

    def test_delete_method(self):
        self.john.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)