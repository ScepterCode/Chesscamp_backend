from django.urls import path
from . import views

urlpatterns = [
    path('send/', views.send_notification, name='send_notification'),
    path('<int:user_id>/', views.get_user_notifications, name='get_user_notifications'),
    path('<int:notification_id>/read/', views.mark_notification_read, name='mark_notification_read'),
]
