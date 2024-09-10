
from django.contrib import admin
from .models import Campus, Player, Tournament, TournamentResult

@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('user', 'chess_com_username', 'campus', 'local_rating')
    list_filter = ('campus',)
    search_fields = ('user__username', 'chess_com_username')

@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'campus')
    list_filter = ('campus', 'start_date')
    search_fields = ('name',)
    date_hierarchy = 'start_date'

@admin.register(TournamentResult)
class TournamentResultAdmin(admin.ModelAdmin):
    list_display = ('tournament', 'player', 'position', 'points')
    list_filter = ('tournament', 'player')
    search_fields = ('tournament__name', 'player__user__username')
