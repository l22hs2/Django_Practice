from django.views.generic import ListView, DetailView
from django.shortcuts import render
from blog.models import Post

class PostList(ListView):
    model = Post
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post
    ordering = '-pk'


# def index(request):
#     posts = Post.objects.all().order_by('-pk') # select * from post, -pk -> 내림차순
#     return render(request, 'blog/index.html',
#         {
#             'posts_':posts,
#         }
#     )

# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk) # select pk from post
#     return render(request, 'blog/single_post_page.html',
#         {
#             'post_':post
#         }
#     )