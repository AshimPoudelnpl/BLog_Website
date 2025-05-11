from django.shortcuts import render
from django.http import HttpResponse as httpResponse
from django.contrib import messages

# Create your views here.
def blogHome(request):
    return render(request, 'blog/blogHome.html')
def blogPost(request, slug): 
    # Logic for blogPost can be added here
    return render(request, 'blog/blogPost.html', {'slug': slug})    

