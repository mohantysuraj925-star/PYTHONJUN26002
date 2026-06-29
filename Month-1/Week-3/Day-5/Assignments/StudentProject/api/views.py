from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

def home_index(request):
    return JsonResponse({
        "status": "Running",
        "message": "StudentProject Day-5 Token Authentication System is active.",
        "endpoints": {"user_registration": "/api/register/", "user_login": "/api/login/", "user_profile": "/api/profile/"}
    })

@csrf_exempt
@api_view(['POST'])
def user_register(request):
    try:
        data = request.data
        if User.objects.filter(username=data.get('username')).exists():
            return JsonResponse({"error": "Profile already exists"}, status=400)
        user = User.objects.create_user(username=data.get('username'), password=data.get('password'))
        token, _ = Token.objects.get_or_create(user=user)
        return JsonResponse({"message": "User registered successfully", "token": token.key}, status=201)
    except Exception as e: return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
@api_view(['POST'])
def user_login(request):
    try:
        data = request.data
        user = authenticate(username=data.get('username'), password=data.get('password'))
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return JsonResponse({"message": "Login successful", "token": token.key}, status=200)
        return JsonResponse({"error": "Invalid credentials"}, status=401)
    except Exception as e: return JsonResponse({"error": str(e)}, status=400)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_profile(request):
    return JsonResponse({"username": request.user.username, "email": request.user.email}, status=200)
