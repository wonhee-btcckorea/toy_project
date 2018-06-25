# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(max_length=30, primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)

class RedisUser(models.Model):
    name = models.TextField()