# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    account = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.account

class File(models.Model):
    code = models.CharField(max_length=1000)
    hashHex = models.CharField(max_length=1000 ,default="")
    file = models.FileField(upload_to="fileServer/static/files")

    def __str__(self):
        return self.code

