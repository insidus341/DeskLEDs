from run.homeassistant_connection import HomeAssistant
from dotenv import load_dotenv
import pytest
import os
import json

load_dotenv('./run/configuration.txt')

HOMEASSISTANT_IP = str(os.getenv('HOMEASSISTANT_IP'))
HOMEASSISTANT_PORT = int(os.getenv('HOMEASSISTANT_PORT'))
HOMEASSISTANT_PROTOCOL = str(os.getenv('HOMEASSISTANT_PROTOCOL'))
HOMEASSISTANT_API_TOKEN = str(os.getenv('HOMEASSISTANT_API_TOKEN'))
HOMEASSISTANT_LIGHT_ID = str(os.getenv('HOMEASSISTANT_LIGHT_ID'))
HOMEASSISTANT_LIGHT_BRIGHTNESS = int(os.getenv('HOMEASSISTANT_LIGHT_BRIGHTNESS'))

def create_homeassistant_class():
    homeassistant = HomeAssistant(
        HOMEASSISTANT_IP,
        HOMEASSISTANT_PORT,
        HOMEASSISTANT_PROTOCOL,
        HOMEASSISTANT_API_TOKEN,
        HOMEASSISTANT_LIGHT_ID,
        HOMEASSISTANT_LIGHT_BRIGHTNESS
    )

    return homeassistant

def create_homeassistant_bad_class():
    homeassistant = HomeAssistant(
        '1.2.3.4',
        HOMEASSISTANT_PORT,
        HOMEASSISTANT_PROTOCOL,
        HOMEASSISTANT_API_TOKEN,
        HOMEASSISTANT_LIGHT_ID,
        HOMEASSISTANT_LIGHT_BRIGHTNESS
    )

    return homeassistant

def test_homeassistant_connection_create_homeassistant_class():
    try:
        create_homeassistant_class()
    except:
        pytest.fail("Unable to create the Home Assistant class")

def test_homeassistant_confirm_connection_to_homeassistant_server_no_exception():
    try:
        ha = create_homeassistant_class()
    except:
        pytest.fail("Unable to succesfully connect to the Home Assistant server")

def test_homeassistant_confirm_connection_to_homeassistant_server_json():
    ha = create_homeassistant_class()
    response = ha.confirm_connection_to_homeassistant_server()
    assert response['message'] == 'API running.'

def test_homeassistant_confirm_connection_to_homeassistant_server_json_bad():
    ha = create_homeassistant_bad_class()
    try:
        response = ha.confirm_connection_to_homeassistant_server()
        pytest.fail("Unable to succesfully connect to the Home Assistant server")    
    except:
        assert True

def test_homeassistant_get_current_light_state_no_exception():
    ha = create_homeassistant_class()
    try:
        ha.get_current_light_state()
    except:
        pytest.fail("Unable to get current light state")

def test_homeassistant_get_current_light_state_json():
    ha = create_homeassistant_class()
    response = ha.get_current_light_state()
    assert response['entity_id'] == HOMEASSISTANT_LIGHT_ID

def test_homeassistant_set_new_light_color():
    ha = create_homeassistant_class()
    rgb = (100,100,100)
    try:
        ha.set_new_light_color(rgb)
        assert True
    except:
        assert False
