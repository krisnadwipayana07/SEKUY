from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model,login,logout

from .forms import userLoginForm,UserRegisterForm,MateriForm
from .models import Materi

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

def AddMateri(request):
    materi_form = MateriForm(request.POST or None)

    if request.method == 'POST':
        if materi_form.is_valid():
            materi_form.save()
        
        return redirect('materi')

    context = {
        "page_title" : "Tambah Materi",
        "materi_form" : materi_form,
    }

    return render(request,'Materi/tambahmateri.html',context)

def ListMateri(request):
    semua_materi = Materi.objects.all()

    context = {
        'page_title':'Materi',
        'semua_materi':semua_materi,
    }

    return render(request,'Materi/materi.html',context)

def hapusMateri(request, hapus_id):
    Materi.objects.filter(id=hapus_id).delete()
    return redirect('materi')

def updateMateri(request,update_id):
    materi_update = Materi.objects.get(id=update_id)

    data = {
        'title'     : materi_update.title,
        'slug'      : materi_update.slug,
        'body'      : materi_update.body,
    }

    materi_form = MateriForm(request.POST or None, initial=data, instance=materi_update)

    if request.method == 'POST':
        if materi_form.is_valid():
            materi_form.save()
        
        return redirect('materi')

    context = {
        "page_title" : "Update Materi",
        "materi_form" : materi_form,
    }

    return render(request,'materi/tambahmateri.html',context)

def videoPembelajaran(request):
    context = {
        'image_url' : "https://www.youtube.com/watch?v=YXhSY13juUU&list=PLOOe-m1n0C7rSQgETlfdKCxHKgWrPHz6y&index=4&t=915s"
    }
    return render(request,'videoPembelajaran.html', context)