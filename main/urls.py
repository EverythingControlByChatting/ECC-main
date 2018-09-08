from django.urls import path
from . import views

urlpatterns = [
    path('slack/add', views.slack_add, name='slack_add'),
    path('slack/oauth', views.slack_oauth, name='slack_oauth'),
]
