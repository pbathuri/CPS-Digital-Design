#!/usr/bin/env python3

import smbus

# Open I2C port 1
bus = smbus.SMBus(1)

# Read register 0x0f from the device at address 0x5d (recall address from i2cdetect)
data = bus.read_byte_data(0x5d,0x0f)

if (data == 0xbb):
    print("Found Sensor")
else:
    print("Received %d from the sensor"%(data))

bus.close()
