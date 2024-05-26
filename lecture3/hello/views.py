from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "hello/index.html")


def rian(request):
    return HttpResponse("Olá Rian!")


def david(request):
    return HttpResponse("Olá, David!")


def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
