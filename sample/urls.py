from django.urls import path
from . import views

urlpatterns = [
    path('wiki/slash-commands', views.wiki_slash_commands, name='wiki'),
    path('short-delay-message/slash-commands', views.short_delay_message, name='short-delay-message'),
]
