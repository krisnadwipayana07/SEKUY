from django.db import models
from django import forms
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

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
                raise forms.ValidationError('User tidak active')
        
        return super(userLoginForm, self).clean(*args, **kwargs)



class UserRegisterForm(forms.ModelForm):
    first_name = forms.CharField (label='Nama Depan')
    last_name = forms.CharField (label='Nama Belakang')
    email = forms.EmailField (label='Email Address')
    phonenumber = forms.CharField(max_length=100,min_length=5)
    DateOfBirth = forms.DateField ()
    password = forms.CharField (widget=forms.PasswordInput)
    password2 = forms.CharField (widget=forms.PasswordInput, label="Password Confirmation")

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'phonenumber',
            'DateOfBirth',
            'password',
            'password2'
        ]
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password == password2:
            raise forms.ValidationError("Kata sandi harus sama")
        return password

# class videoLearning(forms.Form):
#     videoName = forms.CharField(label="Nama Video Materi")
#     videoLink = forms.URLField(label="Video Learning", required=False)

#     class Meta:
    
    
#     def clean(self,*args, **kwargs):
#         videoName = self.cleaned_data.get('videoName')


