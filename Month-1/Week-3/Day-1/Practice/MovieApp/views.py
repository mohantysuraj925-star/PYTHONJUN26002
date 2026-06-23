from django.shortcuts import render

def home(request):
    return render(request, "home/index.html")

def add(request):
    return render(request, "add/index.html")
