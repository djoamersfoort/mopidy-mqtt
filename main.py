import paho.mqtt.client as mqtt
import os

class Daemon:
    def __init__(self,
        host="mqtt.bitlair.nl",
        topic="bitlair/switch/state/djo",
        keyword="open"):

        self.client = mqtt.Client()
        self.client.on_message = self.on_message

        self.host = host
        self.topic = topic
        self.keyword = keyword

        self.status = None
    
    def connect(self):
        self.client.connect(self.host)
        self.client.subscribe(self.topic)

        self.client.loop_forever()


    def on_message(self, _c, _u, msg):
        if msg.topic == self.topic:
            payload = msg.payload.decode("utf-8") == self.keyword

            if self.status != payload:
                self.status = payload
                print(f"{self.keyword} is {'open' if self.status else 'closed'}")

                self.handle_change()
    
    def handle_change(self):
        command = f"systemctl {'start' if self.status else 'stop'} mopidy"
        print(f"Running systemctl command: {command}")
        os.system(command)

if __name__ =="__main__":
    daemon = Daemon()
    daemon.connect()