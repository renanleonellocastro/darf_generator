#!/usr/bin/python3

from include.stock_list_ui import Ui_StockList
from PySide2 import QtWidgets

class StockListScreen(QtWidgets.QWidget, Ui_StockList):

    def __init__(self, *args, **kwargs):
        super(StockListScreen, self).__init__()
        self.setupUi(self)
