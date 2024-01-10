from django.conf import settings
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=255)
    publication_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    content = models.TextField(max_length=255)
    publication_date = models.DateField(auto_now_add=True)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.author.username}"
