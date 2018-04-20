# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
class Informations(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name="Titre")
    slug = models.SlugField(max_length=100, null=True, blank=True, verbose_name="Slug")
    description = models.TextField()
    picture = models.ImageField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now(), auto_now=True, auto_now_add=True)
    update_at = models.DateTimeField(default=timezone.now(), auto_now=True, auto_now_add=True)