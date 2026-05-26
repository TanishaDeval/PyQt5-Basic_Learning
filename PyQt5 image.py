import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QPixmap,QFont
from PyQt5.QtCore import Qt
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        label=QLabel("🐯WELCOME TO THE JUNGLE🐯",self)
        label.setFont(QFont("Times New Roman",70))
        label.setStyleSheet("background-color:green;"
                            "color:white;"
                            "font-weight:bold;"
                            )
        label.resize(1910,150)

        label=QLabel(self)
        label.setAlignment(Qt.AlignCenter)
        label.setGeometry(200,150,1550,900)
        photo=QPixmap("C:\\Users\\DELL\\PycharmProjects\\PythonProject4\\profilejungle.jpg")
        label.setPixmap(photo)
        label.setScaledContents(True)




def main():
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    main()

