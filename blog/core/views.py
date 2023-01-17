from django.shortcuts import render, get_object_or_404
from core.models import Blog


def listing(request):
    context = {
        'blogs':Blog.objects.all()
    }
    return render(request, "listing.html", context)

def view_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    context = {
        'blog' : blog
    }
    return render(request, 'view_blog.html', context)