
# chess/models.py

from django.db import models
from django.contrib.auth.models import User

class Campus(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    chess_com_username = models.CharField(max_length=100)
    campus = models.ForeignKey(Campus, on_delete=models.SET_NULL, null=True)
    local_rating = models.IntegerField(default=1500)

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name='tournaments')
    rounds = models.IntegerField(default=1)
    current_round = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)

class TournamentResult(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    position = models.IntegerField()
    points = models.FloatField()

class PlayerStats(models.Model):
    player = models.OneToOneField(User, on_delete=models.CASCADE, related_name="stats")
    games_played = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    win_ratio = models.FloatField(default=0.0)
    average_game_time = models.DurationField(null=True, blank=True)

    def update_stats(self, win=None, game_time=None):
        self.games_played += 1
        if win is not None:
            if win:
                self.wins += 1
            else:
                self.losses += 1
        else:
            self.draws += 1
        
        if self.games_played > 0:
            self.win_ratio = self.wins / self.games_played

        if game_time:
            if self.average_game_time:
                total_time = self.average_game_time.total_seconds() * (self.games_played - 1) + game_time.total_seconds()
                self.average_game_time = total_time / self.games_played
            else:
                self.average_game_time = game_time
        self.save()


class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='matches')
    round_number = models.IntegerField()
    player1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='match_player1')
    player2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='match_player2')
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='match_winner')

    def progress_tournament(self):
        tournament = self.tournament
        if Match.objects.filter(tournament=tournament, round_number=tournament.current_round, winner__isnull=True).exists():
            return False  # Not all matches in the current round are finished
        if tournament.current_round < tournament.rounds:
            tournament.current_round += 1
            tournament.save()
            return True
        else:
            tournament.is_active = False
            tournament.save()
            return False
        

class GameInvitation(models.Model):
    sender = models.ForeignKey(User, related_name='invitations_sent', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='invitations_received', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Game Invitation from {self.sender.username} to {self.receiver.username} - {self.status}"