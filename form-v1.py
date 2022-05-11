import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle('First App')
    win.setGeometry(200,200,500,500)
    win.setWindowIcon(QIcon(r"C:\Users\Mhd Krm\Desktop\pyq\deneme.py\Fırat_Üniversitesi_logo.png"))
    win.setToolTip("Hi!")

    lbl_name = QtWidgets.QLabel(win)
    lbl_name.setText("adınız:")
    lbl_name.move(50,30)

    lbl_surname = QtWidgets.QLabel(win)
    lbl_surname.setText("Soyadınız:")
    lbl_surname.move(50,60)

    txt_name= QtWidgets.QLineEdit(win)
    txt_name.move(150,30)
    txt_surname=QtWidgets.QLineEdit(win)
    txt_surname.move(150,70)

    def clicked(self):
        print ("bottuna tıklandı: " + txt_name.text() + txt_surname.text())


    btn_save = QtWidgets.QPushButton(win)
    btn_save.setText("kaydet")
    btn_save.move(150,110)
    btn_save.clicked.connect(clicked) #consolda yazdırır.

    win.show()
    sys.exit(app.exec_())
window()
