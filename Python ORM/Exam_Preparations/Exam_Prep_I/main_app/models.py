from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models
from main_app.base_models import Person, IsAwardedMixin, LastUpdatedMixin
from main_app.choices import MovieGenreChoices
from main_app.managers import DirectorManager


# Create your models here.
class Director(Person):
    years_of_experience = models.SmallIntegerField(default=0, validators=[MinValueValidator(0)])

    objects = DirectorManager()


class Actor(IsAwardedMixin, LastUpdatedMixin, Person):
    ...


class Movie(IsAwardedMixin, LastUpdatedMixin, models.Model):
    title = models.CharField(max_length=150, validators=[MinLengthValidator(5)])
    release_date = models.DateField()
    storyline = models.TextField(blank=True, null=True)
    genre = models.CharField(max_length=6,
                             default="Other",
                             choices=MovieGenreChoices.choices)
    rating = models.DecimalField(max_digits=3,
                                 decimal_places=1,
                                 validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
                                 default=0.0)
    is_classic = models.BooleanField(default=False)

    director = models.ForeignKey(to=Director, on_delete=models.CASCADE, related_name='director_movies')

    starring_actor = models.ForeignKey(to=Actor,
                                       null=True,
                                       blank=True,
                                       on_delete=models.SET_NULL,
                                       related_name='starring_actor_movies')

    actors = models.ManyToManyField(to=Actor, related_name='actor_movies')
