from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.views.decorators.csrf import csrf_exempt

# Class Practice: User Registration Endpoint
@csrf_exempt
@api_view(['POST'])
def user_register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return JsonResponse({"msg": "username and password required"}, status=400)
        
    if User.objects.filter(username=username).exists():
        return JsonResponse({"msg": "user already exists"}, status=400)
        
    user = User.objects.create_user(username=username, password=password)
    token, created = Token.objects.get_or_create(user=user)
    return JsonResponse({"status": "success", "token": token.key}, status=201)

# Class Practice: User Login Endpoint 
@csrf_exempt
@api_view(['POST'])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return JsonResponse({"msg": "login done", "token": token.key}, status=200)
    
    return JsonResponse({"msg": "invalid credentials"}, status=401)

# Class Practice: Token Protected Profile Endpoint
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_profile(request):
    return JsonResponse({
        "username": request.user.username,
        "email": request.user.email,
        "msg": "welcome to profile page"
    }, status=200)
