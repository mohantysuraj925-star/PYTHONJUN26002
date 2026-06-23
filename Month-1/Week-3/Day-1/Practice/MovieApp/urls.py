from django.urls import path
from . import views

urlpatterns = [
    path('', views.add, name='add'), # Root par hi direct add view chalega
    path('add/', views.add, name='add'), # Backup ke liye /add/ bhi chalega
]
