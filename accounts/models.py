from django.db import models

# Create your models here.
class isiMateri(models.Manager):
    def buatMateri(self, judul, comment, *args , **kwargs):
        materi = self.create(judul=judul,comment=comment)
        return materi

class Materi(models.Model):
    judul = models.CharField(max_length=30)
    comment = models.CharField(max_length=3000)

    if judul and command :
        objects = isiMateri()

materi = Materi.objects.buatMateri("Judul Materi","Isi Materi")