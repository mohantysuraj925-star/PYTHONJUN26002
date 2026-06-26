from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/students/', views.student_list_or_create, name='student_list_or_create'),
    path('api/students/<int:pk>/', views.student_detail, name='student_detail'),
]
