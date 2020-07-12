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
    load_dotenv('configuration.txt')

    HOMEASSISTANT_IP = str(os.getenv('HOMEASSISTANT_IP'))
    HOMEASSISTANT_PORT = int(os.getenv('HOMEASSISTANT_PORT'))
    HOMEASSISTANT_PROTOCOL = str(os.getenv('HOMEASSISTANT_PROTOCOL'))
    HOMEASSISTANT_API_TOKEN = str(os.getenv('HOMEASSISTANT_API_TOKEN'))
    HOMEASSISTANT_LIGHT_ID = str(os.getenv('HOMEASSISTANT_LIGHT_ID'))
    HOMEASSISTANT_LIGHT_BRIGHTNESS = int(os.getenv('HOMEASSISTANT_LIGHT_BRIGHTNESS'))

    MONLIGHT_SCREEN_NUMBER = int(os.getenv('MONLIGHT_SCREEN_NUMBER'))
    MONLIGHT_ANALYZE_ENTIRE_SCREEN = bool(os.getenv('MONLIGHT_ANALYZE_ENTIRE_SCREEN'))

except Exception as e:
    print('There is an error in the configuration file')
    print(e) # Print the error
    exit()
    

# def update_light_color(red, green, blue):
#     print(red)
#     url = f"{HOMEASSISTANT_PROTOCOL}://{HOMEASSISTANT_IP}:{HOMEASSISTANT_PORT}/api/services/light/turn_on"
#     data = {
#         "entity_id": HOMEASSISTANT_LIGHT_ID,
#         "rgb_color": [
#             red,
#             green,
#             blue
#         ],
#         "brightness": HOMEASSISTANT_LIGHT_BRIGHTNESS
#     }

#     response = requests.post(url, json=data, headers=headers, verify=False)
#     print(response.status_code)

if __name__ == "__main__":

    monitor = Monitor(1)  
    print(monitor.get_monitor_id())
    print(monitor.get_monitor_bounding_box())
    print(monitor.get_monitor_average_color())

    homeassistant = HomeAssistant(
        HOMEASSISTANT_IP,
        HOMEASSISTANT_PORT,
        HOMEASSISTANT_PROTOCOL,
        HOMEASSISTANT_API_TOKEN,
        HOMEASSISTANT_LIGHT_ID,
        HOMEASSISTANT_LIGHT_BRIGHTNESS
    )

    homeassistant.confirm_connection_to_homeassistant_server()
    homeassistant.get_current_light_state()
    homeassistant.set_new_light_color((0, 100, 200))
    exit()

    while(True):
        
        sleep(5)