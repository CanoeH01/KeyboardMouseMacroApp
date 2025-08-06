from PySide6.QtCore import QObject, Signal
from InputReplayer import InputReplayer


class ReplayerWorker(QObject):
    replaying_finished = Signal()

    def __init__(self, events):
        super().__init__()

        self.replayer = InputReplayer(events)

    def start(self):
        self.replayer.start()
        self.replaying_finished.emit()

    def get_events(self):
        return self.replayer.events
