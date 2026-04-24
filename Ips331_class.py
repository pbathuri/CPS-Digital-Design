#/usr/bin/env python3

import smbus
import sys
import numpy as np
import time

addr = 0x5d
bus = smbus.SMBus(1)
class lps331:
    ''' allows connection from Raspberry pi to I2C connected lps331 '''

    def __init__(self,raspberry_pi_i2c_port=1):
        self.i2c_port_number = raspberry_pi_i2c_port
        self.bus = smbus.SMBus(self.i2c_port_number)
        self.address = self.find_sensor()
        #self.address = addr
        if (self.address == -1):
            print("Error: could not read from sensor at i2c address 0x5d")
            sys.exit()
        self.enable_sensor()
        
    def find_sensor(self):
        
        ''' read the whoami byte from i2c address 0x5d and confirm to be 0xbb '''
        # Return the address if found (0x5d) and 0 if not found
       
        address = bus.read_byte_data(0x5d, 0x0f)
        # @@@@ Your Code Here @@@@ 
        if address == 0xbb:
            return 0x5d
        else:
            0

        pass   # if the sensor was not located on either bus, return -1

    def i2c_address(self):
        return(self.address)

    def sample_once(self):
        ''' Cause the sensor to sample one time '''
        # @@@@ Your Code Here @@@@ 
        ctrl_reg2 = bus.read_byte_data(self.address,0x21)
        bus.write_byte_data(self.address,0x21,0x01|ctrl_reg2) 
        
        ctrl_reg2 = bus.read_byte_data(self.address,0x21)
#        while (ctrl_reg2&0x01):
 #           ctrl_reg2 = bus.read_byte_data(self.address,0x21)

        pass
        
    def read_temperature(self):
        ''' Sample, read temperature registers, and convert to Degrees C ''' 
        tempC = 0
        self.sample_once()
        temp_out_low = bus.read_byte_data(self.address, 0x2b) 
        temp_out_high = bus.read_byte_data(self.address, 0x2c)
        
        data = (temp_out_high<<8) | temp_out_low
        if data > 2**15:
            data -= 2**16
        tempC = 42.5 + (data)/480
         
        # @@@@ Your Code Here @@@@ 
        
        return(tempC)

    def read_pressure(self):
        ''' Sample, read pressure registers, and convert to inhg ''' 
        press_inhg = 0
        
        # @@@@ Your Code Here @@@@ 
        self.sample_once()
        press_out_h = bus.read_byte_data(self.address, 0x2a)
        press_out_l = bus.read_byte_data(self.address, 0x29)
        press_out_xl = bus.read_byte_data(self.address, 0x28)

        press_inhg = ((press_out_h<<16) | (press_out_l<<8) | (press_out_xl))/4096
        press_inhg = press_inhg/33.864
        return(press_inhg)
    
    def enable_sensor(self):
        ''' Turn on sensor in control register 1'''

        # @@@@ Your Code Here @@@@ 
        ctrl_reg1 = bus.read_byte_data(self.address,0x20)
        bus.write_byte_data(self.address,0x20,0x80|ctrl_reg1)
        pass
    
    def disable_sensor(self):
        ''' Turn off sensor in control register 1 '''

        # @@@@ Your Code Here @@@@ 
        ctrl_reg1 = bus.read_byte_data(self.address,0x20)
        bus.write_byte_data(self.address,0x20,0x80|ctrl_reg1) 
        pass
        
    def close(self):
        ''' Disable the sensor and close connection to i2c port '''
        self.disable_sensor()
        self.bus.close()
       
if  __name__ == "__main__":
    sensor = lps331(1)
    print("Temperature = %0.2f Deg C "%(sensor.read_temperature()))
    print("Pressure = %0.2f inHg"%(sensor.read_pressure()))
    sensor.close()
