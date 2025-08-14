from datetime import datetime
from PySide6.QtCore import Qt, QThread, QTimer
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMenu, QInputDialog, QMessageBox
from ReplayerWorker import ReplayerWorker
from gui.ui_main_window import Ui_formMain
from gui.record_macro import RecordMacroForm
from gui.edit_macro import EditMacroForm
from MacroManager import MacroManager

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_formMain()
        self.ui.setupUi(self)
        self.options_context = QMenu()

        self.record_macro = RecordMacroForm(self)

        self.selected_macro = {'name': None, 'filePath': None }
        self.replayer = None
        self.file_manager = MacroManager()
        self.is_repeating = False

        self.populateMacrosList()
        self.createOptionsContextMenu()

        self.ui.tblSavedMacros.itemSelectionChanged.connect(self.on_macro_selected)
        self.ui.btnRecordNewMacro.clicked.connect(self.record_new_macro)
        self.record_macro.macro_saved.connect(self.populateMacrosList)
        self.ui.btnPlayMacro.clicked.connect(self.btnPlayMacro_clicked)

    def populateMacrosList(self):
        self.file_manager.loadMacrosMetaData()
        self.ui.tblSavedMacros.clearContents()
        self.ui.tblSavedMacros.setRowCount(len(self.file_manager.macros_metadata))

        for i in range(len(self.file_manager.macros_metadata)):
            macroDateTime = datetime.fromtimestamp(self.file_manager.macros_metadata[i]['timestamp'])
            macroDateTime = macroDateTime.strftime("%d/%m/%Y %H:%M")
            timeTableItem = QTableWidgetItem()
            timeTableItem.setData(Qt.UserRole, self.file_manager.macros_metadata[i]["file_path"])
            timeTableItem.setText(macroDateTime)

            nameTableItem = QTableWidgetItem()
            nameTableItem.setData(Qt.UserRole, self.file_manager.macros_metadata[i]["file_path"])
            nameTableItem.setText(self.file_manager.macros_metadata[i]["name"])

            self.ui.tblSavedMacros.setItem(i, 0, nameTableItem)
            self.ui.tblSavedMacros.setItem(i, 1, timeTableItem)
        self.ui.tblSavedMacros.sortItems(1, Qt.DescendingOrder)

    def createOptionsContextMenu(self):
        self.options_context = QMenu(self)
        self.options_context.actionItems = {}

        self.options_context.actionItems['rename'] = (QAction("Rename", self))
        self.options_context.actionItems['rename'].triggered.connect(self.rename_macro)

        self.options_context.actionItems['delete'] = (QAction("Delete", self))
        self.options_context.actionItems['delete'].triggered.connect(self.delete_macro)

        self.options_context.actionItems['edit'] = (QAction("Edit", self))
        self.options_context.actionItems['edit'].triggered.connect(self.edit_macro)

        self.options_context.actionItems['repeat'] = (QAction("Repeat", self))
        self.options_context.actionItems['repeat'].setCheckable(True)
        self.options_context.actionItems['repeat'].triggered.connect(self.chkRepeatMacro_checked)

        for item in self.options_context.actionItems.values():
            item.setEnabled(False)
            self.options_context.addAction(item)

        self.ui.btnOptions.setMenu(self.options_context)

    def on_macro_selected(self):
        selected_items = self.ui.tblSavedMacros.selectedItems()

        if selected_items:
            self.selected_macro['name'] = selected_items[0]
            self.selected_macro['filePath'] = self.ui.tblSavedMacros.item(self.selected_macro['name'].row(), 0).data(Qt.UserRole)

            self.ui.btnPlayMacro.setEnabled(True)
            self.ui.btnDeleteMacro.setEnabled(True)
            for item in self.options_context.actionItems.values():
                item.setEnabled(True)
        else:
            self.selected_macro['name'] = None
            self.selected_macro['filePath'] = None

            self.ui.btnPlayMacro.setEnabled(False)
            self.ui.btnDeleteMacro.setEnabled(False)
            for item in self.options_context.actionItems.values():
                item.setEnabled(False)

    def rename_macro(self):
        nameDialog = QInputDialog.getText(None, "Rename Macro", "Please enter a new name for macro: " + self.selected_macro['name'].text())

        if nameDialog[1]:
            self.file_manager.renameMacro(self.selected_macro['filePath'], nameDialog[0])
            self.record_macro.macro_saved.emit(True)

    def delete_macro(self):
        confirmDialog = QMessageBox()
        confirmDialog.setWindowTitle("Delete Macro")
        confirmDialog.setText("Are you sure you want to delete saved macro:\n" + self.selected_macro['name'].text())
        confirmDialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        if confirmDialog.exec() == QMessageBox.Yes:
            if self.file_manager.deleteMacro(self.selected_macro['filePath']):
                self.record_macro.macro_saved.emit(True)
                QMessageBox.information(self, "Macro Deleted", "Macro Deleted Successfully")

    def chkRepeatMacro_checked(self):
        self.options_context.show()
        if self.options_context.actionItems['repeat'].isChecked():
            self.is_repeated = True
        else:
            self.is_repeated = False

    def btnPlayMacro_clicked(self):
        if self.options_context.actionItems['repeat'].isChecked():
            self.start_repeating()
        else:
            self.playMacro()

    def playMacro(self, repeat = False):
        selectedMacro = self.file_manager.loadMacroSteps(self.selected_macro['filePath'])
        if not selectedMacro:
            QMessageBox.critical(self, "Error", "Failed to load macro.")
            return

        replay_thread = QThread(self)
        self.replayer = ReplayerWorker(selectedMacro)
        self.replayer.moveToThread(replay_thread)

        replay_thread.started.connect(self.replayer.start)

        self.replayer.replaying_finished.connect(self.replaying_done)
        self.replayer.replaying_finished.connect(replay_thread.quit)
        self.replayer.replaying_finished.connect(self.replayer.deleteLater)

        replay_thread.finished.connect(replay_thread.deleteLater)

        if repeat:
            self.replayer.replaying_finished.connect(self._repeat_if_needed)
            self.setWindowTitle("Looping replay... press ESC to stop")
        else:
            self.setWindowTitle("Replaying...")

        self.ui.btnOptions.setEnabled(False)
        self.ui.btnRecordNewMacro.setEnabled(False)
        self.ui.btnPlayMacro.setEnabled(False)
        self.ui.btnDeleteMacro.setEnabled(False)
        self.ui.lblSavedMacros.setEnabled(False)
        self.ui.tblSavedMacros.setEnabled(False)
        for item in self.options_context.actionItems.values():
            item.setEnabled(False)

        replay_thread.start()

    def _repeat_if_needed(self):
        if self.is_repeating:
            QTimer.singleShot(100, lambda: self.playMacro(repeat=True))

    def start_repeating(self):
        if not self.is_repeating:
            self.is_repeating = True
            self.playMacro(repeat=True)

    def stop_repeating(self):
        self.is_repeating = False

    def replaying_done(self):
        if not self.is_repeating:
            self.setWindowTitle("Macro Manager")
            self.ui.btnOptions.setEnabled(True)
            self.ui.btnRecordNewMacro.setEnabled(True)
            self.ui.btnPlayMacro.setEnabled(True)
            self.ui.btnDeleteMacro.setEnabled(True)
            self.ui.lblSavedMacros.setEnabled(True)
            self.ui.tblSavedMacros.setEnabled(True)
            for item in self.options_context.actionItems.values():
                item.setEnabled(True)

    def record_new_macro(self):
        self.hide()
        self.record_macro.exec()
        self.show()

    def edit_macro(self):
        selectedMacro = self.file_manager.loadMacro(self.selected_macro['filePath'])
        self.hide()
        editMacroForm = EditMacroForm(selectedMacro)
        editMacroForm.exec()
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            if self.is_repeating:
                self.stop_repeating()
        else:
            super().keyPressEvent(event)