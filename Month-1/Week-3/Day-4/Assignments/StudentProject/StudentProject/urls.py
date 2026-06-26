from django.urls import path
from . import views
urlpatterns = [
    path('', views.student_list_or_create, name='student_list_or_create'),
    path('api/students/', views.student_list_or_create, name='student_list_or_create'),
    path('api/students/<int:pk>/', views.student_detail, name='student_detail'),
]
