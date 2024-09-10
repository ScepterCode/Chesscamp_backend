

from django.contrib import admin
from .models import Forum, ForumPost, PostComment, ChatGroup, ChatMessage

@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'campus', 'city', 'created_at', 'created_by')
    search_fields = ('name', 'description')

@admin.register(ForumPost)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'forum', 'author', 'author', 'created_at')
    search_fields = ('title', 'body')
    list_filter = ('forum',)

@admin.register(PostComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'content', 'created_at')
    search_fields = ('body',)
    list_filter = ('post',)

@admin.register(ChatGroup)
class ChatGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'campus', 'tournament', 'is_tournament_based', 'created_at')
    search_fields = ('name',)

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('chat_group', 'content', 'author', 'created_at')
    search_fields = ('message',)
    list_filter = ('chat_group',)

