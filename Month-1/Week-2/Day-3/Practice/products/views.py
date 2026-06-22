from django.shortcuts import render
from django.http import Http404

ProductsList = [
    {'id': 1, 'name': "IPhone", 'img': "https://images.unsplash.com/photo-1726574686436-5ef90358e032?fm=jpg&q=60&w=3000&auto=format&fit=crop", 'desc': 'Apple iPhone with premium design and advanced camera system.'},
    {'id': 2, 'name': 'Samsung', 'img': "https://images.samsung.com/is/image/samsung/p6pim/in/s2602/gallery/in-galaxy-s26-ultra-s948-sm-s948bzvbins-thumb-550793679", 'desc': 'Samsung flagship phone featuring a built-in S-Pen and pro-grade lens.'},
    {'id': 3, 'name': 'VIVO', 'img': 'https://images.unsplash.com/photo-1755318535396-cdb062dc60bd?fm=jpg&q=60&w=3000&auto=format&fit=crop', 'desc': 'Vivo premium smartphone with large cinematic rear camera layout.'},
    {'id': 4, 'name': 'Realme', 'img': 'https://images.unsplash.com/photo-1609081219090-a6d81d3085bf?w=400', 'desc': 'Realme mid-range smartphone offering ultra-fast charging and stylish design.'},
    {'id': 5, 'name': 'OnePlus', 'img': 'https://images.unsplash.com/photo-1620283085439-39620a1e21c4?w=400', 'desc': 'OnePlus flagship device with iconic round camera module and smooth display.'},
    {'id': 6, 'name': 'Xiaomi', 'img': 'https://images.unsplash.com/photo-1605647540924-852290f6b0d5?w=400', 'desc': 'Xiaomi smartphone packed with a high-resolution sensor and sleek aesthetics.'},
    {'id': 7, 'name': 'Google Pixel', 'img': 'https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=400', 'desc': 'Google Pixel running stock Android with a sleek signature horizontal camera bar.'},
    {'id': 8, 'name': 'Motorola', 'img': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400', 'desc': 'Motorola stylish modern device featuring an ultra-slim glass back finish.'}
]

def home(request):
    return render(request, 'products/index.html', {'ProductsList': ProductsList})

def product_detail(request, product_id):
    product = next((p for p in ProductsList if p['id'] == product_id), None)
    if product is None:
        raise Http404("Product not found")
    return render(request, 'products/detail.html', {'product': product, 'index': product_id})

def contact(request):
    return render(request, 'products/contact.html')

def student(request):
    student_data = {
        "name": "Rahul",
        "age": 21,
        "course": "Python Full Stack"
    }
    return render(request, 'products/student.html', {'student': student_data})

def about_company(request):
    company_data = {
        "name": "Qlith Innovation Pvt Ltd",
        "location": "Bhubaneswar",
        "services": ["Web Development", "Mobile App Development", "UI/UX Design"]
    }
    return render(request, 'products/about_company.html', {'company': company_data})

def faq(request):
    faqs_data = [
        {"question": "What is Django?", "answer": "A Python Web Framework"},
        {"question": "What is URL Routing?", "answer": "Mapping URLs to Views"},
        {"question": "What is a Template?", "answer": "HTML file rendered by Django"}
    ]
    return render(request, 'products/faq.html', {'faqs': faqs_data})

def team(request):
    team_data = [
        {"name": "John", "role": "Developer"},
        {"name": "Emma", "role": "Designer"},
        {"name": "Alex", "role": "Tester"}
    ]
    return render(request, 'products/team.html', {'team': team_data})
