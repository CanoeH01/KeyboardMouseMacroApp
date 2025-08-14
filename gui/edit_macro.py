from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QTreeWidgetItem, QHeaderView

from gui.ui_edit_macro import Ui_formEdit

class EditMacroForm(QDialog):
    def __init__(self, macro, parent=None):
        super().__init__()
        self.ui = Ui_formEdit()
        self.ui.setupUi(self)

        self.selected_macro = macro

        self.ui.lblMacroName.setText(self.selected_macro['name'])
        self.populateMacroTree()

    def populateMacroTree(self):
        self.ui.treeMacroData.clear()
        self.ui.treeMacroData.header().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        for step in self.selected_macro['steps']:
            self.addStepToTree(self.ui.treeMacroData, step)

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