import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


# Import your models here
from main_app.models import TennisPlayer, Tournament, Match
from django.db.models import Count, Q


# Django Queries I
def get_tennis_players(search_name=None, search_country=None):
    if search_name is None and search_country is None:
        return ''

    query = Q()
    if search_name is not None and search_country is None:
        query = Q(full_name__icontains=search_name)
    elif search_name is None and search_country is not None:
        query = Q(country__icontains=search_country)
    else:
        query = Q(full_name__icontains=search_name) & Q(country__icontains=search_country)

    tennis_players = TennisPlayer.objects.filter(query).order_by('ranking')
    if not tennis_players:
        return ''

    return '\n'.join([f'Tennis Player: {t.full_name}, country: {t.country}, ranking: {t.ranking}'
                      for t in tennis_players])


def get_top_tennis_player():
    top_player = TennisPlayer.objects.annotate(wins=Count('winner')).order_by('-wins', 'full_name').first()

    if not top_player:
        return ""

    return f"Top Tennis Player: {top_player.full_name} with {top_player.wins} wins."


def get_tennis_player_by_matches_count():
    top_player = (TennisPlayer.objects
                  .annotate(matches_count=Count('players'))
                  .order_by('-matches_count', 'ranking')
                  .first())

    if not top_player:
        return ""

    if not top_player.matches_count:
        return ""

    return f"Tennis Player: {top_player.full_name} with {top_player.matches_count} matches played."


# Django Queries II
def get_tournaments_by_surface_type(surface=None):
    if surface is None:
        return ""

    tournaments_by_type = (Tournament.objects
                           .filter(surface_type__icontains=surface)
                           .annotate(matches_count=Count('tournaments'))
                           .order_by('-start_date'))

    if not tournaments_by_type:
        return ""

    return "\n".join(f"Tournament: {t.name}, start date: {t.start_date}, matches: {t.matches_count}"
                     for t in tournaments_by_type)


def get_latest_match_info():
    latest_match = Match.objects.order_by('-date_played', '-id').first()
    if not latest_match:
        return ""

    players_names = " vs ".join(p.full_name if p is not None else "TBA" for p in latest_match.players
                                .all().order_by('full_name'))

    winner_name = latest_match.winner.full_name if latest_match.winner is not None else "TBA"

    return (f"Latest match played on: {latest_match.date_played}, "
            f"tournament: {latest_match.tournament.name}, "
            f"score: {latest_match.score}, "
            f"players: {players_names}, "
            f"winner: {winner_name}, "
            f"summary: {latest_match.summary}")


def get_matches_by_tournament(tournament_name=None):
    if tournament_name is None:
        return "No matches found."

    all_matches = Match.objects.filter(tournament__name__exact=tournament_name).order_by('-date_played')

    if not all_matches:
        return "No matches found."

    return "\n".join(f"Match played on: {m.date_played}, score: {m.score}, "
                     f"winner: {m.winner.full_name if m.winner is not None else 'TBA'}" for m in all_matches)
