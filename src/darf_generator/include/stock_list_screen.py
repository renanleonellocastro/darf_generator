#!/usr/bin/python3

from PySide2 import QtCore
from PySide2 import QtWidgets
from darf_generator.include.stock import Stock
from darf_generator.include.stock import StockTypes
from darf_generator.include.stock_widget import StockWidget
from darf_generator.include.stock_list_ui import Ui_StockList

class StockListScreen(QtWidgets.QWidget, Ui_StockList):

# Definition of Qt Signals
#----------------------------------------------------------------------------------------------------------------------
    exit_consult_stocks_signal = QtCore.Signal()
    edit_stock_signal = QtCore.Signal(Stock)

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
        new_stock_widget.edit_stock_signal.connect(self.edit_stock_slot)
        self.stockListLayout.insertWidget(self.stockListLayout.count() -1, new_stock_widget)

# Find a stock widget in the list and return it's index. In error case, return -1
#----------------------------------------------------------------------------------------------------------------------  
    def find_stock(self, requested_stock_name):
        for i in range(self.stockListLayout.count() - 1):
            stock_name_label = self.stockListLayout.itemAt(i).widget().findChild(QtWidgets.QLabel, "stockLabel")
            if stock_name_label.text() == requested_stock_name:
                return i
        return -1

# Remove a stock widget from the list. In error case, return false.
#----------------------------------------------------------------------------------------------------------------------  
    def remove_stock(self, old_stock_name):
        stock_position_in_list = self.find_stock(old_stock_name)
        if (stock_position_in_list != -1):
            item_to_be_removed = self.stockListLayout.takeAt(stock_position_in_list)
            item_to_be_removed.widget().deleteLater()
            return True
        else:
            return False

# SLOT - Process the back button clicked
#----------------------------------------------------------------------------------------------------------------------  
    def on_back_button_clicked(self):
        self.exit_consult_stocks_signal.emit()

# SLOT - Fires when receive an update stock list signal from the control
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot(Stock)
    def update_stock_list_slot(self, new_stock):
        self.add_stock(new_stock)

# SLOT - Fires when receive an edit stock signal from the stock widget
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot(Stock)
    def edit_stock_slot(self, edit_stock):
        self.edit_stock_signal.emit(edit_stock)

# SLOT - Fires when receive an update stock widget signal from the control
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot(Stock, bool, str)
    def update_stock_widget_slot(self, edit_stock, remove_item, error_message):
        if error_message != "":
            self.errorLabel.setStyleSheet("color: red")
            self.errorLabel.setText(error_message)
        else:
            if remove_item:
                if not self.remove_stock(edit_stock.name):
                    error_message = "Erro: item da tabela não existe!"
                    self.errorLabel.setStyleSheet("color: red")
                    self.errorLabel.setText(error_message)
                else:
                    self.errorLabel.setStyleSheet("color: green")
                    self.errorLabel.setText("Ação %s removida com sucesso!" %edit_stock.name)
            else:
                stock_widget_index = self.find_stock(edit_stock.name)
                if stock_widget_index != -1:
                    self.stockListLayout.itemAt(stock_widget_index).widget().update_stock(edit_stock)
                    self.errorLabel.setStyleSheet("color: green")
                    self.errorLabel.setText("Ação %s editada com sucesso!" %edit_stock.name)
                else:
                    error_message = "Erro: item da tabela não existe!"
                    self.errorLabel.setStyleSheet("color: red")
                    self.errorLabel.setText(error_message)
#----------------------------------------------------------------------------------------------------------------------
