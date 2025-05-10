from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_player_profile(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance, rating=1200)

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1200)
    title = models.CharField(max_length=10, blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.get_full_name()} ({self.rating})"

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=100)
    rounds = models.IntegerField(default=5)
    current_round = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    players = models.ManyToManyField(Player, through='TournamentRegistration')
    
    def __str__(self):
        return self.name

class TournamentRegistration(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('player', 'tournament')

class Round(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    round_number = models.IntegerField()
    is_completed = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('tournament', 'round_number')  # This is what causes the error

class Game(models.Model):
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    white_player = models.ForeignKey(Player, related_name='white_games', on_delete=models.CASCADE)
    black_player = models.ForeignKey(Player, related_name='black_games', on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=True)
    result = models.CharField(max_length=1, choices=[
        ('1', 'White wins'),
        ('0', 'Black wins'),
        ('½', 'Draw'),
        ('-', 'Not played yet'),
    ], default='-')
    
    def __str__(self):
        return f"{self.white_player} vs {self.black_player} - {self.get_result_display()}"
    def save(self, *args, **kwargs):
        if not self.tournament and self.round:
            self.tournament = self.round.tournament
        super().save(*args, **kwargs)
