#!/usr/bin/python3

from PySide2 import QtCore
from PySide2 import QtWidgets
from include.stock import Stock
from include.stock import StockTypes
from include.stock_widget import StockWidget
from include.stock_list_ui import Ui_StockList

class StockListScreen(QtWidgets.QWidget, Ui_StockList):

# Definition of Qt Signals
#----------------------------------------------------------------------------------------------------------------------
    exit_consult_stocks_signal = QtCore.Signal()

# Constructor
#----------------------------------------------------------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        super(StockListScreen, self).__init__()
        self.setupUi(self)
        self.backButton.clicked.connect(self.on_back_button_clicked)

# Add a new stock widget to the list
#----------------------------------------------------------------------------------------------------------------------  
    def add_stock(self, new_stock):
        new_stock_widget = StockWidget([])
        new_stock_widget.stockLabel.setText(new_stock.name)
        new_stock_widget.valueInput.setValue(new_stock.price)
        new_stock_widget.ammountInput.setValue(new_stock.ammount)
        new_stock_widget.faresInput.setValue(new_stock.paid_fares)
        new_stock_widget.categoryInput.setCurrentIndex(0 if new_stock.category == StockTypes.FI else 1)
        new_stock_widget.totalValueLabel.setText("%0.2f" %new_stock.total_price)
        self.stockListLayout.insertWidget(self.stockListLayout.count() -1, new_stock_widget)

# SLOT - Process the back button clicked
#----------------------------------------------------------------------------------------------------------------------  
    def on_back_button_clicked(self):
        self.exit_consult_stocks_signal.emit()

# SLOT - Fires when receive an add stock signal from the control
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot(Stock)
    def update_stock_list_slot(self, new_stock):
        self.add_stock(new_stock)
#----------------------------------------------------------------------------------------------------------------------
