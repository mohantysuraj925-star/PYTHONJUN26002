from django.contrib import admin
from django.urls import path
from KumarApp.views import welcome, post_data, handle_data

# URL Patterns for SuraajCore Project
urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', welcome, name="welcome"),      # GET only
    path('post/', post_data, name="post_data"),     # POST only
    path('process/', handle_data, name="handle_data"), # GET & POST
]
