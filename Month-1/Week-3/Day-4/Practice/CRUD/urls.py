from django.contrib import admin
from django.urls import path
from events.views import welcome, addEvent, getEvents, getEventByID, updateEvent, delteEvent, getEventByPaginate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name="welcome"),
    path('addEvent/', addEvent, name="addEvent"),
    path('getEvents/', getEvents, name="getEvents"),
    path('getEventByID/<int:id>/', getEventByID, name="getEventByID"),
    path('updateEvent/<int:id>/', updateEvent, name="updateEvent"),
    path('delteEvent/<int:id>/', delteEvent, name="delteEvent"),
    path('getEventByPaginate/', getEventByPaginate, name="getEventByPaginate")
]
