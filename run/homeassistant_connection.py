import requests
import json

from abc import ABC, abstractmethod

class HomeAssistantABC(ABC):

    def __init__(self, HOMEASSISTANT_IP, 
    HOMEASSISTANT_PORT, 
    HOMEASSISTANT_PROTOCOL, 
    HOMEASSISTANT_API_TOKEN,
    HOMEASSISTANT_LIGHT_ID,
    HOMEASSISTANT_LIGHT_BRIGHTNESS):
        self.HOMEASSISTANT_IP = HOMEASSISTANT_IP
        self.HOMEASSISTANT_PORT = HOMEASSISTANT_PORT
        self.HOMEASSISTANT_PROTOCOL = HOMEASSISTANT_PROTOCOL
        self.HOMEASSISTANT_API_TOKEN = HOMEASSISTANT_API_TOKEN
        self.HOMEASSISTANT_LIGHT_ID = HOMEASSISTANT_LIGHT_ID
        self.HOMEASSISTANT_LIGHT_BRIGHTNESS = HOMEASSISTANT_LIGHT_BRIGHTNESS

    @abstractmethod
    def confirm_connection_to_homeassistant_server(self):
        pass

    @abstractmethod
    def get_current_light_state(self):
        pass

    @abstractmethod
    def set_new_light_color(self):
        pass


class HomeAssistant(HomeAssistantABC):

    def __get_rest_headers(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.HOMEASSISTANT_API_TOKEN}"
        }
        return headers

    def __get_base_url(self):
        base_url = f"{self.HOMEASSISTANT_PROTOCOL}://{self.HOMEASSISTANT_IP}:{self.HOMEASSISTANT_PORT}/api/"
        return base_url      

    def __confirm_good_rest_response(self, response):
        if response.status_code == '427':
            print("Home Assistant threw a timeout, please wait 10 seconds before trying again")
        if response.status_code != 200:
            print(f"Did not receive a HTTP/200 from {self.HOMEASSISTANT_IP}")
            raise ValueError

    def __run_rest_get(self, url):
        headers = self.__get_rest_headers()
        response = requests.get(url, headers=headers, verify=False)
        self.__confirm_good_rest_response(response)
        return response.json()

    def __run_rest_post(self, url, payload):
        headers = self.__get_rest_headers()
        response = requests.post(url, json=payload, headers=headers, verify=False)
        self.__confirm_good_rest_response(response)

    def confirm_connection_to_homeassistant_server(self):
        url = self.__get_base_url()
        response = self.__run_rest_get(url)  
        return response

    def get_current_light_state(self):
        url = f"{self.__get_base_url()}states/{self.HOMEASSISTANT_LIGHT_ID}"
        response = self.__run_rest_get(url)
        return response

    def set_new_light_color(self, rgb):
        url = f"{self.__get_base_url()}services/light/turn_on"
        payload = {
            "entity_id": self.HOMEASSISTANT_LIGHT_ID,
            "rgb_color": [
                        rgb[0],
                        rgb[1],
                        rgb[2]
                    ],
            "brightness": self.HOMEASSISTANT_LIGHT_BRIGHTNESS
        }
        print(payload)

        try:
            self.__run_rest_post(url, payload)
        except:
            print(f"Failed to update {self.HOMEASSISTANT_LIGHT_ID}")
