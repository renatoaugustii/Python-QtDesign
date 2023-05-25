from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import QSize, Qt
import sys
from PySide6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Imagem")
        self.lbl = QLabel()
        self.lbl.setPixmap(QPixmap("img.jpeg"))
        self.lbl.setScaledContents(True)


        self.setCentralWidget(self.lbl)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
