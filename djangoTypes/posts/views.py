from django.shortcuts import render
from .forms import section

# Create your views here.

listOfPosts = []

def post(request):
    Section = section()
    return render(request, 'post.html', {'form': Section})

def posts(request):
    Title = request.GET.get('Title')
    url = request.GET.get('URL')
    SMS = request.GET.get('SMS')
    Press = request.GET.get('Press')
    DontTouch = request.GET.get('DontTouch')
    post = [Title, url, SMS, Press, DontTouch]
    listOfPosts.append(post)
    return render(request, 'posts.html', {'form': [listOfPosts[i] for i in range(len(listOfPosts))]})