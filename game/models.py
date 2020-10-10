from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Card(models.Model):
    categories_choices = [
        ("UB", "Ubicación"),
        ("HR", "Heroe")
    ]

    background_img_choice = [
        ("blue", "src"),
        ("green", "src")
    ]

    rarity_choice = [
        ("LGN", "legend"),
        ("BS" ,"basic")
    ]

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    img = models.ImageField(upload_to="game/")

    rarity = models.CharField(
        max_length=3,
        choices=rarity_choice,
        default="BS",
    )

    background = models.CharField(
        max_length=5,
        choices=background_img_choice,
        default="blue",
    )

    label = models.CharField(
        max_length=2,
        choices=categories_choices,
        default="a",
    )


    def __str__(self):
        return self.name

class Deck(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="Deck"
    )
    cards = models.ManyToManyField(Card, blank=True)


    def __str__(self):
        return self.user.name