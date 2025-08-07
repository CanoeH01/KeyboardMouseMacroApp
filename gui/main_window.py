from datetime import datetime
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMenu, QInputDialog
from keyboard import register_word_listener
from ReplayerWorker import ReplayerWorker
from gui.ui_main_window import Ui_formMain
from gui.record_macro import RecordMacroForm
from MacroManager import MacroManager

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_formMain()
        self.ui.setupUi(self)
        self.record_macro = RecordMacroForm(self)

        self.selected_macro = {'name': None, 'filePath': None }
        self.options_context = QMenu()
        self.replayer = None
        self.file_manager = MacroManager()

        self.populateMacrosList()
        self.createOptionsContextMenu()

        self.ui.tblSavedMacros.itemSelectionChanged.connect(self.on_macro_selected)
        self.ui.btnRecordNewMacro.clicked.connect(self.record_new_macro)
        self.record_macro.macro_saved.connect(self.populateMacrosList)

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
        self.options_context.actionItems['edit'] = (QAction("Edit", self))
        self.options_context.actionItems['repeat'] = (QAction("Repeat", self))
        self.options_context.actionItems['repeat'].setCheckable(True)

        for item in self.options_context.actionItems.values():
            item.setEnabled(False)
            self.options_context.addAction(item)

        self.ui.btnOptions.setMenu(self.options_context)

    def rename_macro(self):
        nameDialog = QInputDialog.getText(None, "Rename Macro", "Please enter a new name for macro: " + self.selected_macro['name'].text())

        if nameDialog[1]:
            self.file_manager.renameMacro(self.selected_macro['filePath'], nameDialog[0])
            self.record_macro.macro_saved.emit(True)

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

    def record_new_macro(self):
        self.hide()
        self.record_macro.exec()
        self.show()