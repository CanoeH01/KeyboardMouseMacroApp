from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QTreeWidgetItem, QHeaderView, QMessageBox

from MacroManager import MacroManager
from gui.ui_edit_macro import Ui_formEdit

class EditMacroForm(QDialog):
    def __init__(self, macro, file_path, parent=None):
        super().__init__(parent)
        self.ui = Ui_formEdit()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('gui/cursoricon.png'))
        self.ui.seqKeyPressed.setMaximumSequenceLength(1)

        self.selected_macro = macro
        self.file_path = file_path
        self.current_item = None
        self.current_step = None

        self.ui.lblMacroName.setText(macro['name'])
        self.populateMacroTree()

        self.ui.numMoveX.valueChanged.connect(lambda val: self.on_move_changed(axis=0, val=val))
        self.ui.numMoveY.valueChanged.connect(lambda val: self.on_move_changed(axis=1, val=val))
        self.ui.btnSaveChanges.clicked.connect(self.saveChanges)
        self.ui.btnCancel.clicked.connect(self.close)

    def populateMacroTree(self):
        self.ui.treeMacroData.clear()
        self.ui.treeMacroData.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        for step in self.selected_macro['steps']:
            self.addStepToTree(self.ui.treeMacroData, step)
        self.ui.treeMacroData.itemSelectionChanged.connect(self.stepSelected)

    def addStepToTree(self, parent, step):
        item = QTreeWidgetItem(parent)
        item.setText(0, str(step["id"]))
        item.setText(1, step["type"].replace("_", " "))

        match step["type"]:
            case "mouse_move" | "mouse_scroll":
                pos_string = f"x: {step['pos'][0]}\ny: {step['pos'][1]}"
                item.setText(2, pos_string)
            case "mouse_click":
                item.setText(2, step["button"])
            case "key_press" | "key_release":
                key_text = step["key"]
                if key_text.startswith("Key."):
                    key_text = key_text[4:].replace("_", " + ")
                else:
                    key_text = key_text.strip("'")
                item.setText(2, key_text)
            case "if":
                item.setText(2, step["condition"])

        item.setTextAlignment(2, Qt.AlignmentFlag.AlignRight)

        if "steps" in step:
            for child_step in step["steps"]:
                self.addStepToTree(item, child_step)

    def refreshTreeItem(self, item, step):
        item.setText(0, str(step["id"]))
        item.setText(1, step["type"].replace("_", " "))

        match step["type"]:
            case "mouse_move" | "mouse_scroll":
                item.setText(2, f"x: {step['pos'][0]}\ny: {step['pos'][1]}")
            case "mouse_click":
                item.setText(2, step["button"])
            case "key_press" | "key_release":
                key_text = step["key"]
                if key_text.startswith("Key."):
                    key_text = key_text[4:].replace("_", " + ")
                else:
                    key_text = key_text.strip("'")
                item.setText(2, key_text)
            case "if":
                item.setText(2, step["condition"])


    def stepSelected(self):
        item = self.ui.treeMacroData.currentItem()
        if not item:
            self.ui.stckEditor.setCurrentIndex(0)
            return

        step_type = self.get_step_from_item(item)["type"]
        match step_type:
            case "mouse_move":
                self.moveSelected(item)
            case "mouse_click":
                self.ui.stckEditor.setCurrentIndex(2)
            case "mouse_scroll":
                self.ui.stckEditor.setCurrentIndex(3)
            case "key_press":
                self.ui.stckEditor.setCurrentIndex(4)
            case "key_release":
                self.ui.stckEditor.setCurrentIndex(5)
            case "if":
                self.ui.stckEditor.setCurrentIndex(6)
            case _:
                self.ui.stckEditor.setCurrentIndex(0)

    def moveSelected(self, item):
        self.current_item = item
        self.current_step = self.get_step_from_item(item)

        self.ui.stckEditor.setCurrentIndex(1)
        self.ui.lblMouseMove.setText(f"Step {self.current_step['id']} Mouse Move")
        self.ui.numMoveX.setValue(self.current_step["pos"][0])
        self.ui.numMoveY.setValue(self.current_step["pos"][1])

    def get_step_from_item(self, item):
        path = []
        current = item
        while current.parent():
            parent = current.parent()
            path.insert(0, parent.indexOfChild(current))
            current = parent
        path.insert(0, self.ui.treeMacroData.indexOfTopLevelItem(current))

        # Walk path to get the step dict
        step = self.selected_macro['steps'][path[0]]
        for index in path[1:]:
            step = step["steps"][index]
        return step

    def on_move_changed(self, axis, val):
        if self.current_step and self.current_item:
            self.current_step["pos"][axis] = val
            self.refreshTreeItem(self.current_item, self.current_step)

    def saveChanges(self):
        confirmDialog = QMessageBox()
        confirmDialog.setWindowTitle("Update Macro")
        confirmDialog.setText("Do you want to save changes?")
        confirmDialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        if confirmDialog.exec() == QMessageBox.Yes:
            macro_updater = MacroManager()
            macro_updater.updateMacro(self.file_path, self.selected_macro)
            QMessageBox.information(self, "Macro Updated", "Macro Saved Successfully")

