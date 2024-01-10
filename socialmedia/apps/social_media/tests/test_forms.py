from datetime import date, datetime, timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from social_media.forms import PostForm
from social_media.models import *

now = date.today()


User = get_user_model()


class TestForms(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test",
            email="test@example.com",
            password="123",
            first_name="test",
            last_name="test",
        )

    def test_post_form_is_valid(self):
        form = PostForm(
            data={
                "title": "test",
                "content": "test",
                "publication_date": str(now.strftime("%Y-%m-%d")),
                "author": self.user
            }
        )

        self.assertTrue(form.is_valid())

    def test_post_form_is_not_valid(self):
        form = PostForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_post_form_title_empty(self):
        form = PostForm(
            data={
                "title": "",
                "content": "test",
                "publication_date": str(now.strftime("%Y-%m-%d")),
                "author": self.user
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_post_form_content_empty(self):
        form = PostForm(
            data={
                "title": "test",
                "content": "",
                "publication_date": str(now.strftime("%Y-%m-%d")),
                "author": self.user
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_post_form_author_empty(self):
        form = PostForm(
            data={
                "title": "test",
                "content": "test",
                "publication_date": str(now.strftime("%Y-%m-%d")),
                "author": ""
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
