from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import render, redirect
from django.forms import ModelForm, Textarea, DateInput, TextInput, PasswordInput
from django.db import models

from .models import CustomUser, Articles, Telegram, Twitch, TV, VK, YouTube


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'description']
        widget = {
            'description': Textarea(attrs={'class': 'form-control'}),
            'username': TextInput(attrs={'class': 'form-control'}),
            'password1': PasswordInput(attrs={'class': 'form-control'}),
            'password2': PasswordInput(attrs={'class': 'form-control'}),
        }


    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': "введите ваш никнейм"})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': "введите пароль"})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': "введите пароль ещё раз"})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'rows': 5, 'placeholder': "введите описание вашего профиля"})








# Create your models here.


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['anons', 'title', 'full_text', 'date']

        widgets = {
            "anons": TextInput(attrs={'class': 'form-control', 'placeholder': 'Название ваших медиа'}),
            "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Ссылки для обсуждения условий рекламы'}),
            "full_text": Textarea(attrs={'class': 'form-control', 'placeholder': 'Расскажите о себе'}),
            "date": DateInput(attrs={'class': "form-control", 'type': 'date'}),
        }


class TelegramForm(ModelForm):
    class Meta:
        model = Telegram
        fields = ['anons', 'title', 'full_text', 'date']

        widgets = {
            "anons": TextInput(attrs={'class': 'form-control', 'placeholder': 'Название ваших медиа'}),
            "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Ссылки для обсуждения условий рекламы'}),
            "full_text": Textarea(attrs={'class': 'form-control', 'placeholder': 'Расскажите о себе'}),
            "date": DateInput(attrs={'class': "form-control", 'type': 'date'}),
        }


class TwitchForm(ModelForm):
    class Meta:
        model = Twitch
        fields = ['anons', 'title', 'full_text', 'date']

        widgets = {
            "anons": TextInput(attrs={'class': 'form-control', 'placeholder': 'Название ваших медиа'}),
            "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Ссылки для обсуждения условий рекламы'}),
            "full_text": Textarea(attrs={'class': 'form-control', 'placeholder': 'Расскажите о себе'}),
            "date": DateInput(attrs={'class': "form-control", 'type': 'date'}),
        }


class TvForm(ModelForm):
    class Meta:
        model = TV
        fields = ['anons', 'title', 'full_text', 'date']

        widgets = {
            "anons": TextInput(attrs={'class': 'form-control', 'placeholder': 'Название ваших медиа'}),
            "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Ссылки для обсуждения условий рекламы'}),
            "full_text": Textarea(attrs={'class': 'form-control', 'placeholder': 'Расскажите о себе'}),
            "date": DateInput(attrs={'class': "form-control", 'type': 'date'}),
        }


class VkForm(ModelForm):
    class Meta:
        model = VK
        fields = ['anons', 'title', 'full_text', 'date']

        widgets = {
            "anons": TextInput(attrs={'class': 'form-control', 'placeholder': 'Название ваших медиа'}),
            "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Ссылки для обсуждения условий рекламы'}),
            "full_text": Textarea(attrs={'class': 'form-control', 'placeholder': 'Расскажите о себе'}),
            "date": DateInput(attrs={'class': "form-control", 'type': 'date'}),
        }


class YouTubeForm(ModelForm):
    class Meta:
        model = YouTube
        fields = ['anons', 'title', 'full_text', 'date']

        widgets = {
            "anons": TextInput(attrs={'class': 'form-control', 'placeholder': 'Название ваших медиа'}),
            "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Ссылки для обсуждения условий рекламы'}),
            "full_text": Textarea(attrs={'class': 'form-control', 'placeholder': 'Расскажите о себе'}),
            "date": DateInput(attrs={'class': "form-control", 'type': 'date'}),
        }



