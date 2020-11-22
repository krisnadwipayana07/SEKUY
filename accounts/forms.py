from django.db import models, transaction
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import *

class userLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Maaf Akun tidak tersedia')
            if not user.check_password(password):
                raise forms.ValidationError('Password yang anda masukan salah')
            if not user.is_active:
                raise forms.ValidationError('User tidak ada')
        
        return super(userLoginForm, self).clean(*args, **kwargs)

class MuridRegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        return user

class GuruRegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    phone=forms.CharField(required=True)
    destionation=forms.CharField(label="Materi Yang Diajar",required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        teacher.phone=self.cleaned_data.get('phone')
        teacher.destionation=self.cleaned_data.get('destionation')
        teacher.save()

        return teacher

# Fitur Views
class MateriForm(forms.ModelForm):
    class Meta:
        model = Materi
        fields = [
            'title',
            'slug',
            'body'
        ]
    
class VideoPembelajaranForm(forms.ModelForm):
    class Meta:
        model = VideoPembelajaran
        fields = [
            'materi',
            'link'
        ]
    
