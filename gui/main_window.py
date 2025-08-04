import os
from PySide6.QtWidgets import QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile



class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def loadMainWindow(self):
        loader = QUiLoader()
        ui_file = QFile(os.path.join(os.path.dirname(__file__), "main_window.ui"))
        ui_file.open(QFile.ReadOnly)

        window = loader.load(ui_file)
        ui_file.close()

        return window

