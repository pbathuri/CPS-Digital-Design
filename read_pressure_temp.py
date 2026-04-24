#!/usr/bin/env python3

import smbus
import sys
import time
import numpy as np

# Open I2C port 1
bus = smbus.SMBus(1)

# Pressure Sensor Address 
address = 0x5d

# Read, modify, and the write back control register 1.
# Notice that bit 7 is being "or"ed to a value of 1. 
ctrl_reg1 = bus.read_byte_data(address,0x20)
bus.write_byte_data(address,0x20,0x80|ctrl_reg1) 

# Show the old values for pressure and temperature
press_xl = bus.read_byte_data(address,0x28)
press_l = bus.read_byte_data(address,0x29)
press_h= bus.read_byte_data(address,0x2a)
print("Old Pressure Bytes 0x%02x 0x%02x 0x%02x"%(press_h,press_l,press_xl))
temp_l = bus.read_byte_data(address,0x2b)
temp_h = bus.read_byte_data(address,0x2c) 
print("Old Temperature Bytes 0x%02x 0x%02x"%(temp_h,temp_l))

# Write Control Register 2 to cause the sensor to sample
ctrl_reg2 = bus.read_byte_data(address,0x21)
bus.write_byte_data(address,0x21,0x01|ctrl_reg2) 
ctrl_reg2 = bus.read_byte_data(address,0x21)

# Poll until the bit that was set control register 2 is cleared. 
while (ctrl_reg2&0x01):
    ctrl_reg2 = bus.read_byte_data(address,0x21)

# Read the pressure and temperature again to get the new values 
press_xl = bus.read_byte_data(address,0x28)
press_l = bus.read_byte_data(address,0x29)
press_h= bus.read_byte_data(address,0x2a)
print("New Pressure Bytes 0x%02x 0x%02x 0x%02x"%(press_h,press_l,press_xl))
temp_l = bus.read_byte_data(address,0x2b)
temp_h = bus.read_byte_data(address,0x2c) 
print("New Temperature Bytes 0x%02x 0x%02x"%(temp_h,temp_l))
bus.close()
