from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    blogs = Blog.objects.order_by('-created_datetime')
    return render(request, 'blogs/index.html', { 'blogs': blogs })

def detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blogs/detail.html', {'blog': blog})

def new(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    else:
        form = BlogForm
    return render(request, 'blogs/new.html', {'form': form})

@require_POST
def delete(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.delete()
    return redirect('blogs:index')

def edit(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blogs:detail', blog_id=blog_id)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blogs/edit.html', {'form': form, 'blog': blog})