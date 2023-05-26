import sys
from PySide6.QtCore import QSize 
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ListWidget")  
        self.lw=QListWidget()
        self.lw.addItems(['Item 01','Item 02','Item 03'])

        self.setCentralWidget(self.lw)

        self.lw.itemDoubleClicked.connect(self.abrir_janela)
        self.lw.currentItemChanged.connect(self.texto_alterado)

    def abrir_janela(self):
        print('Abrindo Janelas') 

    def texto_alterado(self,t):
        print(t.text())               

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()