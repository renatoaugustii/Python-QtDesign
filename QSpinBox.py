import sys
from PySide6.QtCore import QSize 
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QSpinBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QSpinBox")
        self.qsb = QSpinBox()
        self.qsb.setMinimum(-5)
        self.qsb.setMaximum(100)
        self.qsb.setPrefix("R$")
        self.qsb.setSingleStep(3)
        self.setCentralWidget(self.qsb) 

        self.qsb.valueChanged.connect(self.value_c)
        self.qsb.textChanged.connect(self.value_c)

    def value_c(self, i):
        print(i)      


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()