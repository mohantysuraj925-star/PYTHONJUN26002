from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from firstapi.views import welcome, postmethod, getorpost

urlpatterns = [
    path('', RedirectView.as_view(url='welcome/', permanent=False)), # Main link ko welcome par bhej dega
    path('admin/', admin.site.urls),
    path('welcome/', welcome, name="welcome"),
    path('post-method/', postmethod, name="postmethod"),
    path('get-or-post/', getorpost, name="getorpost")
]
