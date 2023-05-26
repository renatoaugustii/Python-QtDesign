import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QLabel, QStatusBar

#BIBLIOTECA DE ÍCONES
# https://p.yusukekamiyamane.com/

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QToolBar")  

        self.lbl = QLabel("QToolBar")
        self.lbl.setAlignment(Qt.AlignCenter) 
        self.setCentralWidget(self.lbl)  

        toolbar = QToolBar("Minha Tool")
        self.addToolBar(toolbar)
        toolbar.setIconSize(QSize(24,24))


        btn_action = QAction(QIcon('home.png'),"meu btn", self)
        btn_action.setStatusTip("Esse é meu Btn")
        btn_action.triggered.connect(self.functionn)
        btn_action.setCheckable(True)

        toolbar.addAction(btn_action)

        toolbar.addSeparator()

        
        btn_action2 = QAction(QIcon('open-share.png'),"2 btn", self)
        btn_action2.setStatusTip("Esse é meu Btn 2")
        btn_action2.triggered.connect(self.functionn)
        btn_action2.setCheckable(True)
        toolbar.addAction(btn_action2)

        self.setStatusBar(QStatusBar(self))

    def  functionn(self, s):
        print("Clicked",s) 

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()