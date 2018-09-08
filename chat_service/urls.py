from django.urls import path
from . import views

urlpatterns = [
    path('search/lunch', views.lunch, name='lunch'),
    path('category', views.lunch_category, name='category')
]
