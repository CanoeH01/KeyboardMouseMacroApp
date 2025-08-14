from PySide6.QtWidgets import QDialog
from gui.ui_edit_macro import Ui_formEdit

class EditMacroForm(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_formEdit()
        self.ui.setupUi(self)