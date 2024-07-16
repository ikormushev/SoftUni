from django.db import models


class AnimalsChoices(models.TextChoices):
    MAMMALS = "Mammals", "Mammals"
    BIRDS = "Birds", "Birds"
    REPTILES = "Reptiles", "Reptiles"
    OTHERS = "Others", "Others"
