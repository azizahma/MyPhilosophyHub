from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse('Welcome to Myphilosophyhub, you are my number 1 view')

