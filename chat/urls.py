from django.urls import path
from . import views

urlpatterns = [
    path('api/users/chat/<int:sender>/<int:receiver>/', views.sendMessage, name='send_message'),
    path('api/users/chat/<int:sender>/', views.getMessageBySender, name='get_message_by_sender'),
    path('api/users/chat/<int:receiver>/', views.getMessageByReceiver, name='get_message_by_receiver'),
    path('api/users/chat/get/<int:sender>/<int:receiver>/', views.getMessage, name='get_message'),
]