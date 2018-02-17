from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    """Wyświetlenie listy postów."""
    posts = Post.published.all()
    context = {'posts': posts}
    return render(request, 'blog/post/list.html',
                            context)

def post_detail(request, year, month, day, post):
    """Wyświetlenie konkretnego posta."""
    post = get_object_or_404(Post, slug=post, status='published',
                                              publish__year=year,
                                              publish__month=month,
                                              publish__day=day)
    return render(request,
                  'blog/post/detail.html', 
                  {'post': post})
#eksdeedededed
