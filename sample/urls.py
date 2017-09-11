from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^wiki/slash-commands$', views.wiki_slash_commands, name='wiki'),
]