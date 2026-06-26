import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Student

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
        results = [{"id": s.id, "name": s.name, "email": s.email, "phone": s.phone, "course": s.course} for s in page_obj.object_list]
        host = request.build_absolute_uri('/')
        return JsonResponse({"count": total_count, "next": f"{host}?page={page_obj.next_page_number()}" if page_obj.has_next() else None, "previous": f"{host}?page={page_obj.previous_page_number()}" if page_obj.has_previous() else None, "results": results}, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        student = Student.objects.create(name=data.get('name'), email=data.get('email'), phone=data.get('phone'), course=data.get('course'))
        return JsonResponse({"id": student.id, "name": student.name, "email": student.email, "phone": student.phone, "course": student.course}, status=201)
