from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Direct main root par views mapping pass karna
    path('', include('urls')), 
]
