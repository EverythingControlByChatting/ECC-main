from django.urls import path
from . import views

urlpatterns = [
    path('calendar/list', views.calendarlist, name='calendar-list'),
    path('event/insert', views.eventinsert, name='event-insert'),
    path('event/delete', views.eventdelete, name='event-delete'),
    path('event/update', views.eventupdate, name='event-update'),
    path('event/list', views.eventlist, name='event-list'),
    path('calendar/help', views.help, name='calendar-help'),
    path('calendar/redirect', views.redirect, name='redirect')
]
