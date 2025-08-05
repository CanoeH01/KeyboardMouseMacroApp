from PySide6.QtCore import Qt, QThread
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QWidget, QInputDialog
from InputReplayer import InputReplayer
from RecorderWorker import RecorderWorker
from .ui_main_window import Ui_Form
from MacroManager import MacroManager


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.recorder = None
        self.recording_thread = None

        self.ui.btnRecord.clicked.connect(self.btnRecord_clicked)
        self.ui.btnReplay.clicked.connect(self.btnReplay_clicked)
        self.ui.btnSave.clicked.connect(self.btnSave_clicked)

    def btnRecord_clicked(self):
        self.recording_thread = QThread()
        self.recorder = RecorderWorker()
        self.recorder.moveToThread(self.recording_thread)

        self.recording_thread.started.connect(self.recorder.start)
        self.recorder.recording_finished.connect(self.recording_done)

        self.ui.lblRecording.setText("Recording...\nPress Esc to Stop")
        self.ui.btnReplay.setEnabled(False)
        self.ui.btnRecord.setEnabled(False)
        self.ui.btnSave.setEnabled(False)
        self.recording_thread.start()

    def btnReplay_clicked(self):
        if self.recorder:
            replayer = InputReplayer(self.recorder.get_events())
            replayer.start()

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Escape and self.recorder:
            self.recorder.stop()

    def recording_done(self):
        self.ui.btnReplay.setEnabled(True)
        self.ui.btnRecord.setEnabled(True)
        self.ui.btnSave.setEnabled(True)
        self.ui.lblRecording.setText("done")
        self.recording_thread.quit()
        self.recording_thread.wait()

    def btnSave_clicked(self):
        nameDialog = QInputDialog.getText(None, "Save File", "Please enter file name:")

        if nameDialog[1]:
            fileSaver = MacroManager()
            fileSaver.saveMacro(self.recorder.get_events(), nameDialog[0])

