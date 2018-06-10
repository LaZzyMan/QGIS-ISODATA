from PyQt5.QtWidgets import QApplication, QProgressBar, QPushButton
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QBasicTimer
import os


class ProgressBar(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self)

        self.setGeometry(800, 400, 400, 100)
        self.setWindowOpacity(0)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        with open(os.path.join(os.path.dirname(__file__), 'src/black.qss'), encoding='utf-8') as qss:
            self.setStyleSheet(qss.read())
        self.setWindowTitle('请稍候')
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 30, 340, 40)

    def setMax(self, max):
        self.pbar.setMaximum(max)

    def clear(self):
        self.pbar.setValue(0)

    def setValue(self, value):
        self.pbar.setValue(value)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    qb = ProgressBar()
    qb.show()
    sys.exit(app.exec_())
