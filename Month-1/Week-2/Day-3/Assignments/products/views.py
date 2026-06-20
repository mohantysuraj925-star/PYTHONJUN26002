from django.shortcuts import render

def home(request):
    ProductsList = [
        {'id': 1, 'name': "IPhone", 'img': "https://images.unsplash.com/photo-1726574686436-5ef90358e032?fm=jpg&q=60&w=3000&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aXBob25lJTIwMTN8ZW58MHx8MHx8fDA%3D"},
        {'id': 2, 'name': 'Samsung', 'img': "https://images.samsung.com/is/image/samsung/p6pim/in/s2602/gallery/in-galaxy-s26-ultra-s948-sm-s948bzvbins-thumb-550793679"},
        {'id': 3, 'name': 'VIVO', 'img': 'https://images.unsplash.com/photo-1755318535396-cdb062dc60bd?fm=jpg&q=60&w=3000&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8dml2byUyMHNtYXJ0cGhvbmV8ZW58MHx8MHx8fDA%3D'},
        {'id': 4, 'name': 'Realme', 'img': 'https://images.unsplash.com/photo-1616348436168-de43ad0db179?w=300'},
        {'id': 5, 'name': 'OnePlus', 'img': 'https://images.unsplash.com/photo-1616348436168-de43ad0db179?w=300'},
        {'id': 6, 'name': 'Xiaomi', 'img': 'https://images.unsplash.com/photo-1616348436168-de43ad0db179?w=300'},
        {'id': 7, 'name': 'Google Pixel', 'img': 'https://images.unsplash.com/photo-1616348436168-de43ad0db179?w=300'},
        {'id': 8, 'name': 'Motorola', 'img': 'https://images.unsplash.com/photo-1616348436168-de43ad0db179?w=300'}
    ]
    return render(request, 'products/index.html', {'ProductsList': ProductsList})

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
