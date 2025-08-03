import time
from pynput import mouse, keyboard
from pynput.keyboard import Key


class InputReplayer:
    def __init__(self, events):
        self.events = events
        self.keyboard = keyboard.Controller()
        self.mouse = mouse.Controller()

    def start(self):
        previousTime = 0

        for event in self.events:
            time.sleep(event['timestamp'] - previousTime)
            previousTime = event['timestamp']
            match event['type']:
                case 'mouse_move':
                    self.mouse.position = (event['pos'])
                case 'mouse_click':
                    if event['pressed']:
                        self.mouse.press(event['button'])
                    else:
                        self.mouse.release(event['button'])
                case 'mouse_scroll':
                    self.mouse.scroll(event['pos'][0], event['pos'][1])
                case 'key_press':
                    self.keyboard.press(self.stringToKey(event['key']))
                case 'key_release':
                    self.keyboard.release(self.stringToKey(event['key']))

    def stringToKey(self, key_str):
        if key_str.startswith('Key.'):
            return getattr(Key, key_str.split('.')[1])
        else:
            return key_str.strip("'")
