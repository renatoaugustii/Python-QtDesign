from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PySide6.QtCore import QSize, Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Meu Qlabel")
        self.lbl = QLabel('Meu Code')
        #self.setFixedSize(QSize(600,400))
        #self.lbl.setText("Meu Label")

        font = self.lbl.font()
        font.setPointSize(35)
        self.lbl.setFont(font)
        self.lbl.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.setCentralWidget(self.lbl)    
        
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
