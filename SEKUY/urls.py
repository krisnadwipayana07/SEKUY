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
    path('accounts/login/', login_view),
    path('accounts/register/', register_view, name="signup"),
    path('accounts/logout/', login_view),

    # Materi Link
    url(r'sosmed/delete/(?P<delete_id>[0-9]+)$', deleteMateri, name='hapusMateri'),
    url(r'sosmed/update/(?P<update_id>[0-9]+)$', updateMateri, name='updateMateri'),
    path('materi/tambahmateri/', createMateri, name="createMateri"),
    path('materi/', listMateri, name="materi"),
    
]
