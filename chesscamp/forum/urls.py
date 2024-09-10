# community/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('forum/create/', views.CreateForumView.as_view(), name='create_forum'),
    path('forum/<int:forum_id>/', views.ViewForumPostsView.as_view(), name='view_forum_posts'),
    path('forum/<int:forum_id>/post/', views.AddForumPostView.as_view(), name='add_forum_post'),
    path('forum/post/<int:post_id>/comment/', views.AddPostCommentView.as_view(), name='add_post_comment'),
    path('chat/create/', views.CreateChatGroupView.as_view(), name='create_chat_group'),
    path('chat/<int:chat_id>/message/', views.SendChatMessageView.as_view(), name='send_chat_message'),
    path('chat/<int:chat_id>/messages/', views.ViewChatMessagesView.as_view(), name='view_chat_messages'),
]
