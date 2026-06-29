import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Student

def home_index(request):
    return JsonResponse({
        "status": "Running",
        "message": "StudentProject Token Authentication System is fully active on root page.",
        "endpoints": {
            "user_registration": "/api/register/",
            "user_login": "/api/login/",
            "user_profile": "/api/profile/",
            "students_pagination_list": "/api/students/"
        }
    })

@csrf_exempt
def student_list_or_create(request):
    if request.method == 'GET':
        students_query = Student.objects.all().order_by('id')
        total_count = students_query.count()
        page_num = request.GET.get('page', 1)
        paginator = Paginator(students_query, 5)

        try:
            page_obj = paginator.get_page(page_num)
        except (PageNotAnInteger, EmptyPage):
            page_obj = paginator.get_page(1)

        results = []
        for student in page_obj.object_list:
            results.append({
                "id": student.id,
                "name": student.name,
                "email": student.email,
                "phone": student.phone,
                "course": student.course
            })

        host = request.build_absolute_uri('/')
        next_page = f"{host}?page={page_obj.next_page_number()}" if page_obj.has_next() else None
        previous_page = f"{host}?page={page_obj.previous_page_number()}" if page_obj.has_previous() else None

        return JsonResponse({
            "count": total_count,
            "next": next_page,
            "previous": previous_page,
            "results": results
        }, safe=False)

    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            student = Student.objects.create(
                name=data.get('name'),
                email=data.get('email'),
                phone=data.get('phone'),
                course=data.get('course')
            )
            return JsonResponse({
                "id": student.id,
                "name": student.name,
                "email": student.email,
                "phone": student.phone,
                "course": student.course
            }, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return JsonResponse({"error": "Student not found"}, status=404)

    if request.method == 'GET':
        return JsonResponse({
            "id": student.id,
            "name": student.name,
            "email": student.email,
            "phone": student.phone,
            "course": student.course
        })

    elif request.method == 'PUT':
        try:
            data = json.loads(request.body)
            student.name = data.get('name', student.name)
            student.email = data.get('email', student.email)
            student.phone = data.get('phone', student.phone)
            student.course = data.get('course', student.course)
            student.save()
            return JsonResponse({
                "id": student.id,
                "name": student.name,
                "email": student.email,
                "phone": student.phone,
                "course": student.course
            })
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    elif request.method == 'DELETE':
        student.delete()
        return JsonResponse({"message": "Student deleted successfully"}, status=200)

# --- DAY-5 ENDPOINTS ---

@csrf_exempt
@api_view(['POST'])
def user_register(request):
    try:
        data = request.data
        username = data.get('username')
        password = data.get('password')
        email = data.get('email', '')

        if not username or not password:
            return JsonResponse({"error": "Username and password are required"}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already exists"}, status=400)

        user = User.objects.create_user(username=username, password=password, email=email)
        token, _ = Token.objects.get_or_create(user=user)

        return JsonResponse({
            "message": "User registered successfully",
            "username": user.username,
            "token": token.key
        }, status=201)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
@api_view(['POST'])
def user_login(request):
    try:
        data = request.data
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return JsonResponse({
                "message": "Login successful",
                "username": user.username,
                "token": token.key
            }, status=200)
        else:
            return JsonResponse({"error": "Invalid credentials"}, status=401)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_profile(request):
    return JsonResponse({
        "username": request.user.username,
        "email": request.user.email,
        "date_joined": request.user.date_joined
    }, status=200)
