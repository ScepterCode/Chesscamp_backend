# chess_api/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Campus, Player, Tournament, TournamentResult
from .models import GameInvitation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = ['id', 'name', 'location']

class PlayerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    campus = CampusSerializer(read_only=True)

    class Meta:
        model = Player
        fields = ['id', 'user', 'chess_com_username', 'campus', 'local_rating']

class PlayerCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['chess_com_username', 'campus', 'local_rating']

    def create(self, validated_data):
        user = self.context['request'].user
        return Player.objects.create(user=user, **validated_data)

class TournamentSerializer(serializers.ModelSerializer):
    campus = CampusSerializer(read_only=True)

    class Meta:
        model = Tournament
        fields = ['id', 'name', 'start_date', 'end_date', 'campus']

class TournamentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ['name', 'start_date', 'end_date', 'campus']

    def validate(self, data):
        if data['start_date'] >= data['end_date']:
            raise serializers.ValidationError("End date must be after start date")
        return data

class TournamentResultSerializer(serializers.ModelSerializer):
    tournament = TournamentSerializer(read_only=True)
    player = PlayerSerializer(read_only=True)

    class Meta:
        model = TournamentResult
        fields = ['id', 'tournament', 'player', 'position', 'points']

class TournamentResultCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentResult
        fields = ['tournament', 'player', 'position', 'points']

    def validate_position(self, value):
        if value < 1:
            raise serializers.ValidationError("Position must be a positive integer")
        return value

    def validate_points(self, value):
        if value < 0:
            raise serializers.ValidationError("Points cannot be negative")
        return value

class LeaderboardEntrySerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    campus_name = serializers.CharField(source='campus.name', allow_null=True)

    class Meta:
        model = Player
        fields = ['id', 'username', 'chess_com_username', 'local_rating', 'campus_name']


class GameInvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameInvitation
        fields = ['id', 'sender', 'receiver', 'status', 'created_at']
