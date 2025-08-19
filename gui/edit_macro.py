from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QTreeWidgetItem, QHeaderView, QHBoxLayout

from gui.ui_edit_macro import Ui_formEdit

class EditMacroForm(QDialog):
    def __init__(self, macro, parent=None):
        super().__init__()
        self.ui = Ui_formEdit()
        self.ui.setupUi(self)
        self.ui.seqKeyPressed.setMaximumSequenceLength(1)

        self.selected_macro = macro
        self.ui.lblMacroName.setText(macro['name'])
        self.populateMacroTree()

    def populateMacroTree(self):
        self.ui.treeMacroData.clear()
        self.ui.treeMacroData.header().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        for step in self.selected_macro['steps']:
            self.addStepToTree(self.ui.treeMacroData, step)
        self.ui.treeMacroData.itemSelectionChanged.connect(self.stepSelected)

    def addStepToTree(self, parent, step):
        item = QTreeWidgetItem(parent)
        item.setText(0, str(step["id"]))
        item.setText(1, step["type"].replace("_", " "))

        match step["type"]:
            case "mouse_move" | "mouse_scroll":
                pos_string = "x: " + str(step["pos"][0]) + "\ny: " + str(step["pos"][1])
                item.setText(2, pos_string)
            case "mouse_click":
                item.setText(2, step["button"])
            case "key_press" | "key_release":
                if "Key." in step["key"]:
                    item.setText(2, step["key"][4:].replace("_", " + "))
                else:
                    item.setText(2, step["key"].strip("\'"))
            case "if":
                item.setText(2, step["condition"])

        item.setData(0, Qt.UserRole, step)
        item.setTextAlignment(2, Qt.AlignmentFlag.AlignRight)

        if "steps" in step:
            for child_step in step["steps"]:
                self.addStepToTree(item, child_step)

    def stepSelected(self):
        if self.ui.treeMacroData.currentItem():
            selected_step = self.ui.treeMacroData.currentItem().data(0, Qt.UserRole)

            # may need to add more cases to account for variables?
            match selected_step["type"]:
                case "mouse_move":
                    self.ui.stckEditor.setCurrentIndex(1)
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
        else:
            self.ui.stckEditor.setCurrentIndex(0)

    def moveSelected(self):
        return # todo: create functions for each step type that hooks ui up to logic