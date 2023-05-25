from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox
from PySide6.QtCore import QSize, Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ComboBox")
        self.cb = QComboBox()

        # self.cb.addItem('Item 1')
        # self.cb.addItem('Item 2')
        # self.cb.addItem('Item 3')
        
        self.cb.addItems(["Item 01", "Item 02", "Item 03"])

        self.setCentralWidget(self.cb) 

        self.cb.currentIndexChanged.connect(self.mudanca_indice)

        #self.cb.setEditable(self.cb) #Torna o cb editável
        
        #self.cb.setMaxCount(10)
        #self.cb.NoInsert
        #self.cb.InsertAtTop
        #self.cb.InsertAfterCurrent
        #self.cb.InsertBeforeCurrent

    def mudanca_indice(self,i):
        print(i)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
