from datetime import datetime
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QTableWidgetItem
from gui.ui_main_window import Ui_formMain
from gui.record_macro import RecordMacroForm
from MacroManager import MacroManager

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_formMain()
        self.ui.setupUi(self)

        self.record_macro = None

        self.file_manager = MacroManager()

        self.ui.tblSavedMacros.itemSelectionChanged.connect(self.on_macro_selected)
        self.populateMacrosList()

        self.ui.btnRecordNewMacro.clicked.connect(self.record_new_macro)

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

    def on_macro_selected(self):
        selectedItem = self.ui.tblSavedMacros.selectedItems()
        if not selectedItem:
            return
        file_path = self.ui.tblSavedMacros.item(selectedItem[0].row(), 0).data(Qt.UserRole)

    def record_new_macro(self):
        self.record_macro = RecordMacroForm(self)
        self.record_macro.macro_saved.connect(self.populateMacrosList)
        self.hide()
        self.record_macro.exec()
        self.show()