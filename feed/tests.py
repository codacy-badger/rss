# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from models import Feed

# Create your tests here.
class FeedTest(TestCase):

    # name = models.CharField(max_length=500)
    # url = models.CharField(max_length=500)
    # site_url = models.CharField(max_length=500, null=True)
    # user_id = models.IntegerField(null=True)
    # created_at = models.DateTimeField(auto_now_add=True, editable=False)
    # last_check = models.DateTimeField(null=True)
    # errors = models.IntegerField()
    def setUp(self):
        Feed.objects.create(
            name='Test Feed',
            url='https://wwww.google.com/rss',
            site_url='https://wwww.google.com/',
            user_id=1,
            errors=0)

    def test_get_feeds(self):
        feed = Feed.objects.get(name='Test Feed')

        self.assertEqual(
            feed.get_site_url(), "https://wwww.google.com/")

