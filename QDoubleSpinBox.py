import sys
from PySide6.QtCore import QSize 
from PySide6.QtWidgets import (QApplication, QMainWindow, 
                               QWidget, QDoubleSpinBox, QAbstractSpinBox)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QSpinBox")
        self.qDsb = QDoubleSpinBox()
        self.qDsb.setMinimum(-5)
        self.qDsb.setMaximum(100)
        self.qDsb.setPrefix("R$")
        self.qDsb.setSingleStep(3)
        self.setCentralWidget(self.qDsb) 

        self.qDsb.valueChanged.connect(self.value_c)
        self.qDsb.textChanged.connect(self.value_c)
        self.qDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)

    def value_c(self, i):
        print(i)      


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()