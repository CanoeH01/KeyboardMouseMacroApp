import time

from pynput import mouse

class InputRecorder:
    def __init__(self):
        self.events = []
        self.start_time = None

    def start(self):
        listener = mouse.Listener(
            on_move=self.on_move,
            on_click=self.on_click,
            on_scroll=self.on_scroll)
        listener.start()
        self.start_time = time.time()
        listener.join()

    def getTime(self):
        return time.strftime("%H:%M:%S", time.localtime())

    def on_move(self, x, y):
        print('Pointer moved to', (x, y), self.getTime())

    def on_click(self, x, y, button, pressed):
        print(button, 'pressed' if pressed else 'released', 'at', (x, y), self.getTime())

    def on_scroll(self, x, y, dx, dy):
        print('Scrolled', 'down' if dy < 0 else 'up',(x, y), self.getTime())