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
    Returns core infrastructure configuration map directly on primary link.
    """
    return JsonResponse({
        "status": "Running",
        "message": "StudentProject Day-5 Token Authentication System is active.",
        "endpoints": {
            "user_registration": "/api/register/",
            "user_login": "/api/login/",
            "user_profile": "/api/profile/"
        }
    })

@csrf_exempt
@api_view(['POST'])
def user_register(request):
    """
    Creates fresh profile instances mapping secure access authorization signatures.
    """
    try:
        data = request.data
        username = data.get('username')
        password = data.get('password')
        email = data.get('email', '')

        if not username or not password:
            return JsonResponse({"error": "Username and password values are mandatory"}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Profile account username already identity matched"}, status=400)

        user = User.objects.create_user(username=username, password=password, email=email)
        token, _ = Token.objects.get_or_create(user=user)

        return JsonResponse({
            "message": "User registered securely",
            "username": user.username,
            "token": token.key
        }, status=201)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
@api_view(['POST'])
def user_login(request):
    """
    Verifies user parameters to distribute valid security session authentication tokens.
    """
    try:
        data = request.data
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return JsonResponse({
                "message": "Authentication handshake confirmed",
                "username": user.username,
                "token": token.key
            }, status=200)
        else:
            return JsonResponse({"error": "Invalid profile security authentication matching"}, status=401)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_profile(request):
    """
    Validates tokens to retrieve secure protected active profile details.
    """
    return JsonResponse({
        "username": request.user.username,
        "email": request.user.email,
        "date_joined": request.user.date_joined
    }, status=200)
