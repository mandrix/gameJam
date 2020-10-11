from django.contrib.auth.models import User, Group
from rest_framework import serializers
from game.serializer import Cardserializer



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        instance = self.Meta.model.objects.create_user(**validated_data)
        return instance


class ObtainedCards(serializers.Serializer):
    cards = Cardserializer(many=True)
