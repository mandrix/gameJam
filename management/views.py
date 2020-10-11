from itertools import count
from random import random, randint

from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from management.serializer import UserSerializer, GroupOfCards
from management.models import (
    Province,
    Location,
)
from game.models import (
    Deck,
    Card
)


# Create your views here.

class RegisterView(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    serializer_class = UserSerializer


class UserView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_active=True)


class OpenPack(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = GroupOfCards

    def update(self, request, *args, **kwargs):
        if id_user := request.user.id:
            user = User.objects.filter(id=id_user).first()
            location = Location.objects.filter(name=request.data.get("code")).first()
            deck_normal = location.cards
            deck_legend = location.province.cards
            c = count(-3)
            data = {"cards": []}
            while next(c):
                new_card = self.obtainACard(deck_normal, deck_legend)
                user.deck.cards.add(new_card)  # TODO validar si se tiene la carta en el deck
                data["cards"].append(
                    {
                        "name": new_card.name,
                        "description": new_card.description,
                        "img": new_card.img,
                        "rarity": new_card.rarity,
                        "background": new_card.background,
                        "label": new_card.label
                    }
                )
            user.save()
            serializer = GroupOfCards(data=data)
            if serializer.is_valid():
                return Response(serializer.data)
            return Response(serializer.errors)

    def obtainACard(self, deck_normal, deck_legend):
        if randint(0, 3):  # TODO aumentar el rango para bajar la % de legend
            return deck_normal.all()[randint(0, deck_normal.count() - 1)]
        else:
            return deck_legend.all()[randint(0, deck_legend.count() - 1)]
