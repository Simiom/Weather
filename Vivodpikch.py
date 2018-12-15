import sys
from PyQt5.QtGui import QPixmap
from PyQt5 import uic

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QLabel, QHBoxLayout,  QWidget


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('new.ui', self)

        self.pushButton.clicked.connect(self.run)

    def run(self):
        pixmap = QPixmap('sun2.jpg')
        self.label.setPixmap(pixmap)
        self.label.resize(pixmap.width(), pixmap.height())

        self.show()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
