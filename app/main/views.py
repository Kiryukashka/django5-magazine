from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  context = {
    'title': 'Home',
    'content': 'Welcome to the home page.',
    'list': ['first', 'second'],
    'dict': {'first': 1},
    'is_authenticated': True
  }
  
  return render(request, 'main/index.html', context)

def about(request):
  return HttpResponse("Hello, world. You're at the main about page.")