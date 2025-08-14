from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QKeyEvent, QColor
from PySide6.QtWidgets import QInputDialog, QDialog, QGraphicsDropShadowEffect
from ReplayerWorker import ReplayerWorker
from RecorderWorker import RecorderWorker
from gui.ui_record_macro import Ui_formRecord
from MacroManager import MacroManager

class RecordMacroForm(QDialog):
    macro_saved = Signal(bool)

    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_formRecord()
        self.ui.setupUi(self)

        self.recorder = None
        self.recording_thread = None
        self.replayer = None
        self.replay_thread = None
        self.file_manager = MacroManager()


        self.ui.btnRecord.clicked.connect(self.btnRecord_clicked)
        self.ui.btnReplay.clicked.connect(self.btnReplay_clicked)
        self.ui.btnSave.clicked.connect(self.btnSave_clicked)

    def btnRecord_clicked(self):
        self.recording_thread = QThread()
        self.recorder = RecorderWorker()
        self.recorder.moveToThread(self.recording_thread)

        self.recording_thread.started.connect(self.recorder.start)
        self.recorder.recording_finished.connect(self.recording_done)

        self.ui.btnReplay.setEnabled(False)
        self.ui.btnRecord.setEnabled(False)
        self.ui.btnSave.setEnabled(False)

        self.setWindowTitle("Recording...")
        self.ui.lblStopRecording.setText("Press ESC to stop")

        self.recording_thread.start()

    def btnReplay_clicked(self):
        if self.recorder:
            self.replay_thread = QThread()
            self.replayer = ReplayerWorker(self.recorder.get_events())
            self.replayer.moveToThread(self.replay_thread)

            self.replay_thread.started.connect(self.replayer.start)
            self.replayer.replaying_finished.connect(self.replaying_done)
            self.replayer.replaying_finished.connect(self.replay_thread.quit)
            self.replayer.replaying_finished.connect(self.replay_thread.deleteLater)

            self.ui.btnReplay.setEnabled(False)
            self.ui.btnRecord.setEnabled(False)
            self.ui.btnSave.setEnabled(False)
            self.setWindowTitle("Replaying...")

            self.replay_thread.start()

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Escape and self.recorder:
            self.recorder.stop()

    def replaying_done(self):
        self.ui.btnReplay.setEnabled(True)
        self.ui.btnRecord.setEnabled(True)
        self.ui.btnSave.setEnabled(True)
        self.setWindowTitle("Create Macro")
        self.ui.lblStopRecording.setText("Macro recorded")

    def recording_done(self):
        self.ui.btnReplay.setEnabled(True)
        self.ui.btnRecord.setEnabled(True)
        self.ui.btnSave.setEnabled(True)
        self.setWindowTitle("Create Macro")
        self.ui.lblStopRecording.setText("Macro recorded")
        self.recording_thread.quit()
        self.recording_thread.wait()

    def btnSave_clicked(self):
        nameDialog = QInputDialog.getText(None, "Save File", "Please enter file name:")

        if nameDialog[1]:
            self.file_manager.saveMacro(self.recorder.get_events(), nameDialog[0])
            self.ui.lblStopRecording.setText("")
            self.macro_saved.emit(True)
            self.close()