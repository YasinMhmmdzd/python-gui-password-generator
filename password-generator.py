import random
import pyperclip
from PyQt6.QtWidgets import QApplication , QWidget , QLabel , QPushButton , QLineEdit
import sys
from PyQt6.QtGui import QIcon , QFont , QPixmap
app = QApplication(sys.argv)
class MainPasswordGeneratorWindow(QWidget):
    def __init__(self):
        super(MainPasswordGeneratorWindow, self).__init__()
        self.setWindowTitle("پسورد ساز فارسی")
        self.setFont(QFont("vazir" , 17))
        self.label = QLabel("سازنده پسورد فارسی" , self)
        self.setWindowIcon(QIcon("logo.png"))
        self.label.move(410 , 5)
        self.app_logo = QLabel(self)
        logo = QPixmap("logo.png")
        self.app_logo.setPixmap(logo)
        self.setFixedSize(1000 , 500)
        self.app_logo.move(425 , 65)
        self.range_label = QLabel("تعداد کاراکتر پسورد : " , self)
        self.range = QLineEdit(self)
        self.range.setGeometry(450 , 190 , 100 , 45)
        self.range.setStyleSheet("border:1px solid #bbb;padding:10px;border-radius:10px;")
window = MainPasswordGeneratorWindow()
window.show()
sys.exit(app.exec())