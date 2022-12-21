from channels.generic.websocket import JsonWebsocketConsumer

# it's used to show user's online status and send notificatin
class ChatConsumer(JsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.room_name = None

    def connect(self):
        print("Connected!")
        self.room_name = "home"
        self.accept()
        self.send_json(
            {
                "type": "welcome_message",
                "message": "Hey there! You've successfully connected!",
            }
        )

    def disconnect(self, code):
        print("Disconnected!")
        return super().disconnect(code)
    
    def receive_json(self, content, **kwargs):
        print(content)
        return super().receive_json(content, **kwargs)