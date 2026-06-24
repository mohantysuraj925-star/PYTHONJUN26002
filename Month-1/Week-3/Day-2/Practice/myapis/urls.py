from django.contrib import admin
from django.urls import path
from firstapi.views import welcome, postmethod

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', welcome),
    path('post-method/', postmethod),
]
