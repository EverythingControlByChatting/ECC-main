from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^calendar/calendarlist$', views.calendarlist, name='calendarlist'),
    url(r'^calendar/eventinsert$', views.eventinsert, name='eventinsert'),
    url(r'^calendar/eventdelete$', views.eventdelete, name='eventdelete'),
    url(r'^calendar/eventupdate$', views.eventupdate, name='eventupdate'),
    url(r'^calendar/eventlist$', views.eventlist, name='eventlist'),
    url(r'^calendar/help$', views.help, name='help'),
    url(r'^calendar/redirect', views.redirect, name='redirect')
]