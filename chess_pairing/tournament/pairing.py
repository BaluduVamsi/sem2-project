from django.db.models import Q
from .models import Tournament, Player, Round, Game, TournamentRegistration

class SwissPairing:
    def __init__(self, tournament):
        self.tournament = tournament
    
    def create_pairings(self, players):
        # Sort players by score (descending) and rating (descending)
        sorted_players = sorted(
            players,
            key=lambda p: (self._calculate_score(p), p.rating),
            reverse=True
        )
        
        pairings = []
        paired = set()
        
        for i, player1 in enumerate(sorted_players):
            if player1 in paired:
                continue
                
            # Find the next unpaired player with the closest score who hasn't played before
            for j in range(i+1, len(sorted_players)):
                player2 = sorted_players[j]
                if player2 not in paired and not self._have_played_before(player1, player2):
                    pairings.append((player1, player2))
                    paired.add(player1)
                    paired.add(player2)
                    break
            else:
                # If no suitable opponent found, pair with the next available player
                for j in range(i+1, len(sorted_players)):
                    player2 = sorted_players[j]
                    if player2 not in paired:
                        pairings.append((player1, player2))
                        paired.add(player1)
                        paired.add(player2)
                        break
        
        # Handle odd number of players (give one player a bye)
        if len(paired) < len(sorted_players):
            unpaired = [p for p in sorted_players if p not in paired]
            if unpaired:
                # Give the lowest-ranked unpaired player a bye
                bye_player = unpaired[-1]
                pairings.append((bye_player, None))  # None indicates a bye
        
        return pairings
    
    def _calculate_score(self, player):
        # Calculate total score from previous rounds
        total = 0
        previous_rounds = Round.objects.filter(
            tournament=self.tournament,
            is_completed=True
        )
        
        for round in previous_rounds:
            games = Game.objects.filter(
                Q(round=round) & 
                (Q(white_player=player) | Q(black_player=player))
            )
            
            for game in games:
                if game.white_player == player:
                    if game.result == '1':
                        total += 1
                    elif game.result == '½':
                        total += 0.5
                elif game.black_player == player:
                    if game.result == '0':
                        total += 1
                    elif game.result == '½':
                        total += 0.5
        
        return total
    
    def _have_played_before(self, player1, player2):
        # Check if these players have played before in this tournament
        return Game.objects.filter(
            Q(tournament=self.tournament) &
            (
                (Q(white_player=player1) & Q(black_player=player2)) |
                (Q(white_player=player2) & Q(black_player=player1))
            )
        ).exists()