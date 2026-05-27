import sys
from PyQt5.QtWidgets import QWidget,QApplication,QMainWindow,QPushButton,QHBoxLayout
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1=QPushButton("#1")
        self.button2=QPushButton("#2")
        self.button3=QPushButton("#3")
        self.initUI()


    def initUI(self):
        central_widget=QWidget()
        self.setCentralWidget(central_widget)

        hbox=QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        central_widget.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet("""
            QPushButton{font-size:40px;
                        font-family:"Times New Roman;
                        font-weight:bold;
                        color:white;
                        margin:25px;
                        border:3px solid;
                        border-radius:15px;
                        }
            QPushButton#button1{
                    background-color:blue;}
            QPushButton#button2{
                    background-color:green;}
            QPushButton#button3{
                    background-color:yellow;}
            QPushButton#button1:hover{
                    background-color:lightblue;}
            QPushButton#button2:hover{
                    background-color:lightgreen;}
            QPushButton#button3:hover{
                    background-color:lightyellow;}
                    
                                
            """)




def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit=app.exec_()
if __name__=="__main__":
    main()