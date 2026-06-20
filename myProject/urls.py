from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('student/', views.student, name='student'),
    path('about_company/', views.about_company, name='about_company'),
    path('faq/', views.faq, name='faq'),
    path('team/', views.team, name='team'),
]
