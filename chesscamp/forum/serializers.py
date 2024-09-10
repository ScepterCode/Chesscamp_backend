
# community/serializers.py

from rest_framework import serializers
from .models import Forum, ForumPost, PostComment, ChatGroup, ChatMessage

class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = ['id', 'name', 'description', 'campus', 'city', 'created_at']

class ForumPostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = ForumPost
        fields = ['id', 'forum', 'author', 'author_name', 'title', 'content', 'created_at']

class PostCommentSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = PostComment
        fields = ['id', 'post', 'author', 'author_name', 'content', 'created_at']

class ChatGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatGroup
        fields = ['id', 'name', 'campus', 'tournament', 'created_at']

class ChatMessageSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = ChatMessage
        fields = ['id', 'chat_group', 'author', 'author_name', 'content', 'created_at']

