#!/usr/bin/python3

import sys
from include.gui import Ui_Gui
from PySide2 import QtWidgets

class Gui(QtWidgets.QWidget, Ui_Gui):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.center()

    def center(self):
        frame = self.frameGeometry()
        centerPosition = QtWidgets.QDesktopWidget().availableGeometry().center()
        frame.moveCenter(centerPosition)
        self.move(frame.topLeft())

app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')
application = Gui()
application.show()
app.exec_()

