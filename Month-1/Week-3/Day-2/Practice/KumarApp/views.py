from rest_framework.decorators import api_view
from rest_framework.response import Response

# Welcome endpoint to check API health
@api_view(['GET'])
def welcome(request):
    return Response({"message": "Welcome to SuraajCore API"})

# Endpoint specifically for POST requests
@api_view(['POST'])
def post_data(request):
    return Response({"status": "POST request received successfully"})

# Multi-method handler for GET and POST requests
@api_view(['GET', 'POST'])
def handle_data(request):
    if request.method == "POST":
        return Response({"action": "Data Received via POST"})
    return Response({"action": "Data Fetched via GET"})
