from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from social_media.forms import PostForm
from social_media.models import Comment, Post


# Create your views here.
def index(request):
    posts = Post.objects.prefetch_related(
        'comment_set').order_by('publication_date')

    data = {}
    data['posts'] = posts
    data['title'] = "Posts List"

    return render(request, 'social_media/social_media.html', data)


def view_content_post(request, post_id):
    post = get_object_or_404(Post.objects.prefetch_related(
        'comment_set'), pk=post_id)

    data = {}
    data['post'] = post
    data['title'] = "Post Content"

    return render(request, 'social_media/post_content.html', data)


@login_required
def create_post(request):
    context = {}

    if request.method == 'POST':
        form = PostForm(request.POST or None)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()

    context['form'] = form
    context['title'] = "Create a new Post"

    return render(request, 'social_media/forms.html', context)
