from django import forms
from django.contrib.auth.models import User
from account.models import Profile, Request


class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), label="Пароль")

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')


class UserFormForEdit(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo', 'sex', 'city', 'passport', 'phone', 'social_status')


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('id', 'offer',)
        #exclude =('profile',) # исключает показ поля на странице


