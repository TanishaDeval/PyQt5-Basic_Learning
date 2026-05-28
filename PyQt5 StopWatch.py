import sys
from PyQt5.QtWidgets import (QApplication,QLabel,QPushButton,QWidget,
                             QVBoxLayout,QHBoxLayout)
from PyQt5.QtCore import QTimer,QTime,Qt
class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label=QLabel("00:00:00:00",self)
        self.start_button=QPushButton("Start",self)
        self.stop_button=QPushButton("Stop",self)
        self.reset_button=QPushButton("Reset",self)
        self.timer=QTimer(self)

        self.initUI()
    def initUI(self):
        self.setStyleSheet("""QLabel,QPushButton{
                                      font-family:Calibri;
                                      font-weight:bold;
                                      padding:25px;
                                    }
                                    QPushButton{
                                      Font-size:50px;
                                    }
                                    QLabel{
                                    font-size:100px;
                                    border-radius:30px;
                                    background-color:lightblue;
                                    }
                            """)
        self.time_label.setAlignment(Qt.AlignCenter)
        vbox=QVBoxLayout(self)
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        hbox=QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addLayout(hbox)
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_time)

    def start(self):
        self.timer.start(10)

    def stop(self):
         self.timer.stop()
    def reset(self):
        self.timer.stop()
        self.time=QTime(0,0,0,0)
        self.time_label.setText(self.format_time(self.time))
    def format_time(self,time):
        hours=time.hour()
        minutes=time.minute()
        seconds=time.second()
        millisecond=time.msec()//10
        return f"{hours:02}:{minutes:02}:{seconds:02}:{millisecond:02}"

    def update_time(self):
        self.time=self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))

def main():
    app=QApplication(sys.argv)
    stopwatch=StopWatch()
    stopwatch.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()