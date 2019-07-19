# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Feed(models.Model):
    name = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    errors = models.IntegerField()