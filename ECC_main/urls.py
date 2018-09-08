from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('sample/', include('sample.urls')),
    path('calendar-service/', include('calendar_service.urls')),
    path('chat-service/', include('chat_service.urls')),
    path('iot-service/', include('iot_service.urls')),
]
