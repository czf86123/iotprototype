# -*- coding: utf-8 -*-
"""
to be deleted
"""
import paho.mqtt.client as mqtt


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flag, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("msg_to_server")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + ':' + str(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
#
# client.connect('127.0.0.1', 1883, 60)
#
# client.loop_forever()