from screeninfo import get_monitors

def getVirtualScreenBounds():
    monitors = get_monitors()
    min_x = min(monitor.x for monitor in monitors)
    min_y = min(monitor.y for monitor in monitors)
    max_x = max(monitor.x + monitor.width for monitor in monitors)
    max_y = max(monitor.y + monitor.height for monitor in monitors)
    return min_x, min_y, max_x - min_x, max_y - min_y