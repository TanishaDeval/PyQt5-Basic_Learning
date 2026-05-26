import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.button=QPushButton("Click",self)
        self.label=QLabel("Hello",self)
        self.label.setGeometry(680,600,570,250)
        self.label.setFont(QFont("Times New Roman",60))
        self.label.setStyleSheet(
                                 "Font-weight:bold;"
                                 "color:white;"
                                 "background-color:black;")
        self.label.setAlignment(Qt.AlignCenter)
        self.initUI()

    def initUI(self):
        self.button.setGeometry(650,300,600,200)
        self.button.setStyleSheet("color:white;"
                                  "background-color:grey;"
                                  "Font-size:50px;"
                                  "Font-style:Times New Roman;"
                                  "font-weight:bold;")
        self.button.clicked.connect(self.on_click)
    def on_click(self):
        self.label.setText("Bye")
        print("clicked")


def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__=="__main__" :
    main()