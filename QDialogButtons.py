import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton,QLineEdit,
                               QDialog, QDialogButtonBox, QVBoxLayout, QLabel)



class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Dialog ")
    btn = QPushButton("Click para abrir um Dialog!")
    btn.clicked.connect(self.button_clicked)
    
    
    self.setCentralWidget(btn)
    
  
  def button_clicked(self, s):
    print("click", s)
    dlg = Meu_dialog()
    if dlg.exec_():
      print("sucesso")
    else:
      print("cancelar!")
  
class Meu_dialog(QDialog):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Meu Dialog")
    self.texto = ""
    
    buttons = QDialogButtonBox.SaveAll | QDialogButtonBox.Close
    
    self.btn_box = QDialogButtonBox(buttons)
    self.btn_box.accepted.connect(self.accept)
    self.btn_box.rejected.connect(self.reject)

   
    self.layout = QVBoxLayout()
    msg = QLabel("Você deseja continuar")
    self.layout.addWidget(msg)
    self.layout.addWidget(self.btn_box)
    self.setLayout(self.layout)
    
    """
    QDialogButtonBox.Ok
    QDialogButtonBox.Open
    QDialogButtonBox.Save
    QDialogButtonBox.Cancel
    QDialogButtonBox.Close
    QDialogButtonBox.Discard
    QDialogButtonBox.Apply
    QDialogButtonBox.Reset
    QDialogButtonBox.RestoreDefaults
    QDialogButtonBox.Help
    QDialogButtonBox.SaveAll
    QDialogButtonBox.Yes
    QDialogButtonBox.YesToAll
    QDialogButtonBox.No
    QDialogButtonBox.NoToAll
    QDialogButtonBox.Abort
    QDialogButtonBox.Retry
    QDialogButtonBox.Ignore
    QDialogButtonBox.NoButton

    
    """

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
