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
        self.range_label.move(550 , 195)
        self.range = QLineEdit(self)
        self.range.setGeometry(450 , 190 , 100 , 45)
        self.range.setStyleSheet("border:1px solid #bbb;padding:10px;border-radius:10px;")
        self.set_btn = QPushButton("ساخت پسورد" , self)
        self.set_btn.setGeometry(225 , 190 , 200 , 45)
        self.set_btn.setStyleSheet("background-color:#060a12;color:white;border-radius:10px;outline:none;")
        self.set_btn.clicked.connect(self.set_pass)
        self.chars = []
        self.allow_chars = ('aqzswxdecrfvgtbhynjumki,lo.p;[1234567890-=!@#$%^&*()_+/*-`~')
    def set_pass(self):
        if self.range >= 10 :
            for char in range(self.range):
                char = random.choice(self.allow_chars)
                self.chars.append(char)
            new_password = ''.join(self.chars)

window = MainPasswordGeneratorWindow()
window.show()
sys.exit(app.exec())