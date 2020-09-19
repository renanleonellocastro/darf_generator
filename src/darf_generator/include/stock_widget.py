#!/usr/bin/python3

import copy
from PySide2 import QtCore
from PySide2 import QtWidgets
from darf_generator.include.stock import Stock
from darf_generator.include.stock import StockTypes
from darf_generator.include.stock_ui import Ui_Stock

class StockWidget(QtWidgets.QWidget, Ui_Stock):

# Definition of Qt Signals
#----------------------------------------------------------------------------------------------------------------------
    edit_stock_signal = QtCore.Signal(Stock)

# Constructor
#----------------------------------------------------------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        super(StockWidget, self).__init__()
        self.setupUi(self)
        self.__is_editting = False
        self.__stock = Stock()
        self.editButton.clicked.connect(self.on_edit_button_clicked)

# Send a signal to the control module to update the stock properties
#----------------------------------------------------------------------------------------------------------------------
    def send_signal_to_control_to_update_the_stock(self):
        category = StockTypes.FI if self.categoryInput.currentIndex() == 0 else StockTypes.NORMAL
        new_stock = Stock(self.stockLabel.text(),self.valueInput.value(),category,\
            self.ammountInput.value(),self.faresInput.value())      
        self.edit_stock_signal.emit(new_stock)

# Update graphical elements of the widget with the updated stock values
#----------------------------------------------------------------------------------------------------------------------
    def update_stock(self, updated_stock):
        self.__stock = copy.deepcopy(updated_stock)
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
            self.send_signal_to_control_to_update_the_stock()
