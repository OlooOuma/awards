from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=150)
    landing_page = models.ImageField(upload_to='photos')
    description = models.CharField(max_length=255)
    live_link = models.URLField(max_length=250)
    design = models.IntegerField(blank=True,default=0)
    usability = models.IntegerField(blank=True,default=0)
    content = models.IntegerField(blank=True,default=0)
    overall = models.IntegerField(blank=True,default=0)
    posted  = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        ordering = ('title',)

    @classmethod
    def search_project(cls, search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects

    def save_project(self):
        self.save()


    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='profiles/')
    bio = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)

    class Meta:
        ordering = ('user',)

    
    
    def save_profile(self):
        self.save()


class Review(models.Model):
    CHOICES = (1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6),(7, 7),(8, 8),(9, 9),(10, 10)

    title= models.CharField(max_length=60)
    design = models.IntegerField(choices=CHOICES,default=0)
    usability= models.IntegerField(choices=CHOICES,default=0)
    content =  models.IntegerField(choices=CHOICES,default=0)
    overall_score = models.IntegerField(blank=True,default=0)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)     