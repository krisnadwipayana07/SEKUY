from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import *
# Register your models here.
admin.site.register(Materi)

class VideoPembelajaranAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(VideoPembelajaran, VideoPembelajaranAdmin)