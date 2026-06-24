from django.contrib import admin
from django.urls import path
from firstapi.views import welcome,postmethod,getorpost

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', welcome, name="welcome"),
    path('post-method/', postmethod, name="postmethod"),
    path('get-or-post/', getorpost, name="getorpost")
]
