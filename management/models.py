import uuid

from django.db import models
from game.models import Card

# Create your models here.
class Province(models.Model):
    """
    place where legendary cards will be
    """
    name = models.CharField(max_length=100)
    cards = cards = models.ManyToManyField(Card, blank=True)


    def __str__(self):
        return self.name

class Location(models.Model):
    """
    this place will have a unique province
    place where any cards will be
    """
    name = models.UUIDField(default=uuid.uuid4, unique=True)
    cards = models.ManyToManyField(Card, blank=True)
    province = models.OneToOneField(
        Province, on_delete=models.CASCADE, related_name="province"
    )


    def __str__(self):
        return str(self.name)