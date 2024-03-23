import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected")


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "test1")

client.on_connect = on_connect

client.connect("localhost", 1883)

client.loop_start()

while True:
    moisture = 350
    client.publish("moisture", moisture)
    time.sleep(3)

client.loop_stop()