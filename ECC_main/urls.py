from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main/', include('main.urls')),
    url(r'^sample/', include('sample.urls')),
    url(r'^calendar-service/', include('calendar_service.urls')),
    url(r'^chat-service/', include('chat_service.urls')),
    url(r'^iot_service/', include('iot_service.urls')),
]
