import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('First App')
        self.setGeometry(200,200,500,500)
        self.setWindowIcon(QIcon(r"C:\Users\Mhd Krm\Desktop\pyq\deneme.py\Fırat_Üniversitesi_logo.png"))
        self.setToolTip("Hi!")
        self.initUI()

    def initUI(self):    
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText("adınız:")
        self.lbl_name.move(50,30)

        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText("Soyadınız:")
        self.lbl_surname.move(50,60)

        self.txt_name= QtWidgets.QLineEdit(self)
        self.txt_name.move(150,30)
        self.txt_surname=QtWidgets.QLineEdit(self)
        self.txt_surname.move(150,70)


        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("kaydet")
        self.btn_save.move(150,110)
        self.btn_save.clicked.connect(self.clicked) #consolda yazdırır.
    def clicked(self):
        print ("bottuna tıklandı: " + self.txt_name.text() + self.txt_surname.text())
    
def Window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
    
Window()
