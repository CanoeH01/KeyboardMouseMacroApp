from PySide6.QtCore import QObject, Signal
from InputRecorder import InputRecorder


class RecorderWorker(QObject):
    recording_finished = Signal()

    def __init__(self):
        super().__init__()

        self.recorder = InputRecorder()
        self._is_recording = False

    def start(self):
        self._is_recording = True
        self.recorder.start()
        self._is_recording = False
        self.recording_finished.emit()

    def stop(self):
        if self._is_recording:
            self.recorder.stop()

    def get_events(self):
        return self.recorder.events
