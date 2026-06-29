import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Student

@csrf_exempt
def student_list_or_create(request):
    """
    API endpoint to list students with pagination (GET) or create a new student (POST).
    """
    if request.method == 'GET':
        students_query = Student.objects.all().order_by('id')
        total_count = students_query.count()
        page_num = request.GET.get('page', 1)
        paginator = Paginator(students_query, 5)
        try:
            page_obj = paginator.get_page(page_num)
        except (PageNotAnInteger, EmptyPage):
            page_obj = paginator.get_page(1)
        results = [{"id": s.id, "name": s.name, "email": s.email, "phone": s.phone, "course": s.course} for s in page_obj.object_list]
        host = request.build_absolute_uri('/')
        next_page = f"{host}?page={page_obj.next_page_number()}" if page_obj.has_next() else None
        previous_page = f"{host}?page={page_obj.previous_page_number()}" if page_obj.has_previous() else None
        return JsonResponse({"count": total_count, "next": next_page, "previous": previous_page, "results": results}, safe=False)
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            student = Student.objects.create(name=data.get('name'), email=data.get('email'), phone=data.get('phone'), course=data.get('course'))
            return JsonResponse({"id": student.id, "name": student.name, "email": student.email, "phone": student.phone, "course": student.course}, status=201)
        except Exception as e: 
            return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def student_detail(request, pk):
    """
    API endpoint to retrieve, update, or delete a specific student instance by ID.
    """
    try: 
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist: 
        return JsonResponse({"error": "Student record not found"}, status=404)
        
    if request.method == 'GET': 
        return JsonResponse({"id": student.id, "name": student.name, "email": student.email, "phone": student.phone, "course": student.course})
    elif request.method == 'PUT':
        try:
            data = json.loads(request.body)
            student.name = data.get('name', student.name)
            student.email = data.get('email', student.email)
            student.phone = data.get('phone', student.phone)
            student.course = data.get('course', student.course)
            student.save()
            return JsonResponse({"id": student.id, "name": student.name, "email": student.email, "phone": student.phone, "course": student.course})
        except Exception as e: 
            return JsonResponse({"error": str(e)}, status=400)
    elif request.method == 'DELETE':
        student.delete()
        return JsonResponse({"message": "Student record deleted successfully"}, status=200)
