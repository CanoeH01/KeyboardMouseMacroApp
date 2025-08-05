import json
import time
import uuid

class MacroManager:
    def __init__(self):
        self.events = []

    def saveMacro(self, events, name = "untitled"):
        events.insert(0, {
            "id": str(uuid.uuid1()),
            "name": name,
            "timestamp": time.time()
        })

        with open('saved-macros\macro_' + str(events[0]['id']) + '.json', 'w') as file:
            json.dump(events, file)

    def loadMacro(self):
        with open('saved-macros\macros.json', 'r') as file:
            self.events = json.load(file)