import json
import time
import uuid
from pathlib import Path

class MacroManager:
    def __init__(self):
        self.events = []
        self.macros_metadata = []

        Path("saved-macros").mkdir(parents=True, exist_ok=True)

    def saveMacro(self, events, name = "untitled"):
        events.insert(0, {
            "id": str(uuid.uuid1()),
            "name": name,
            "timestamp": time.time()
        })
        with open('saved-macros\macro_' + str(events[0]['id']) + '.json', 'w') as file:
            json.dump(events, file)

    def loadMacro(self, file_path):
        with open(file_path, 'r') as file:
            events = json.load(file)

    def loadMacrosMetaData(self):
        self.macros_metadata = []
        for file in Path("saved-macros").glob("*.json"):
            with open(file, 'r') as f:
                macroData = json.load(f)[0]
                macroData['file_path'] = str(file)
                self.macros_metadata.append(macroData)

    def renameMacro(self, macroPath, name = "untitled"):
        with open (macroPath, 'r+') as file:
            macro = json.load(file)
            macro[0]['name'] = name
            file.seek(0)
            json.dump(macro, file)
            file.truncate()