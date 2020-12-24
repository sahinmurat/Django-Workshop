from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return HttpResponse('That is a message that i have own created on views.py!')

def about_view(request):
    return HttpResponse('about')