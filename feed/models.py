# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Feed(models.Model):
    name = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    site_url = models.CharField(max_length=500, null=True)
    user_id = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    last_check = models.DateTimeField(null=True)
    errors = models.IntegerField()

    def get_site_url(self):
        return self.site_url