import os

import django
from django.db.models import Q, Count, Avg, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Director, Actor, Movie


# Create queries within functions
# Django Queries I
def get_directors(search_name=None, search_nationality=None):
    if search_name is None and search_nationality is None:
        return ''

    if search_name is not None and search_nationality is None:
        query = Q(full_name__icontains=search_name)
    elif search_name is None and search_nationality is not None:
        query = Q(nationality__icontains=search_nationality)
    else:
        query = Q(full_name__icontains=search_name) & Q(nationality__icontains=search_nationality)
    directors = (Director.objects.filter(query).order_by('full_name'))

    if not directors:
        return ''

    return "\n".join([f"Director: {d.full_name}, "
                      f"nationality: {d.nationality}, "
                      f"experience: {d.years_of_experience}" for d in directors])


def get_top_director():
    directors = Director.objects.get_directors_by_movies_count()

    if not directors:
        return ''

    director = directors.first()
    return f"Top Director: {director.full_name}, movies: {director.movies_num}."


def get_top_actor():
    actor = (Actor.objects.prefetch_related('starring_actor_movies')
             .annotate(
        movies_num=Count('starring_actor_movies'),
        average_rating=Avg('starring_actor_movies__rating')
    ).order_by('-movies_num', 'full_name').first())

    if not actor:
        return ''

    movies = actor.starring_actor_movies.all()

    if not movies:
        return ''

    return (f"Top Actor: {actor.full_name}, "
            f"starring in movies: {', '.join([m.title for m in movies if m])}, "
            f"movies average rating: {actor.average_rating:.1f}")


# Django Queries II
def get_actors_by_movies_count():
    actors = (Actor.objects.annotate(movies_num=Count('actor_movies'))
              .order_by('-movies_num', 'full_name'))[:3]

    if not actors or not actors[0].movies_num:
        return ""

    result = []

    for actor in actors:
        result.append(f"{actor.full_name}, participated in {actor.movies_num} movies")

    return "\n".join(result)


def get_top_rated_awarded_movie():
    movie = ((Movie.objects.
             select_related('starring_actor')
              .prefetch_related('actors')).filter(is_awarded=True)
             .order_by('-rating', 'title').first())

    if movie is None:
        return ""

    cast = ", ".join([a.full_name for a in movie.actors.order_by('full_name')])
    starring_actor_name = movie.starring_actor.full_name if movie.starring_actor else "N/A"

    return f"Top rated awarded movie: {movie.title}, rating: {movie.rating:.1f}. " \
           f"Starring actor: {starring_actor_name}. Cast: {cast}."


def increase_rating():
    movies = Movie.objects.filter(Q(is_classic=True) & Q(rating__lt=10.0))

    if not movies:
        return "No ratings increased."

    updated_movies_num = movies.update(rating=F('rating') + 0.1)
    return f"Rating increased for {updated_movies_num} movies."
