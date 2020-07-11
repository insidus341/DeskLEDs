from PIL import Image, ImageGrab
from time import sleep
from screeninfo import get_monitors
import requests


def get_monitor_middle():
    mon = get_monitors()[1]
    width = mon.width
    height = mon.height

    return (width, height)

def get_bounding_box_top_left(offset = 100):
    (mon_width, mon_height) = get_monitor_middle()
    box_top_left = ((mon_width / 2) - (offset), (mon_height / 2 - offset))
    return box_top_left

def get_bounding_box_bottom_right(offset = 100):
    (mon_width, mon_height) = get_monitor_middle()
    box_bottom_right = ((mon_width / 2) + (offset), (mon_height / 2 + offset))
    return box_bottom_right

def get_bounding_box():
    offset = 200
    box_top_left = get_bounding_box_top_left(offset)
    box_bottom_right = get_bounding_box_bottom_right(offset)

    bbox = (box_top_left[0], box_top_left[1], box_bottom_right[0], box_bottom_right[1])
    return bbox
    

def get_screen_avg_color():
    im = ImageGrab.grab(bbox=get_bounding_box())
    pix_list = list(im.getdata())

    pixel_count = 0
    red_count = 0
    red_avg = 0
    green_count = 0
    green_avg = 0
    blue_count = 0
    blue_avg = 0


    for pixel in pix_list:
        red_count += pixel[0]
        green_count += pixel[1]
        blue_count += pixel[2]

        pixel_count += 1

    red_avg = int(red_count / pixel_count)
    green_avg = int(green_count / pixel_count)
    blue_avg = int(blue_count / pixel_count)

    print(f"r: {red_avg}, g: {green_avg}, b: {blue_avg}")
    update_light_color(red_avg, green_avg, blue_avg)



def update_light_color(red, green, blue):
    print(red)
    url = "https://192.168.0.33:8123/api/services/light/turn_on"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJlM2QzMTE3Yjc2ZDc0NDlhOWQ2Y2ZmYTVmOGI2YTMzNyIsImlhdCI6MTU5NDQwNzIyMywiZXhwIjoxOTA5NzY3MjIzfQ.BXio1s_hBuDZ6Is0HxkoMa3yfR823_HINKApUeOABUw"
    }
    data = {
        "entity_id": "light.sofa_led",
        "rgb_color": [
            red,
            green,
            blue
        ],
        "brightness": 120
    }

    response = requests.post(url, json=data, headers=headers, verify=False)
    print(response.status_code)

if __name__ == "__main__":
    while(True):
        get_screen_avg_color()
        sleep(5)