from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^slack/add$', views.slack_add, name='slack_add'),
    url(r'^slack/oauth$', views.slack_oauth, name='slack_oauth'),
]