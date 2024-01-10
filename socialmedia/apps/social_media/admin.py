from django.contrib import admin

# Register your models here.
from .models import Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'publication_date',
        'author_name',
    )

    search_fields = (
        'title',
    )

    list_filter = (
        'publication_date',
        'author__username'
    )

    list_display_links = (
        'title',
    )

    def author_name(self, obj):
        return obj.author.username

    list_per_page = 5


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'author_name',
        'publication_date',
        'post'
    )

    search_fields = (
        'author__username',
    )

    list_filter = (
        'author__username',
        'publication_date'
    )

    list_display_links = (
        'author_name',
    )

    def author_name(self, obj):
        return obj.author.username

    list_per_page = 5
