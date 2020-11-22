"""SEKUY URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from .views import *

from accounts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name="index"),
    path('accounts/login/', LoginView, name="login"),
    path('accounts/register-murid/', MuridRegisterView.as_view(), name="register-murid"),
    path('accounts/register-guru/', GuruRegisterView.as_view(), name="register-guru"),
    path('accounts/logout/', logout_view, name="logout"),

    # Materi Link
    url(r'materi/delete/(?P<delete_id>[0-9]+)$', deleteMateri, name='hapusMateri'),
    url(r'materi/update/(?P<update_id>[0-9]+)$', updateMateri, name='updateMateri'),
    path('materi/tambahmateri/', createMateri, name="createMateri"),
    path('materi/', listMateri, name="materi"),
    
    # Video Pembelajaran Link
    url(r'video-pembelajaran/delete/(?P<delete_id>[0-9]+)$', deleteVideo, name='hapusVideo'),
    url(r'video-pembelajaran/update/(?P<update_id>[0-9]+)$', updateVideo, name='updateVideo'),
    path('video-pembelajaran/tambahvideo/', tambahVideo, name="tambahVideo"),
    path('video-pembelajaran/', listVideoPembelajaran, name="videopembelajaran"),
    
]
