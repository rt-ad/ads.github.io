from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import TextField

from django.urls import reverse_lazy


class CustomUser(AbstractUser):
    description = TextField(verbose_name='Описание', blank=True)
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    def get_absolute_url(self):
        return reverse_lazy('username', kwargs={"username_id": self.pk})



    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'



class Articles(models.Model):
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='custom_user', default=3)
    anons = models.CharField('user', max_length=250)
    title = models.CharField('Название', max_length=50)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Telegram(models.Model):
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='telegram_user', default=3)
    anons = models.CharField('user', max_length=250)
    title = models.CharField('Название', max_length=50)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'TG'

class Twitch(models.Model):
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='twitch_user', default=3)
    anons = models.CharField('user', max_length=250)
    title = models.CharField('Название', max_length=50)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'TW'

class VK(models.Model):
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='VK_user', default=3)
    anons = models.CharField('user', max_length=250)
    title = models.CharField('Название', max_length=50)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'VK'

class YouTube(models.Model):
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='youtube_user', default=3)
    anons = models.CharField('user', max_length=250)
    title = models.CharField('Название', max_length=50)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'YT'


class TV(models.Model):
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tv_user', default=3)
    anons = models.CharField('user', max_length=250)
    title = models.CharField('Название', max_length=50)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'TV'
