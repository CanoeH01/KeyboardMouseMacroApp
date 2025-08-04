from PySide6.QtWidgets import QApplication
from gui.main_window import MyWindow

app = QApplication([])
window = MyWindow()
window.show()
app.exec()
