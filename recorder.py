import time

from pynput import mouse, keyboard


class InputRecorder:
    def __init__(self):
        self.events = []
        self.start_time = None

        self.mouseListener = mouse.Listener(
            on_move=self.on_move,
            on_click=self.on_click,
            on_scroll=self.on_scroll)

        self.keyboardListener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)

    def start(self):

        self.start_time = time.time()
        self.mouseListener.start()
        self.keyboardListener.start()
        self.mouseListener.join()
        self.keyboardListener.join()

    def getTime(self):
        return time.strftime("%H:%M:%S", time.localtime())

    def on_move(self, x, y):
        print('Pointer moved to', (x, y), self.getTime())

    def on_click(self, x, y, button, pressed):
        print(button, 'pressed' if pressed else 'released', 'at', (x, y), self.getTime())

    def on_scroll(self, x, y, dx, dy):
        print('Scrolled', 'down' if dy < 0 else 'up',(x, y), self.getTime())

    def on_press(self, key):
        print(key, 'pressed')
        if key == keyboard.Key.esc:
            self.keyboardListener.stop()
            self.mouseListener.stop()

    def on_release(self, key):
        print(key, 'released')