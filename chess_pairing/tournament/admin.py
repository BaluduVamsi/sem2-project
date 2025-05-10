# tournament/admin.py
from django.contrib import admin
from .models import Tournament, Player, Round, Game, TournamentRegistration

class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'location', 'is_active')
    list_filter = ('is_active', 'start_date')
    search_fields = ('name', 'location')

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'title')
    search_fields = ('user__username', 'user__first_name', 'user__last_name')

class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'round', 'white_player', 'black_player', 'result')
    list_filter = ('round__tournament', 'round')

admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Round)
admin.site.register(Game, GameAdmin)
admin.site.register(TournamentRegistration)