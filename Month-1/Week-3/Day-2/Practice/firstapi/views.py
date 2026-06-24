from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

@api_view(['GET'])
def welcome(request):
    return Response("Welcome to apis")

@csrf_exempt
@api_view(['GET', 'POST', 'PUT'])
def postmethod(request):
    if request.method == 'GET':
        return Response("This is GET method")
    elif request.method == 'POST':
        return Response("This is POST method")
    return Response("Method not supported")
