#!/usr/bin/python3

from include.stock_ui import Ui_Stock
from PySide2 import QtWidgets

class StockWidget(QtWidgets.QWidget, Ui_Stock):

    def __init__(self, *args, **kwargs):
        super(StockWidget, self).__init__()
        self.setupUi(self)
