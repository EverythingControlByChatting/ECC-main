from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^on$', views.on, name='on'),
    url(r'^off$', views.off, name='off'),
    url(r'^super$', views.super, name='super'),
    url(r'^set$', views.set, name='set'),
]
