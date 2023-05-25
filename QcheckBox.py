from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox, QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import QSize, Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CheckBox")

        self.lbl = QLabel("Voce bebe?")
        self.lbl2 = QLabel()
        self.ck = QCheckBox("Sim")
        #self.ck.setCheckState(Qt.Checked)

        layout = QVBoxLayout()
        layout.addWidget(self.lbl)
        layout.addWidget(self.ck)
        layout.addWidget(self.lbl2)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.ck.stateChanged.connect(self.verifica)

    def verifica(self, s):
        if s == 2:
            self.lbl2.setText("Preencha o formulário abaixo")
        else:
            self.lbl2.setText("")
            
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
