import time
from pynput import mouse, keyboard
from utils import getVirtualScreenBounds

class InputRecorder:
    def __init__(self):
        self.steps = []
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
            'id': len(self.steps) + 1,
            'type': 'mouse_move',
            'pos': mouse.Controller().position,
            'timestamp': 0
        }
        self.steps.append(mouseStartingPoint)

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
            'id': len(self.steps) + 1,
            'type' : 'mouse_move',
            'pos': self.normalizePosition(x, y),
            'timestamp': self.getElapsedTime(),
        }
        self.steps.append(mouseMovement)

    def on_click(self, x, y, button, pressed):
        mouseClick = {
            'id': len(self.steps) + 1,
            'type' : 'mouse_click',
            'button': button,
            'pressed': pressed,
            'pos': self.normalizePosition(x, y),
            'timestamp': self.getElapsedTime(),
        }
        self.steps.append(mouseClick)

    def on_scroll(self, x, y, dx, dy):
        mouseScroll = {
            'id': len(self.steps) + 1,
            'type' : 'mouse_scroll',
            'pos': (dx, dy),
            'timestamp': self.getElapsedTime(),
        }
        self.steps.append(mouseScroll)

    def on_press(self, key):
        keyPress = {
            'id': len(self.steps) + 1,
            'type' : 'key_press',
            'key': str(key),
            'timestamp': self.getElapsedTime(),
        }
        if key == keyboard.Key.esc:
            self.stop()
        else:
            self.steps.append(keyPress)

    def on_release(self, key):
        keyRelease = {
            'id': len(self.steps) + 1,
            'type' : 'key_release',
            'key': str(key),
            'timestamp': self.getElapsedTime(),
        }
        self.steps.append(keyRelease)