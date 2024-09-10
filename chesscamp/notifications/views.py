from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Notification
from .serializers import NotificationSerializer, NotificationCreateSerializer

# Send a notification
@api_view(['POST'])
def send_notification(request):
    if request.method == 'POST':
        serializer = NotificationCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve user notifications
@api_view(['GET'])
def get_user_notifications(request, user_id):
    notifications = Notification.objects.filter(user_id=user_id).order_by('-created_at')
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)

# Mark notification as read
@api_view(['PUT'])
def mark_notification_read(request, notification_id):
    try:
        notification = Notification.objects.get(pk=notification_id)
    except Notification.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    notification.is_read = True
    notification.save()
    return Response({'message': 'Notification marked as read'}, status=status.HTTP_200_OK)

