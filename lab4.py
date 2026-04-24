#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time

# White Bar Code Label Number on Each Raspberry Pi
sensor_id = None #YOUR PI SERIAL NUMBER
temperature = 21
pressure = 31
x_acceleration = 0.001
y_acceleration = 0.002
z_acceleration = 1.001

def on_message(client, userdata, message):
#    print("topic:", message.topic)
    print("message:", message.payload.decode('UTF-8'))

def on_connect(client,userdata,flags,rc):
    pass
    
client = mqtt.Client()
client.on_message=on_message
client.on_connect=on_connect
client.connect("pivot.iuiot.org")
client.loop_start()
while(1):
    print("Publish Temperature, Pressure, and Accelerometer Data")
    client.publish(f"sensors/{sensor_id}/temperature",f"{temperature}")
    client.publish(f"sensors/{sensor_id}/pressure",f"{pressure}")
    client.publish(f"sensors/{sensor_id}/accel/x",f"{x_acceleration}")
    client.publish(f"sensors/{sensor_id}/accel/y",f"{y_acceleration}")
    client.publish(f"sensors/{sensor_id}/accel/z",f"{z_acceleration}")
    time.sleep(5)
