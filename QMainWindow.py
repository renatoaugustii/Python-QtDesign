from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Meu Primeiro Programa")
        button = QPushButton("Clique Aqui!")
        self.setCentralWidget(button)
        button.clicked.connect(self.imprimir)

    def imprimir(self):
        print("Testando Botão")  
        
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
