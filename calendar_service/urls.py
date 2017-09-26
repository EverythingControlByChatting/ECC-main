from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^calendar/list$', views.calendarlist, name='calendar-list'),
    url(r'^event/insert$', views.eventinsert, name='event-insert'),
    url(r'^event/delete$', views.eventdelete, name='event-delete'),
    url(r'^event/update$', views.eventupdate, name='event-update'),
    url(r'^event/list$', views.eventlist, name='event-list'),
    url(r'^calendar/help$', views.help, name='calendar-help'),
    url(r'^calendar/redirect', views.redirect, name='redirect')
]