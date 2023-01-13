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
        self.setFont(QFont("vazir" , 25))
        self.label = QLabel("سلام" , self)

window = MainPasswordGeneratorWindow()
window.show()
sys.exit(app.exec())