#type: ignore
from microbit import *
import utime

# 1. Initialize Communication (Important!)
# This opens the USB 'pipe' so the laptop can talk back.
uart.init(baudrate=115200) # Fast enough for my current needs, but can be adjusted if necessary.

# Pins for the Elecfreaks Smart Agriculture Kit
SOIL_PIN = pin1
PUMP_PIN = pin2
TEMP_PIN = pin8 

def get_moisture():
    return SOIL_PIN.read_analog()

def get_temp():
    return temperature()

while True:
    # 2. Collect Real Metabolic Data
    moisture = get_moisture()
    temp = get_temp()
    
    # 3. Send to Laptop Brain (Format: MOISTURE,TEMP)
    print(str(moisture) + "," + str(temp))
    
    # 4. Listen for 'PUMP_ON' command from the Brain
    if uart.any():
        data = uart.read().decode().strip()
        if "PUMP_ON" in data:
            PUMP_PIN.write_digital(1)
            display.show(Image.WATER_DROP)
            utime.sleep_ms(2000) # Water for 2 seconds
            PUMP_PIN.write_digital(0)
            display.clear()
            
    utime.sleep_ms(1000) 
