import time
from pynput import mouse, keyboard
from utils import getVirtualScreenBounds

class InputRecorder:
    def __init__(self):
        self.events = []
        self.start_time = None
        self.screen_bounds = getVirtualScreenBounds()

        self.mouseListener = mouse.Listener(
            on_move=self.on_move,
            on_click=self.on_click,
            on_scroll=self.on_scroll)

        self.keyboardListener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)

    def start(self):
        mouseStartingPoint = {
            'type': 'mouse_move',
            'pos': mouse.Controller().position,
            'timestamp': 0
        }
        self.events.append(mouseStartingPoint)

        self.start_time = time.time()
        self.mouseListener.start()
        self.keyboardListener.start()
        self.keyboardListener.join()

    def stop(self):
        self.mouseListener.stop()
        self.keyboardListener.stop()

    def getElapsedTime(self):
        return time.time() - self.start_time

    def normalizePosition(self, x, y):
        norm_x = (x - self.screen_bounds[0]) / self.screen_bounds[2]
        norm_y = (y - self.screen_bounds[1]) / self.screen_bounds[3]
        return norm_x, norm_y

    def on_move(self, x, y):
        mouseMovement = {
            'type' : 'mouse_move',
            'pos': self.normalizePosition(x, y),
            'timestamp': self.getElapsedTime(),
        }
        self.events.append(mouseMovement)

    def on_click(self, x, y, button, pressed):
        mouseClick = {
            'type' : 'mouse_click',
            'button': button,
            'pressed': pressed,
            'pos': self.normalizePosition(x, y),
            'timestamp': self.getElapsedTime(),
        }
        self.events.append(mouseClick)

    def on_scroll(self, x, y, dx, dy):
        mouseScroll = {
            'type' : 'mouse_scroll',
            'pos': (dx, dy),
            'timestamp': self.getElapsedTime(),
        }
        self.events.append(mouseScroll)

    def on_press(self, key):
        keyPress = {
            'type' : 'key_press',
            'key': str(key),
            'timestamp': self.getElapsedTime(),
        }
        if key == keyboard.Key.esc:
            self.stop()
        else:
            self.events.append(keyPress)

    def on_release(self, key):
        keyRelease = {
            'type' : 'key_release',
            'key': str(key),
            'timestamp': self.getElapsedTime(),
        }
        self.events.append(keyRelease)