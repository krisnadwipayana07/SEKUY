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
    name = models.CharField(max_length=40)
    link = EmbedVideoField()  # same like models.URLField()