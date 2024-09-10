
# community/views.py
from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Forum, ForumPost, PostComment, ChatGroup, ChatMessage
from .serializers import ForumSerializer, ForumPostSerializer, PostCommentSerializer, ChatGroupSerializer, ChatMessageSerializer

class CreateForumView(generics.CreateAPIView):
    serializer_class = ForumSerializer
    permission_classes = [permissions.IsAuthenticated]

class ViewForumPostsView(generics.ListAPIView):
    serializer_class = ForumPostSerializer

    def get_queryset(self):
        return ForumPost.objects.filter(forum_id=self.kwargs['forum_id'])

class AddForumPostView(generics.CreateAPIView):
    serializer_class = ForumPostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, forum_id=self.kwargs['forum_id'])

class AddPostCommentView(generics.CreateAPIView):
    serializer_class = PostCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        post = ForumPost.objects.get(id=self.kwargs['post_id'])
        serializer.save(author=self.request.user, post=post)

class CreateChatGroupView(generics.CreateAPIView):
    serializer_class = ChatGroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class SendChatMessageView(generics.CreateAPIView):
    serializer_class = ChatMessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, chat_group_id=self.kwargs['chat_id'])

class ViewChatMessagesView(generics.ListAPIView):
    serializer_class = ChatMessageSerializer

    def get_queryset(self):
        return ChatMessage.objects.filter(chat_group_id=self.kwargs['chat_id'])

