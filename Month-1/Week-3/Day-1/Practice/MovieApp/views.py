from django.shortcuts import render, redirect

def index(request):
    return redirect('add')

def add(request):
    # Agar aapka template 'add.html' ya 'index.html' hai, toh usko render karo
    return render(request, 'MovieApp/add.html') 
