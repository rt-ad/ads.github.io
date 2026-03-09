from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, AnonymousUser, AbstractUser
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import RegisterForm, ArticlesForm, TelegramForm, TvForm, TwitchForm, VkForm, YouTubeForm
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db import models
from django.forms import ModelForm

from .models import Articles, CustomUser, Twitch, Telegram, TV, VK, YouTube


def index(request):
    data = {
        'title': 'Главная'
    }
    return render(request, 'main/index.html', {})


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')

def ads(request):
    return render(request, 'main/ads/ads.html')


def vk(request):
    return render(request, 'main/ads/vk.html')

def youtube(request):
    return render(request, 'main/ads/youtube.html')


def telegram(request):
    return render(request, 'main/ads/telegram.html')

def twitch(request):
    return render(request, 'main/ads/twitch.html')


@login_required
def profile(request):
    return render(request, 'profile/profile.html')

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("login")
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



def news_home(request):
    news = Articles.objects.order_by('date')
    users = CustomUser.objects.all()
    return render(request, 'news/news_home.html', {'news': news})
    return render(request, 'news/news_home.html', {'users': users})

def print_telegram(request):
    tg = Telegram.objects.order_by('date')
    users = CustomUser.objects.all()
    return render(request, 'main/print_ads/telegram.html', {'tg': tg})
    return render(request, 'news/news_home.html', {'users': users})

def print_vk(request):
    vkk = VK.objects.order_by('date')
    users = CustomUser.objects.all()
    return render(request, 'main/print_ads/vk.html', {'vkk': vkk})
    return render(request, 'news/news_home.html', {'users': users})

def print_twitch(request):
    twitchh = Twitch.objects.order_by('date')
    users = CustomUser.objects.all()
    return render(request, 'main/print_ads/twitch.html', {'twitchh': twitchh})
    return render(request, 'news/news_home.html', {'users': users})

def print_tv(request):
    telev = TV.objects.order_by('date')
    users = CustomUser.objects.all()
    return render(request, 'main/print_ads/tv.html', {'telev': telev})
    return render(request, 'news/news_home.html', {'users': users})

def print_youtube(request):
    yt = YouTube.objects.order_by('date')
    users = CustomUser.objects.all()
    return render(request, 'main/print_ads/youtube.html', {'yt': yt})
    return render(request, 'news/news_home.html', {'users': users})

@login_required
def create(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        reverse_lazy("index")
        if form.is_valid():
            CustomUser.user = request.user
            form.save()



    form = ArticlesForm()

    data = {
        'form': form

    }



    return render(request, 'news/create.html', data)

@login_required
def telegram(request):
    if request.method == 'POST':
        form = TelegramForm(request.POST)
        reverse_lazy("index")
        if form.is_valid():
            CustomUser.user = request.user
            form.save()



    form = TelegramForm()

    data = {
        'form': form

    }



    return render(request, 'main/ads/telegram.html', data)

@login_required
def tv(request):
    if request.method == 'POST':
        form = TvForm(request.POST)
        reverse_lazy("index")
        if form.is_valid():
            CustomUser.user = request.user
            form.save()



    form = TvForm()

    data = {
        'form': form

    }



    return render(request, 'main/ads/tv.html', data)


@login_required
def twitch(request):
    if request.method == 'POST':
        form = TwitchForm(request.POST)
        reverse_lazy("index")
        if form.is_valid():
            CustomUser.user = request.user
            form.save()



    form = TwitchForm()

    data = {
        'form': form

    }



    return render(request, 'main/ads/twitch.html', data)

@login_required
def vk(request):
    if request.method == 'POST':
        form = VkForm(request.POST)
        reverse_lazy("index")
        if form.is_valid():
            CustomUser.user = request.user
            form.save()



    form = VkForm()

    data = {
        'form': form

    }



    return render(request, 'main/ads/vk.html', data)

@login_required
def youtube(request):
    if request.method == 'POST':
        form = YouTubeForm(request.POST)
        reverse_lazy("index")
        if form.is_valid():
            CustomUser.user = request.user
            form.save()



    form = YouTubeForm()

    data = {
        'form': form

    }



    return render(request, 'main/ads/youtube.html', data)