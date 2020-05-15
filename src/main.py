#!/usr/bin/python3

import sys
from gui import Ui_Form  # importing our generated file
from PySide2 import QtWidgets

class Gui(QtWidgets.QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

app = QtWidgets.QApplication(sys.argv)
application = Gui()
application.show()
app.exec_()

