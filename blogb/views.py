from django.shortcuts import render, get_object_or_404
from . models import Post

# Create your views here.


def home(request):

    all_posts = Post.newmanager.all()


    return render(request, 'index.html', {
        'posts' : all_posts,
    })

def single_post(request, post):

    post = get_object_or_404(Post, slug=post, status= 'published')

    return render(request, 'single.html', {
        'post': post
    })
