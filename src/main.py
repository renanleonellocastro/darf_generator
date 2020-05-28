#!/usr/bin/python3

import sys
from PySide2 import QtWidgets
from include.gui_ui import Ui_Gui
from include.stock_list_screen import StockListScreen

class Gui(QtWidgets.QWidget, Ui_Gui):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__stock_list_screen = StockListScreen()
        self.setupUi(self)
        self.center()
        self.consultStockButton.clicked.connect(self.consultStocks)

    def center(self):
        frame = self.frameGeometry()
        centerPosition = QtWidgets.QDesktopWidget().availableGeometry().center()
        frame.moveCenter(centerPosition)
        self.move(frame.topLeft())
    
    def consultStocks(self):
        self.__stock_list_screen.show()

app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')
application = Gui()
application.show()
app.exec_()
