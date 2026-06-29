from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

def home_index(request):
    """
    Root endpoint serving basic system verification.
    """
    return JsonResponse({
        "status": "Active",
        "service": "Token Authentication System"
    })

@csrf_exempt
@api_view(['POST'])
def user_register(request):
    """
    Registers a new user account and returns a unique authentication token.
    """
    try:
        data = request.data
        username = data.get('username')
        password = data.get('password')
        if not username or not password:
            return JsonResponse({"error": "Username and password are required"}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already exists"}, status=400)
        user = User.objects.create_user(username=username, password=password)
        token, _ = Token.objects.get_or_create(user=user)
        return JsonResponse({"message": "User registered successfully", "token": token.key}, status=201)
    except Exception as e: 
        return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
@api_view(['POST'])
def user_login(request):
    """
    Authenticates existing user credentials and signs a valid access token.
    """
    try:
        data = request.data
        user = authenticate(username=data.get('username'), password=data.get('password'))
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return JsonResponse({"message": "Login successful", "token": token.key}, status=200)
        return JsonResponse({"error": "Invalid credentials"}, status=401)
    except Exception as e: 
        return JsonResponse({"error": str(e)}, status=400)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_profile(request):
    """
    Retrieves secure profile details using Token Authentication headers.
    """
    return JsonResponse({
        "username": request.user.username,
        "email": request.user.email,
        "date_joined": request.user.date_joined
    }, status=200)
