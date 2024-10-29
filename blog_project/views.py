from django.shortcuts import render
from posts.models import Post
from categories.models import Category

def home(request):
    query = request.GET.get('search', '')
    if query:
        query = str.strip(query)
        data = Post.objects.filter(title__icontains=query) | Post.objects.filter(category__name__icontains=query)
    else:
        data = Post.objects.all()

    return render(request, 'home.html', {'data': data})