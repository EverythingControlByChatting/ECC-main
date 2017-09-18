from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^search/lunch$', views.lunch, name='lunch'),
    url(r'^category$', views.lunch_category, name='category')
]