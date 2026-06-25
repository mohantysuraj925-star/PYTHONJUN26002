from django.contrib import admin
from django.urls import path
from StudentApp.views import student_list_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/students/', student_list_api, name='student-list-api'),
]
