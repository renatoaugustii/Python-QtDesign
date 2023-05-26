import sys
from PySide6.QtCore import QSize 
from PySide6.QtWidgets import QApplication, QMainWindow



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
      


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()