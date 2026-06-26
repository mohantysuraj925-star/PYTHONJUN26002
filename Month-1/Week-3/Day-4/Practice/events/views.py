from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EventSerializer
from .models import Event
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@api_view(['GET'])
def welcome(request):
    return Response("Welcome to events apis...")

@api_view(['POST'])
def addEvent(request):
    # Data structure aur validation ka logic
    if not request.data:
        return Response({"error": "Request body cannot be empty"}, status=400)
        
    ser = EventSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response({
            "status": "Success",
            "message": "Event added to SQL database successfully",
            "data": ser.data
        }, status=201)
        
    return Response({
        "status": "Failed",
        "errors": ser.errors
    }, status=400)

@api_view(['GET'])
def getEvents(request):
    events = Event.objects.all().order_by('id')
    if not events.exists():
        return Response({"message": "Database is currently empty", "data": []})
    serData = EventSerializer(events, many=True)
    return Response(serData.data)

@api_view(['GET'])
def getEventByID(request, id):
    try:
        event = Event.objects.get(id=id)
        serData = EventSerializer(event)
        return Response({
            "status": True,
            "data": serData.data,
            "message": f"Event {id} fetched successfully"
        })
    except Event.DoesNotExist:
        return Response({
            "status": False,
            "data": [],
            "message": f"Event with ID {id} does not exist in database"
        }, status=404)

@api_view(['PUT'])
def updateEvent(request, id):
    try:
        event = Event.objects.get(id=id)
    except Event.DoesNotExist:
        return Response({"message": "Event not found for update"}, status=404)
    
    serData = EventSerializer(event, data=request.data, partial=True)
    if serData.is_valid():
        serData.save()
        return Response({
            "message": "Event updated successfully",
            "updated_data": serData.data
        })
    return Response({"errors": serData.errors}, status=400)

@api_view(['DELETE'])
def delteEvent(request, id):
    try:
        event = Event.objects.get(id=id)
        event.delete()
        return Response({"message": f"Event {id} deleted successfully from SQL"})
    except Event.DoesNotExist:
        return Response({"message": "Event not found"}, status=404)

@api_view(['GET'])
def getEventByPaginate(request):
    # Advanced Multi-Page Request Conditional Logic
    try:
        page = request.GET.get('page', 1)
        per_page = request.GET.get('per_page', 5)
        
        # Datatype validation logic
        try:
            page = int(page)
            per_page = int(per_page)
        except ValueError:
            return Response({"error": "Page and per_page parameters must be integers"}, status=400)

        events_list = Event.objects.all().order_by('id')
        total_records = events_list.count()
        
        paginator = Paginator(events_list, per_page)
        
        # Page-by-page rendering and validation boundary logic
        try:
            page_obj = paginator.get_page(page)
        except EmptyPage:
            page_obj = paginator.get_page(paginator.num_pages)
        except PageNotAnInteger:
            page_obj = paginator.get_page(1)
            
        serData = EventSerializer(page_obj.object_list, many=True)
        
        # Complete preview structural payload for total 3-4 pages monitoring
        return Response({
            "status": "Render Ready",
            "total_records_in_sql": total_records,
            "payload": serData.data,
            "navigation_logic": {
                "requested_page": page,
                "items_per_page": per_page,
                "current_page_number": page_obj.number,
                "total_available_pages": paginator.num_pages,
                "has_next_page_exists": page_obj.has_next(),
                "has_previous_page_exists": page_obj.has_previous(),
                "next_page_index": page_obj.next_page_number() if page_obj.has_next() else None,
                "previous_page_index": page_obj.previous_page_number() if page_obj.has_previous() else None
            }
        })
    except Exception as e:
        return Response({"system_error": str(e)}, status=500)
