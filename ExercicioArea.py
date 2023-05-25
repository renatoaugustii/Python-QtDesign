# Crie um programa que contenha uma lineEdit para informar
# a largura, outro para informar a altura e um para o comprimento.
# Esse programa deverá calcular o metro cúbico de uma área e o 
# resultado deverá ser mostrado em uma label.

# Utilize o QvBoxLayout para deixar os dados organizados.

# Formula:
# A x C x L

# Altura x Comprimento X Largura

import sys
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow, QVBoxLayout,QLabel, QLineEdit, QFrame

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cálculo de metro Cúbico")
        
        self.lbl_Altura = QLabel("Altura")
        self.lbl_Comprimento = QLabel("Comprimento")
        self.lbl_Largura = QLabel("Largura")

        self.resultado = QLabel("0")

        self.txt_altura = QLineEdit()   
        self.txt_largura = QLineEdit()    
        self.txt_comprimento = QLineEdit()     

        self.button = QPushButton("Calcular")

        layout = QVBoxLayout()
        
        layout.addWidget(self.lbl_Largura)
        layout.addWidget(self.txt_largura)

        layout.addWidget(self.lbl_Altura)
        layout.addWidget(self.txt_altura)

        layout.addWidget(self.lbl_Comprimento)
        layout.addWidget(self.txt_comprimento)

        layout.addWidget(self.resultado)

        layout.addWidget(self.button)

        self.button.clicked.connect(self.calcular)

        container = QFrame()
        container.setLayout(layout)

        self.setCentralWidget(container)


    def calcular(self):
        Resultado =str(
            float(self.txt_altura.text())*
            float(self.txt_comprimento.text())*
            float(self.txt_largura.text())
        )
        self.resultado.setText(Resultado)    



app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()

