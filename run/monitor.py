from screeninfo import get_monitors
from PIL import Image, ImageGrab

class Monitor():

    def __init__(self, monitor_number = 1):
        self.monitor_number = monitor_number
        self.select_monitor()
        self.monitor_bbox_offset = 100

    def __get_monitor_details_id(self):
        def function_wrapper(self):
            return self.monitor_number

        return function_wrapper
    
    @__get_monitor_details_id
    def get_monitor_id(self):
        pass

    def select_monitor(self):
        available_monitors = get_monitors()
        selected_monitor = available_monitors[self.get_monitor_id() - 1]
        self.selected_monitor = selected_monitor

    def get_monitor_bounding_box(self):
        try: 
            bbox_top_left = self.get_monitor_bounding_box_top_left()
            bbox_bottom_right = self.get_monitor_bounding_box_bottom_right()

            monitor_bbox = (bbox_top_left[0], bbox_top_left[1], bbox_bottom_right[0], bbox_bottom_right[1])
            return monitor_bbox

        except IndexError as e:
            print("Selected monitor does not exist")
            raise Exception
        except Exception as e:
            print("There was an error selecting the monitor")
            print(e)
            raise Exception

    def get_monitor_bounding_box_top_left(self):
        mon_width = self.selected_monitor.width
        mon_height = self.selected_monitor.height
        bbox_top_left = ((mon_width / 2) - (self.monitor_bbox_offset), (mon_height / 2 - self.monitor_bbox_offset))

        # print(type(bbox_top_left))
        # print(isinstance(bbox_top_left, tuple))
        return bbox_top_left

    def get_monitor_bounding_box_bottom_right(self):
        mon_width = self.selected_monitor.width
        mon_height = self.selected_monitor.height
        bbox_bottom_right = ((mon_width / 2) + (self.monitor_bbox_offset), (mon_height / 2 + self.monitor_bbox_offset))

        return bbox_bottom_right

    def get_pixel_list(self):
        try: 
            im = ImageGrab.grab(bbox=self.get_monitor_bounding_box())
            pixel_list = list(im.getdata())
            return pixel_list

        except Exception as e:
            print('Unable to read the screen pixels')
            raise Exception

    def get_monitor_average_color(self):
        pixel_list = self.get_pixel_list()
        
        # Create our pixel variables
        pixel_count = 0

        # pixel counts per color
        red_count = 0
        green_count = 0
        blue_count = 0
        
        # Color averages
        red_avg = 0
        green_avg = 0
        blue_avg = 0

        # Work out the color counts
        for pixel in pixel_list:
            red_count += pixel[0]
            green_count += pixel[1]
            blue_count += pixel[2]

            pixel_count += 1
        
        # Work out the color averages
        red_avg = int(red_count / pixel_count)
        green_avg = int(green_count / pixel_count)
        blue_avg = int(blue_count / pixel_count)

        if True: # TODO add a debug option
            print(f"r: {red_avg}, g: {green_avg}, b: {blue_avg}")
        
        monitor_rgb = (red_avg, green_avg, blue_avg)
        return monitor_rgb