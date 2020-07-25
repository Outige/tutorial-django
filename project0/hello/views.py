from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")

def tieg(request):
    return HttpResponse("Hello, Tieg")

def greet(request, name):
    # return HttpResponse(f"<h1>Hello, {name}</h1>")
    return render(request, "html/greet.html", {
        "name": name
    })

def html(request, name):
    return render(request, f"html/{name}.html")

def welcome(request):
    name = "welcome"
    return render(request, f'html/{name}.html')
