from django.shortcuts import render, redirect

def index(request):
    return redirect('add_movie')

def add_movie(request):
    # Aapka jo dynamic form aur premium layout ka code tha, wo iske neeche chalega
