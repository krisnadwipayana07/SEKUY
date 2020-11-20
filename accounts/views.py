from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model,login,logout

from .forms import *
from .models import *

def login_view(request):
    next = request.GET.get('next')
    form = userLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')
    context = {
        'form': form,
    }
    return render(request,"login.html", context)

def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')
    context = {
        'form': form,
    }
    return render(request,"signup.html", context)

def logout_view(request):
    logout(request)
    return redirect('/')

def listMateri(request):
    semua_materi = Materi.objects.all().order_by('date')

    context = {
        'page_title':'Instagram',
        'semua_materi':semua_materi,
    }

    return render(request,'Materi/materi.html',context)

def createMateri(request):
    materi_form = MateriForm(request.POST or None)

    if request.method == 'POST':
        if materi_form.is_valid():
            materi_form.save()
        
        return redirect('materi')

    context = {
        "page_title" : "Tambah Akun",
        "materi_form" : materi_form,
    }

    return render(request,'Materi/tambahmateri.html',context)

def deleteMateri(request,delete_id):
    Materi.objects.filter(id=delete_id).delete()
    return redirect('materi')

def updateMateri(request,update_id):
    materi_update = Materi.objects.get(id=update_id)

    data = {
        'title' : materi_update.nama_depan,
        'slug'  : materi_update.nama_belakang,
        'body'  : materi_update.username,
    }

    materi_form = MateriForm(request.POST or None, initial=data, instance=akun_update)

    if request.method == 'POST':
        if materi_form.is_valid():
            materi_form.save()
        
        return redirect('materi')

    context = {
        "page_title" : "Update Akun",
        "materi_form" : materi_form,
    }

    return render(request,'Materi/tambahmateri.html',context)

