from django.urls import path
from . import views

urlpatterns = [
    path('set_webhook', views.set_webhook, name='set_webhook'),
]
