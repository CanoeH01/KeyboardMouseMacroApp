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
        self.keyboardListener.join()

    def getElapsedTime(self):
        return time.time() - self.start_time

    def stop(self):
        self.mouseListener.stop()
        self.keyboardListener.stop()

        for event in self.events:
            for key in event:
                print(key, ":", event[key])
            print()

    def on_move(self, x, y):
        mouseMovement = {
            'type' : 'move',
            'pos': (x, y),
            'timestamp': self.getElapsedTime(),
        }
        self.events.append(mouseMovement)

    def on_click(self, x, y, button, pressed):
        mouseClick = {
            'type' : 'mouse_click',
            'pos': (x, y),
            'timestamp': self.getElapsedTime(),
        }
        self.events.append(mouseClick)

    def on_scroll(self, x, y, dx, dy):
        mouseScroll = {
            'type' : 'mouse_scroll',
            'pos': (x, y, dx, dy),
            'timestamp': self.getElapsedTime(),
        }
        self.events.append(mouseScroll)

    def on_press(self, key):
        keyPress = {
            'type' : 'key_press',
            'key': key,
            'timestamp': self.getElapsedTime(),
        }
        if key == keyboard.Key.esc:
            self.stop()
        else:
            self.events.append(keyPress)

    def on_release(self, key):
        keyRelease = {
            'type' : 'key_release',
            'key': key,
            'timestamp': self.getElapsedTime(),
        }
        self.events.append(keyRelease)