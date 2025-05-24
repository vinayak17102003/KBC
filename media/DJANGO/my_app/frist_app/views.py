from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>hello vinayak <br> how are you broo <br> your are in home page</h1>")

def about(request):
    return HttpResponse("<h1> hell you are in about page</h1>")

def login(request):
    return HttpResponse("<h2> hey App login page pr aa gye ho</h2>")

