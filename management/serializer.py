from django.contrib.auth.models import User, Group
from rest_framework import serializers

from game.models import Deck
from game.serializer import Cardserializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        instance = self.Meta.model.objects.create_user(**validated_data)
        Deck.objects.create(user=instance)
        return instance


class GroupOfCards(serializers.Serializer):
    cards = Cardserializer(many=True)
