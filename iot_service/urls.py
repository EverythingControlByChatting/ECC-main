from django.urls import path
from . import views

urlpatterns = [
    path('acon', views.acon, name='acon'),
    path('acoff', views.acoff, name='acoff'),
    path('acsuper', views.acsuper, name='acsuper'),
    path('achelp', views.achelp, name='achelp'),
]
