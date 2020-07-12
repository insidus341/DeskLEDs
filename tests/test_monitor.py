from run.monitor import Monitor

MONITOR_ID = 1

def test_monitor_get_monitor_id():
    monitor = Monitor(MONITOR_ID)
    assert monitor.get_monitor_id() == MONITOR_ID

def test_monitor_get_monitor_middle():
    monitor = Monitor(MONITOR_ID)
    assert isinstance(monitor.get_monitor_bounding_box(), tuple)

def test_monitor_get_monitor_bounding_box_top_left_tuple():
    monitor = Monitor(MONITOR_ID)
    assert isinstance(monitor.get_monitor_bounding_box_top_left(), tuple)

def test_monitor_get_monitor_bounding_box_top_left_len():
    monitor = Monitor(MONITOR_ID)
    assert len(monitor.get_monitor_bounding_box_top_left()) == 2

def test_monitor_get_monitor_bounding_box_bottom_right_tuple():
    monitor = Monitor(MONITOR_ID)
    assert isinstance(monitor.get_monitor_bounding_box_bottom_right(), tuple)

def test_monitor_get_monitor_bounding_box_bottom_right_len():
    monitor = Monitor(MONITOR_ID)
    assert len(monitor.get_monitor_bounding_box_bottom_right()) == 2

def test_monitor_get_pixel_list_list():
    monitor = Monitor(MONITOR_ID)
    assert isinstance(monitor.get_pixel_list(), list)

def test_monitor_get_pixel_list_len():
    monitor = Monitor(MONITOR_ID)
    assert len(monitor.get_pixel_list()) > 0

def test_monitor_get_monitor_average_color_tuple():
    monitor = Monitor(MONITOR_ID)
    monitor_rgb = monitor.get_monitor_average_color()
    assert isinstance(monitor_rgb, tuple)

def test_monitor_get_monitor_average_color_red_greater_than_or_equal_zero():
    monitor = Monitor(MONITOR_ID)
    monitor_rgb = monitor.get_monitor_average_color()
    assert monitor_rgb[0] >= 0

def test_monitor_get_monitor_average_color_red_less_than_or_equal_255():
    monitor = Monitor(MONITOR_ID)
    monitor_rgb = monitor.get_monitor_average_color()
    assert monitor_rgb[0] <= 255

def test_monitor_get_monitor_average_color_green_greater_than_or_equal_zero():
    monitor = Monitor(MONITOR_ID)
    monitor_rgb = monitor.get_monitor_average_color()
    assert monitor_rgb[1] >= 0

def test_monitor_get_monitor_average_color_green_less_than_or_equal_255():
    monitor = Monitor(MONITOR_ID)
    monitor_rgb = monitor.get_monitor_average_color()
    assert monitor_rgb[1] <= 255

def test_monitor_get_monitor_average_color_blue_greater_than_or_equal_zero():
    monitor = Monitor(MONITOR_ID)
    monitor_rgb = monitor.get_monitor_average_color()
    assert monitor_rgb[2] >= 0

def test_monitor_get_monitor_average_color_blue_less_than_or_equal_255():
    monitor = Monitor(MONITOR_ID)
    monitor_rgb = monitor.get_monitor_average_color()
    assert monitor_rgb[2] <= 255
