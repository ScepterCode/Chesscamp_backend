# chess_api/urls.py

from django.urls import path
from . import views
from .views import PlayerStatsView
from .views import TournamentBracketView, TournamentProgressView


urlpatterns = [
    path('player/<str:chess_com_username>/', views.PlayerDetailView.as_view(), name='player_profile'),
    path('player/<str:username>/archives/', views.player_game_archives, name='player_game_archives'),
    path('player/<str:chess_com_username>/campus/', views.PlayerCampusView.as_view(), name='player_campus'),
    path('tournament/create/', views.CreateTournamentView.as_view(), name='create_tournament'),
    path('tournament/submit-result/', views.SubmitTournamentResultView.as_view(), name='submit_tournament_result'),
    path('leaderboard/', views.LeaderboardView.as_view(), name='leaderboard'),
    path('api/player/<str:username>/stats/', PlayerStatsView.as_view(), name='player-stats'),
    path('api/tournament/<int:tournament_id>/bracket/', TournamentBracketView.as_view(), name='tournament-bracket'),
    path('api/tournament/<int:tournament_id>/progress/', TournamentProgressView.as_view(), name='tournament-progress'),
    path('api/invitation/send/', views.send_invitation, name='send_invitation'),
    path('api/invitation/<int:invitation_id>/respond/', views.respond_to_invitation, name='respond_to_invitation'),
]




   