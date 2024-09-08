from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):  # Модель категорий товаров
    name = models.CharField(max_length=30)  # Имя категории
    slug = models.SlugField(max_length=30, unique=True)  # Человеко понятный url

    def __str__(self):
        return self.name

class PostModel(models.Model):
    date_post = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    content = models.TextField()
    header_post = models.CharField(max_length=64)
    slug = models.SlugField(max_length=30, unique=True, verbose_name='URL товара')



class PostImg(models.Model):
    post = models.ForeignKey(PostModel, related_name='postimg', on_delete=models.CASCADE)
    post_img = models.ImageField(upload_to='img/')