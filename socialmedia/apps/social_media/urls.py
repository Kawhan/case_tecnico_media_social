from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('<int:post_id>/post', view_content_post, name="view_content_post"),
    path('forms', create_post, name="create_post")
]
