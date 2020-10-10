from django.contrib import admin
from game.models import Card
# Register your models here.

class CardAdmin(admin.ModelAdmin):
    model = Card

admin.register(Card, CardAdmin)