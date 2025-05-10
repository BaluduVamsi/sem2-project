from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tournament, Player, Round, Game, TournamentRegistration
from .pairing import SwissPairing
from django.contrib import messages
from django.db import transaction  
@login_required
@transaction.atomic
def complete_round(request, round_id):
    round_obj = get_object_or_404(Round, pk=round_id)
    
    if request.method == 'POST':
        # Check for incomplete games (excluding BYEs)
        incomplete_games = Game.objects.filter(
            round=round_obj,
            result='-'
        ).exclude(black_player=None).exists()
        
        if incomplete_games:
            messages.error(request, "Cannot complete round with unfinished games")
        else:
            round_obj.is_completed = True
            round_obj.save()
            messages.success(request, f"Round {round_obj.round_number} marked as completed")
    
    return redirect('round_detail', round_id=round_obj.id)
@login_required
@transaction.atomic
def pair_round(request, tournament_id):
    tournament = get_object_or_404(Tournament, pk=tournament_id)
    
    # Validate tournament state
    if tournament.current_round >= tournament.rounds:
        messages.error(request, "Tournament has completed all rounds")
        return redirect('tournament_detail', tournament_id=tournament_id)
    
    # Get registered players
    registrations = TournamentRegistration.objects.filter(tournament=tournament)
    if registrations.count() < 2:
        messages.error(request, "Need at least 2 players to pair a round")
        return redirect('tournament_detail', tournament_id=tournament_id)
    
    # Check current round completion
    current_round = Round.objects.filter(
        tournament=tournament,
        round_number=tournament.current_round
    ).first()
    
    if current_round and not current_round.is_completed:
        incomplete_games = Game.objects.filter(
            round=current_round,
            result='-',
            black_player__isnull=False
        ).exists()
        
        if incomplete_games:
            messages.error(request, f"Complete all games in Round {tournament.current_round} first")
            return redirect('round_detail', round_id=current_round.id)
        
        current_round.is_completed = True
        current_round.save()

    # Create new round
    next_round_number = tournament.current_round + 1
    try:
        new_round = Round.objects.create(
            tournament=tournament,
            round_number=next_round_number,
            is_completed=False
        )
    except IntegrityError:
        messages.error(request, f"Round {next_round_number} already exists")
        return redirect('tournament_detail', tournament_id=tournament_id)
    
    # Generate pairings and create games
    players = [reg.player for reg in registrations]
    pairings = SwissPairing(tournament).create_pairings(players)
    
    if not pairings:
        messages.error(request, "Failed to generate pairings")
        return redirect('tournament_detail', tournament_id=tournament_id)
    
    for white, black in pairings:
        Game.objects.create(
            round=new_round,
            tournament=tournament,
            white_player=white,
            black_player=black,
            result='1' if black is None else '-'
        )
    
    # Update tournament state
    tournament.current_round = next_round_number
    tournament.save()
    
    messages.success(request, f"Round {next_round_number} paired with {len(pairings)} games created!")
    return redirect('round_detail', round_id=new_round.id)
@login_required
def tournament_list(request):
    tournaments = Tournament.objects.filter(is_active=True)
    return render(request, 'tournament/list.html', {'tournaments': tournaments})

@login_required
def tournament_detail(request, tournament_id):
    tournament = get_object_or_404(Tournament, pk=tournament_id)
    registrations = TournamentRegistration.objects.filter(tournament=tournament)
    rounds = Round.objects.filter(tournament=tournament)
    
    context = {
        'tournament': tournament,
        'registrations': registrations,
        'rounds': rounds,
    }
    return render(request, 'tournament/detail.html', context)

@login_required
def round_detail(request, round_id):
    round = get_object_or_404(Round, pk=round_id)
    games = Game.objects.filter(round=round)
    
    return render(request, 'tournament/round.html', {
        'round': round,
        'games': games,
    })

@login_required
@transaction.atomic
def pair_round(request, tournament_id):
    tournament = get_object_or_404(Tournament, pk=tournament_id)
    
    # Prevent exceeding max rounds
    if tournament.current_round >= tournament.rounds:
        messages.error(request, "Tournament has completed all rounds")
        return redirect('tournament_detail', tournament_id=tournament_id)
    
    # Check if next round already exists
    next_round_number = tournament.current_round + 1
    if Round.objects.filter(tournament=tournament, round_number=next_round_number).exists():
        messages.error(request, f"Round {next_round_number} already exists")
        return redirect('tournament_detail', tournament_id=tournament_id)
    
    # Check current round completion
    current_round = Round.objects.filter(
        tournament=tournament,
        round_number=tournament.current_round
    ).first()
    
    if current_round and not current_round.is_completed:
        incomplete_games = Game.objects.filter(
            round=current_round,
            result='-',
            black_player__isnull=False
        ).exists()
        
        if incomplete_games:
            messages.error(request, f"Complete all games in Round {tournament.current_round} first")
            return redirect('round_detail', round_id=current_round.id)
        
        current_round.is_completed = True
        current_round.save()
    
    # Create new round
    new_round = Round.objects.create(
        tournament=tournament,
        round_number=next_round_number,
        is_completed=False
    )
    
    # Rest of your pairing logic...
    # [Keep your existing player pairing and game creation code]
    
    tournament.current_round = next_round_number
    tournament.save()
    
    messages.success(request, f"Round {next_round_number} paired successfully!")
    return redirect('round_detail', round_id=new_round.id)
@login_required
def complete_round(request, round_id):
    round = get_object_or_404(Round, pk=round_id)
    
    if request.method == 'POST':
        # Verify all games have results
        incomplete_games = Game.objects.filter(
            round=round,
            result='-'
        ).exclude(black_player=None)  # Exclude BYE games
        
        if incomplete_games.exists():
            messages.error(request, "Not all games have results submitted!")
            return redirect('round_detail', round_id=round.id)
        
        round.is_completed = True
        round.save()
        
        messages.success(request, f"Round {round.round_number} marked as completed!")
    
    return redirect('round_detail', round_id=round.id)

@login_required
def register_player(request, tournament_id):
    tournament = get_object_or_404(Tournament, pk=tournament_id)
    player = get_object_or_404(Player, user=request.user)
    
    if request.method == 'POST':
        TournamentRegistration.objects.get_or_create(
            player=player,
            tournament=tournament
        )
        messages.success(request, "You have been registered for the tournament!")
        return redirect('tournament_detail', tournament_id=tournament_id)
    
    return render(request, 'tournament/register_player.html', {
        'tournament': tournament
    })
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Tournament, Player, Round, Game, TournamentRegistration

@login_required
def submit_result(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    
    if request.method == 'POST':
        result = request.POST.get('result')
        if result in ['1', '0', '½']:
            game.result = result
            game.save()
            messages.success(request, "Game result submitted successfully!")
            return redirect('round_detail', round_id=game.round.id)
        else:
            messages.error(request, "Invalid result submitted")
    
    return redirect('round_detail', round_id=game.round.id)
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
@login_required
def register_player(request, tournament_id):
    tournament = get_object_or_404(Tournament, pk=tournament_id)
    
    # Get or create player profile
    player, created = Player.objects.get_or_create(user=request.user)
    if created:
        # Set default values for new players
        player.rating = 1200
        player.save()
    
    if request.method == 'POST':
        TournamentRegistration.objects.get_or_create(
            player=player,
            tournament=tournament
        )
        messages.success(request, "Registration successful!")
        return redirect('tournament_detail', tournament_id=tournament_id)
    
    return render(request, 'tournament/register_confirmation.html', {
        'tournament': tournament
    })