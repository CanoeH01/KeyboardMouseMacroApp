from PySide6.QtCore import Qt, QThread
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QWidget
from InputReplayer import InputReplayer
from RecorderWorker import RecorderWorker
from .ui_main_window import Ui_Form


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.recorder = None
        self.recording_thread = None

        self.ui.btnRecord.clicked.connect(self.btnRecord_clicked)
        self.ui.btnReplay.clicked.connect(self.btnReplay_clicked)

    def btnRecord_clicked(self):
        self.recording_thread = QThread()
        self.recorder = RecorderWorker()
        self.recorder.moveToThread(self.recording_thread)

        self.recording_thread.started.connect(self.recorder.start)
        self.recorder.recording_finished.connect(self.recording_done)

        self.ui.lblRecording.setText("Recording...\nPress Esc to Stop")
        self.recording_thread.start()

    def btnReplay_clicked(self):
        if self.recorder:
            replayer = InputReplayer(self.recorder.get_events())
            replayer.start()

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Escape and self.recorder:
            self.recorder.stop()

    def recording_done(self):
        self.ui.lblRecording.setText("done")
        self.recording_thread.quit()
        self.recording_thread.wait()
