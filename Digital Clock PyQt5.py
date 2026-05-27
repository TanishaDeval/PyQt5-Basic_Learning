import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel
from PyQt5.QtCore import QTimer,QTime,Qt
from PyQt5.QtGui import QFontDatabase,QFont
class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label=QLabel(self)
        self.timer=QTimer(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(700,300,400,150)
        self.time_label.setGeometry(0,0,400,150)
        self.time_label.setStyleSheet("background-color:black;"
                                      "color:hsv(108, 60%, 78%);"
                                      "font-size:94px;")
        self.time_label.setAlignment(Qt.AlignCenter)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        font_id=QFontDatabase.addApplicationFont("C:\\Users\\DELL\\PycharmProjects"
                                                 "\\PythonProject4\\Technology-BoldItalic.ttf")
        font_family=QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font=QFont(font_family,200)
        self.time_label.setFont(my_font)
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)

def main():
   app=QApplication(sys.argv)
   clock=DigitalClock()
   clock.show()
   sys.exit(app.exec_())
if __name__=="__main__":
    main()