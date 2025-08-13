import json
import time
import uuid
from screeninfo import get_monitors
from pathlib import Path

class MacroManager:
    def __init__(self):
        self.steps = []
        self.macros_metadata = []

        Path("saved-macros").mkdir(parents=True, exist_ok=True)

    def saveMacro(self, steps, name ="untitled"):
        monitors = []
        for m in get_monitors():
            monitors.append({
                "x": m.x,
                "y": m.y,
                "width": m.width,
                "height": m.height,
                "is_primary": getattr(m, 'is_primary', False)
            })

        metaData = {
            "name": name,
            "id": str(uuid.uuid1()),
            "timestamp": time.time(),
            "version": 1,
            "monitors" : monitors,
            "speed" : 1.0,
            "variables" : {},
            "steps" : steps,
        }
        with open('saved-macros\macro_' + str(metaData["id"]) + '.json', 'w') as file:
            json.dump(metaData, file, indent=4)

    def loadMacro(self, file_path):
        with open(file_path, 'r') as file:
            macro = json.load(file)
        return macro["steps"]

    def loadMacrosMetaData(self):
        self.macros_metadata = []
        for file in Path("saved-macros").glob("*.json"):
            with open(file, 'r') as f:
                macro = json.load(f)
                metaData = {k: v for k, v in macro.items() if k != "steps"}
                metaData['file_path'] = str(file)
                self.macros_metadata.append(metaData)

    def renameMacro(self, macroPath, name = "untitled"):
        with open (macroPath, 'r+') as file:
            macro = json.load(file)
            macro['name'] = name
            file.seek(0)
            json.dump(macro, file)
            file.truncate()

    def deleteMacro(self, macroPath):
        filePath = Path(macroPath)
        if filePath.exists():
            filePath.unlink()
            return True
        return False
