from django.db import models
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username
    
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone= models.CharField(max_length=50)
    destionation = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username
    

# Create your models here.
class Materi(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.id)

class VideoPembelajaran(models.Model):
    materi = models.CharField(max_length=40)
    link = EmbedVideoField()
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return "{}".format(self.id)

    