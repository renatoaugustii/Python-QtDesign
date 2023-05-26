import sys
from tkinter import Button
from PySide6.QtCore import QSize 
from PySide6.QtWidgets import (QApplication, QMainWindow, 
                               QPushButton, QMessageBox)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Message BOX")
        self.setFixedSize(QSize(600,400))
        
        button = QPushButton("SHOW!")
        self.setCentralWidget(button)
        
        button.setCheckable(True)
        button.clicked.connect(self.show_question)
        
        
    def show_question(self):
        self.msg = QMessageBox()
        self.msg.setWindowTitle('Question')
        self.msg.setText("Deseja executar esta ação?")
        self.msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.NoToAll | QMessageBox.Abort)
        self.msg.setIcon(QMessageBox.Question)
        resposta = self.msg.exec_()
        if resposta == QMessageBox.Yes:
            print("O Programa será executado.")
            
        elif resposta == QMessageBox.NoToAll:
            print('No to all')
            
        elif resposta == QMessageBox.Abort:
            print('Abort')
        else:
            print("Operação cancelada!")

    def show_message(self,s):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setWindowTitle('Message')
        self.msg.setText("Operação concluída com suscesso!")
        self.msg.exec()

        """_
        QMessageBox.NoIcon
        QMessageBox.Question 
        QMessageBox.Information 
        QMessageBox.Warning 
        QMessageBox.Critical
        """
                

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
