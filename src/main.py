#!/usr/bin/python3

from PyQt5 import QtWidgets
from gui import Ui_Form  # importing our generated file
import sys

class Gui(QtWidgets.QWidget):

    def __init__(self):
        super(Gui, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

app = QtWidgets.QApplication([])
application = Gui()
application.show()
sys.exit(app.exec())

