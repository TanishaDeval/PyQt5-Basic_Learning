import sys
from PyQt5.QtWidgets import QApplication,QMainWindow ,QRadioButton,QButtonGroup
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.radiobutton1=QRadioButton("Visa",self)
        self.radiobutton2=QRadioButton("Credit-card",self)
        self.radiobutton3=QRadioButton("Offline",self)
        self.radiobutton4=QRadioButton("Online",self)
        self.buttongroup1=QButtonGroup(self)
        self.buttongroup2=QButtonGroup(self)
        self.initUI()

    def initUI(self):
        self.radiobutton1.setGeometry(0,0,300,100)
        self.radiobutton2.setGeometry(0,100,300,100)
        self.radiobutton3.setGeometry(0,200,300,100)
        self.radiobutton4.setGeometry(0,300,300,100)

        self.buttongroup1.addButton(self.radiobutton1)
        self.buttongroup1.addButton(self.radiobutton2)
        self.buttongroup2.addButton(self.radiobutton3)
        self.buttongroup2.addButton(self.radiobutton4)

        self.setStyleSheet("QRadioButton{"
                          "font-size:40px;"
                          "font-family:Times New Roman;"
                          "background-color:skyblue;"
                          "color:white;"
                          "font-weight:bold;"
                            "}")
        radio_buttons=[self.radiobutton1,self.radiobutton2,self.radiobutton3,self.radiobutton4]
        for radio_button in radio_buttons:
            radio_button.toggled.connect(self.radio_button_changed)
        #self.radiobutton1.toggled.connect(self.radio_button_changed)
        #self.radiobutton2.toggled.connect(self.radio_button_changed)
        #self.radiobutton3.toggled.connect(self.radio_button_changed)
        #self.radiobutton4.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self):
           radiobutton=self.sender()
           if radiobutton.isChecked():
                print(f"{radiobutton.text()} is selected")

def main():
  app=QApplication(sys.argv)
  window=MainWindow()
  window.show()
  sys.exit(app.exec_())
if __name__=="__main__" :
    main()