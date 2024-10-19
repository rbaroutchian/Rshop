from django.shortcuts import render, get_object_or_404
from .models import single_blog

# Create your views here.

def post(request):
    all_post = single_blog.objects.all()
    return render(request, 'post.html', {'posts': all_post})
def detail(request, sb_slug):
    post = get_object_or_404(single_blog, sb_slug=sb_slug)
    return render(request, 'single_blog.html',
                  {'posts': post})

