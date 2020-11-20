from django.db import models
from embed_video.fields import EmbedVideoField
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

    