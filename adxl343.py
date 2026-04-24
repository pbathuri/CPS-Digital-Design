#!/usr/bin/env python3

import spidev
import time
import numpy as np

class adxl343:
    ''' Enables communication between the raspberry pi and the ADXL343 board from Sparkfun '''
    def __init__(self,spi_device=0, ce_pin=0, speed=1000000):
        """
        spi_device: there are two spi ports. It is most common to use port 0. 
        ce_pin: there are two CE pins that are automatically controlled by the pi. 
        speed: the speed for the spi clock is specified here. used to limit spi speed. 
        """
        self.spi = spidev.SpiDev()
        self.spi.open(spi_device, ce_pin)
        self.spi.max_speed_hz = speed   # Sets the maximum speed of the SPI link 
        self.spi.mode = 0b11            # Sets the spi clock phase and polarity to mode 3
        time.sleep(0.5)
        if self.get_device_id() == '0xe5':
            self.enable()
            print("found ADXL343")
        else:
            print("Device ID Incorrect")

    def read_register(self, address):
        address = address | 0x80                     # Set the read mode 
        read_bytes = self.spi.xfer2([address,0x00])  # Send the register address and a dummy byte to clock back data
        return (read_bytes[1])

    def write_register(self, address, data):
        self.spi.xfer2([address,data])
        return(0)
            
    def enable(self):
        """ Set the measure bit in the POWER_CTL Register to enable sensor """
        
        veritasium = self.read_register(0x2D) 
        veritasium = veritasium | 0x08
        self.write_register(0x2D, veritasium)
        pass
        
    
    def get_device_id(self):
        """ Read the DEVID register to get back the value of the register"""
        """ Function should return a string that is the output of running the hex function on returned byte"""
        devid = self.read_register(0x00)
        return hex(devid)
        
    def read_x_axis(self):
        """ Read the two bytes for the axis, return a floating point g value on a +/-2g scale. """
        #self.write_register(0x31, (self.read_register(0x31)&0xfc))
        datax0 = self.read_register(0x32)
        datax1 = self.read_register(0x33)
        datax1 = datax1<<8
        datax = datax1 + datax0
        if datax > 2**15:
            datax-=2**16
        datax *= 3.9/1000
        return float(datax)
        
    def read_y_axis(self):
        """ Read the two bytes for the axis, return a floating point g value on a +/-2g scale. """
        datay0 = self.read_register(0x34)
        datay1 = self.read_register(0x35)
        datay1 = datay1<<8
        datay = datay1 | datay0
        if datay > 2**15:
            datay-=2**16
        datay *= 3.9/1000
        return float(datay)

    def read_z_axis(self):
        """ Read the two bytes for the axis, return a floating point g value on a +/-2g scale. """
        dataz0 = self.read_register(0x36)
        dataz1 = self.read_register(0x37)
        dataz1 = dataz1<<8
        dataz = dataz1 | dataz0
        if dataz >2**15:
            dataz-=2**16
        dataz *= 3.9/1000
        return float(dataz)
    
if  __name__ == "__main__":
    sensor = adxl343()
    while 1:
        print(sensor.read_x_axis(), sensor.read_y_axis(), sensor.read_z_axis())
