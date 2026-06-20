from django.shortcuts import render

def home(request):
    ProductsList = [
        {'id': 1, 'name': "IPhone", 'img': "https://images.unsplash.com/photo-1726574686436-5ef90358e032?fm=jpg&q=60&w=3000&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aXBob25lJTIwMTN8ZW58MHx8MHx8fDA%3D"},
        {'id': 2, 'name': 'Samsung', 'img': "https://images.samsung.com/is/image/samsung/p6pim/in/s2602/gallery/in-galaxy-s26-ultra-s948-sm-s948bzvbins-thumb-550793679"},
        {'id': 3, 'name': 'VIVO', 'img': 'https://images.unsplash.com/photo-1755318535396-cdb062dc60bd?fm=jpg&q=60&w=3000&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8dml2byUyMHNtYXJ0cGhvbmV8ZW58MHx8MHx8fDA%3D'}
    ]
    return render(request, 'products/index.html', {'ProductsList': ProductsList})
