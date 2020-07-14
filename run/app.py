from time import sleep
from dotenv import load_dotenv

import os
import urllib3

# import the monitor class
from monitor import Monitor

# import the home assistant connection class
from homeassistant_connection import HomeAssistant

# Surpress SSL self signed certificate warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Import our system variables and check their type()
try: 
    load_dotenv('./run/configuration.txt')
    HOMEASSISTANT_IP = str(os.getenv('HOMEASSISTANT_IP'))

except Exception as e:
    print('There is no configuration file. Loading from envrionmentals instead')

finally:
    HOMEASSISTANT_IP = str(os.getenv('HOMEASSISTANT_IP'))
    HOMEASSISTANT_PORT = int(os.getenv('HOMEASSISTANT_PORT'))
    HOMEASSISTANT_PROTOCOL = str(os.getenv('HOMEASSISTANT_PROTOCOL'))
    HOMEASSISTANT_API_TOKEN = str(os.getenv('HOMEASSISTANT_API_TOKEN'))
    HOMEASSISTANT_LIGHT_ID = str(os.getenv('HOMEASSISTANT_LIGHT_ID'))
    HOMEASSISTANT_LIGHT_BRIGHTNESS = int(os.getenv('HOMEASSISTANT_LIGHT_BRIGHTNESS'))

    MONLIGHT_SCREEN_NUMBER = int(os.getenv('MONLIGHT_SCREEN_NUMBER'))
    MONLIGHT_ANALYZE_ENTIRE_SCREEN = bool(os.getenv('MONLIGHT_ANALYZE_ENTIRE_SCREEN'))
    MONLIGHT_TIMER = float(os.getenv('MONLIGHT_TIMER'))


if __name__ == "__main__":

    monitor = Monitor(MONLIGHT_SCREEN_NUMBER)  
    homeassistant = HomeAssistant(
        HOMEASSISTANT_IP,
        HOMEASSISTANT_PORT,
        HOMEASSISTANT_PROTOCOL,
        HOMEASSISTANT_API_TOKEN,
        HOMEASSISTANT_LIGHT_ID,
        HOMEASSISTANT_LIGHT_BRIGHTNESS
    )

    while(True):
        rgb = monitor.get_monitor_average_color()
        homeassistant.set_new_light_color(rgb)
        sleep(MONLIGHT_TIMER)
