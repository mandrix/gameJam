from django.contrib.auth.models import User, Group
from rest_framework import serializers

from game.models import (
    Card,
    Deck
)

class Cardserializer(serializers.ModelSerializer):

    class Meta:
            model = Card
            fields = '__all__'