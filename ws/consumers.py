import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class CommunicationConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def connect(self):
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            "1", self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            "1", self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        async_to_sync(self.channel_layer.group_send)(
            "1", text_data_json
        )

    # Receive message from room group
    def action(self, event):
        # Send message to WebSocket
        self.send(text_data=json.dumps(event))
