from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^search/lunch$', views.lunch, name='wiki'),
]