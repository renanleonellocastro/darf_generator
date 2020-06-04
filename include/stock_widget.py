#!/usr/bin/python3

import copy
from PySide2 import QtCore
from PySide2 import QtWidgets
from include.stock import Stock
from include.stock import StockTypes
from include.stock_ui import Ui_Stock

class StockWidget(QtWidgets.QWidget, Ui_Stock):

# Constructor
#----------------------------------------------------------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        super(StockWidget, self).__init__()
        self.setupUi(self)
        self.__is_editting = False
        self.__stock = Stock()
        self.editButton.clicked.connect(self.on_edit_button_clicked)

# Fill the current stock with the values of a given one
#----------------------------------------------------------------------------------------------------------------------
    def set_stock(self, new_stock):
        self.__stock = copy.deepcopy(new_stock)
        self.update_widget()

# Update stock values with the values of the graphical elements
#----------------------------------------------------------------------------------------------------------------------
    def update_stock(self):
        self.__stock.name = self.stockLabel.text()
        self.__stock.price = self.valueInput.value()
        self.__stock.ammount = self.ammountInput.value()
        self.__stock.paid_fares = self.faresInput.value()
        self.__stock.category = StockTypes.FI if self.categoryInput.currentIndex == 0 else StockTypes.NORMAL
        self.totalValueLabel.setText("%0.2f" %self.__stock.total_price)

# Update graphical elements of the widget with the stock values
#----------------------------------------------------------------------------------------------------------------------
    def update_widget(self):
        self.stockLabel.setText(self.__stock.name)
        self.valueInput.setValue(self.__stock.price)
        self.ammountInput.setValue(self.__stock.ammount)
        self.faresInput.setValue(self.__stock.paid_fares)
        self.categoryInput.setCurrentIndex(0 if self.__stock.category == StockTypes.FI else 1)
        self.totalValueLabel.setText("%0.2f" %self.__stock.total_price)

# SLOT - Process the edit/save button clicked
#----------------------------------------------------------------------------------------------------------------------  
    def on_edit_button_clicked(self):
        if not self.__is_editting:
            self.__is_editting = True
            self.editButton.setText("Salvar")
            self.categoryInput.setEnabled(True)
            self.valueInput.setEnabled(True)
            self.ammountInput.setEnabled(True)
            self.faresInput.setEnabled(True)
        else:
            self.__is_editting = False
            self.editButton.setText("Editar")
            self.categoryInput.setEnabled(False)
            self.valueInput.setEnabled(False)
            self.ammountInput.setEnabled(False)
            self.faresInput.setEnabled(False)
            self.update_stock()
