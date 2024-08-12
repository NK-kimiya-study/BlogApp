from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    profile = models.TextField(blank=True, null=True)

class Post(models.Model):
    title = models.CharField(verbose_name='タイトル',max_length=50)
    text = models.TextField(
        verbose_name='本文',
    )
    image1 = models.ImageField(
        verbose_name='イメージ1',
        upload_to='photos',
        blank=True,
        null=True
    )
    user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
    )
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
    )
    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(verbose_name='カテゴリー',max_length=30)
    def __str__(self):
        return self.title

class Group(models.Model):
    title = models.CharField(verbose_name='グループ名',max_length=30)
    share = models.CharField(verbose_name='招待リンク・グループID',max_length=100)
    text = models.TextField(
        verbose_name='グループ概要',
    )
    user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        verbose_name='サービスカテゴリー',
        on_delete=models.CASCADE
    )
    posted_at = models.DateTimeField(
        verbose_name='作成日時',
        auto_now_add=True
    )
