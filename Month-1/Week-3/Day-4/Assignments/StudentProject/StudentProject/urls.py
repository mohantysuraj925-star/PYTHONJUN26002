from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_index, name='home_index'),
    path('api/students/', views.student_list_or_create, name='student_list_or_create'),
    path('api/students/<int:pk>/', views.student_detail, name='student_detail'),
    path('api/register/', views.user_register, name='user_register'),
    path('api/login/', views.user_login, name='user_login'),
    path('api/profile/', views.user_profile, name='user_profile'),
]
