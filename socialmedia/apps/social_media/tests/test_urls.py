from django.test import SimpleTestCase
from django.urls import resolve, reverse
from social_media.views import *


class TestUrls(SimpleTestCase):
    # Index
    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_view_job(self):
        url = reverse('view_content_post', args=[1])
        self.assertEquals(resolve(url).func, view_content_post)

    def test_create_job(self):
        url = reverse('create_post')
        self.assertEquals(resolve(url).func, create_post)
