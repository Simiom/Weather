import sys
from PyQt5.QtGui import QPixmap
from PyQt5 import uic

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QLabel, QHBoxLayout


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('unt.ui', self)

        self.pushButton.clicked.connect(self.run)

    def run(self):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap('sun.png')

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.show()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
