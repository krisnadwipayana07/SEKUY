from django.db import models

# Create your models here.
class Materi(models.Model):
    # first_name = models.CharField("Judul Materi : ",max_length=30)
    comment = models.CharField("isi Materi",max_length=3000)

