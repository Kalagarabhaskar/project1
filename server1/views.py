from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def jango(request):
    return HttpResponse('<h1><marquee>hloo guys</marquee></h1>')