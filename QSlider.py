import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QSlider



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
      
        self.setWindowTitle("QSlider")
        self.slider = QSlider()

        self.setCentralWidget(self.slider)
        self.slider.setMinimum(-5)    

        self.slider.valueChanged.connect(self.value_changed)
        #sliderMoved
        #SliderPressed
        #SliderReleased

    def value_changed(self, i):
        print(i)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()