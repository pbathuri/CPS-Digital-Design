#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
import adxl343
import Ips331_class

# White Bar Code Label Number on Each Raspberry Pi
sensor_id = 986292
temperature = 21
pressure = 31
x_acceleration = 0.001
y_acceleration = 0.002
z_acceleration = 1.001

def on_message(client, userdata, message):
    print("topic:", message.topic)
    print("message:", message.payload.decode('UTF-8'))

    adx1343.read(accelerometer)
    Ips331_class

def on_connect(client,userdata,flags,rc):
     if rc == 0:
        print("Connected successfully")
        # Subscribing here ensures it happens on every reconnect
        client.subscribe("home/sensors")
     else:
        print(f"Connection failed with code {rc}")
     pass
    
client = mqtt.Client()
client.on_message=on_message
client.on_connect=on_connect
client.connect("pivot.iuiot.org")
client.loop_start()

ips = Ips331_class.lps331(1)
acc = adxl343.adxl343()

while(1):
    print("Publish Temperature, Pressure, and Accelerometer Data")
    temperature = ips.read_temperature()
    pressure = ips.read_pressure()
    x_acceleration = acc.read_x_axis()
    y_acceleration = acc.read_y_axis()
    z_acceleration = acc.read_z_axis()
    client.publish(f"sensors/{sensor_id}/temperature",f"{temperature}")
    client.publish(f"sensors/{sensor_id}/pressure",f"{pressure}")
    client.publish(f"sensors/{sensor_id}/accel/x",f"{x_acceleration}")
    client.publish(f"sensors/{sensor_id}/accel/y",f"{y_acceleration}")
    client.publish(f"sensors/{sensor_id}/accel/z",f"{z_acceleration}")
    time.sleep(5)
