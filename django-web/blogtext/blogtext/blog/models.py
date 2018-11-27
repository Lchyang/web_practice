# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.six import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=100)
    #文章标题
    body = models.TextField()
    #文章内容
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    #这两个表示文章创建的时间和文章修改的时间用datetimefield

    excerpt = models.CharField(max_length=200,blank=True)
    #文章摘要，指定charField的blank=True 存入内容可以为空
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag,blank=True)
    #Foreigkey 一对多关系 manytomany多对多关系

    author = models.ForeignKey(User)
    #文章作者

    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    class Meta:
        ordering = ['-created_time']