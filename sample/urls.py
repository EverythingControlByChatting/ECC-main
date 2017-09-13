from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^wiki/slash-commands$', views.wiki_slash_commands, name='wiki'),
    url(r'^short-delay-message/slash-commands$', views.short_delay_message, name='short-delay-message'),
]