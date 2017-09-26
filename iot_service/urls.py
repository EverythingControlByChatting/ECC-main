from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^acon$', views.acon, name='acon'),
    url(r'^acoff$', views.acoff, name='acoff'),
    url(r'^acsuper$', views.acsuper, name='acsuper'),
    url(r'^achelp$', views.achelp, name='achelp'),
]
