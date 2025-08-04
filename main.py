from PySide6.QtWidgets import QApplication
from gui.main_window import MyWindow

app = QApplication([])
window = MyWindow().loadMainWindow()
window.show()
app.exec()
