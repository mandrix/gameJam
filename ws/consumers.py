import json
from asgiref.sync import async_to_sync, sync_to_async
from channels.db import database_sync_to_async
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from django.contrib.auth.models import User
from django.db.models import Q

from management.serializer import GroupOfCards
from ws.models import Session


@database_sync_to_async
def get_user(_id):
    return User.objects.filter(id=_id)


class CommunicationConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        self.user = None
        self.user_id = None
        self.opponent_id = None
        self.session = None
        self.user1 = None
        super().__init__(*args, **kwargs)

    async def connect(self):
        self.user_id = self.scope["url_route"]["kwargs"]["user_id"]
        await self.channel_layer.group_add(
            self.user_id, self.channel_name
        )
        # await self.add_to_session()
        user = await get_user(self.user_id)
        user = user.first()
        self.user = user

        Session.objects.filter(
            Q(user1_id=self.user_id) | Q(user2_id=self.user_id)
        ).delete()

        if user:
            if session := Session.objects.filter(user2=None).first():
                session.user2 = user
                session.save()
                self.user1 = False
            else:
                session = Session.objects.create(
                    user1=user
                )
                self.user1 = True
            self.session = session

        else:
            await self.close()
        await self.accept()

    # async def add_to_session(self):

    async def disconnect(self, close_code):
        # Leave room group
        if session := Session.objects.filter(
                Q(user1_id=self.user_id) | Q(user2_id=self.user_id)
        ).first():
            session.delete()
        await self.channel_layer.group_discard(
            self.user_id, self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        if text_data_json.get("search"):
            session = Session.objects.filter(
                Q(user1_id=self.user_id) | Q(user2_id=self.user_id)
            ).first()
            player_serializer = GroupOfCards(self.user.deck)
            if session.user1 and session.user2:
                opponent = session.user1 if not self.user1 else session.user2
                self.opponent_id = opponent.pk
                opponent_serializer = GroupOfCards(opponent.deck)
                await self.channel_layer.group_send(
                    self.user_id, {
                        "opponent": {
                            "name": opponent.username,
                            "deck": opponent_serializer.data
                        },
                        "player": {
                            "name": self.user.username,
                            "deck": player_serializer.data
                        },
                        "type": "action"
                    }
                )
            else:
                await self.channel_layer.group_send(
                    self.user_id, {
                        "opponent": "Not found",
                        "player": {
                            "name": self.user.username,
                            "deck": player_serializer.data
                        },
                        "type": "action"
                    }
                )

            # async_to_sync(self.channel_layer.group_send)(
            #     "1", text_data_json
            # )

    # Receive message from room group
    async def action(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps(event))
