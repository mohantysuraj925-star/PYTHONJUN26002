from django.shortcuts import render, redirect

def index(request):
    return redirect('add')

def add(request):
    # Aapka asli premium layout 'add/index.html' ke andar hai
    return render(request, 'add/index.html')
