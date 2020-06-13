#!/usr/bin/python3

import copy
from PySide2 import QtCore
from PySide2 import QtWidgets
from include.stock import Stock
from include.stock import StockTypes
from include.transaction import Transaction
from include.transaction import TransactionTypes
from include.transaction_ui import Ui_Transaction

class TransactionWidget(QtWidgets.QWidget, Ui_Transaction):

# Constructor
#----------------------------------------------------------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        super(TransactionWidget, self).__init__()
        self.setupUi(self)
        self.__is_editting = False
        self.__transaction = Transaction()
        self.editButton.clicked.connect(self.on_edit_button_clicked)

# Fill the current transaction with the values of a given one
#----------------------------------------------------------------------------------------------------------------------
    def set_stock(self, new_transaction):
        self.__transaction = copy.deepcopy(new_transaction)
        self.update_widget()

# Update transaction values with the values of the graphical elements
#----------------------------------------------------------------------------------------------------------------------
    def update_transaction(self):
        self.__transaction.name = self.transactionLabel.text()
        self.__transaction.price = self.priceInput.value()
        self.__transaction.ammount = self.ammountInput.value()
        self.__transaction.paid_fares = self.faresInput.value()
        self.__transaction.category = StockTypes.FI if self.categoryInput.currentIndex() == 0 else StockTypes.NORMAL
        self.__transaction.operation_id = self.idInput.value()
        self.__transaction.operation_type = TransactionTypes.PURCHASE if self.operationTypeInput.currentIndex() == 0\
            else TransactionTypes.SALE
        self.__transaction.set_operation_date(self.operationDateInput.date().year(),\
            self.operationDateInput.date().month(), self.operationDateInput.date().day())
        self.totalValueLabel.setText("%0.2f" %self.__transaction.total_price)

# Update graphical elements of the widget with the stock values
#----------------------------------------------------------------------------------------------------------------------
    def update_widget(self):
        self.transactionLabel.setText(self.__transaction.name)
        self.priceInput.setValue(self.__transaction.price)
        self.ammountInput.setValue(self.__transaction.ammount)
        self.faresInput.setValue(self.__transaction.paid_fares)
        self.categoryInput.setCurrentIndex(0 if self.__transaction.category == StockTypes.FI else 1)
        self.idInput.setValue(self.__transaction.operation_id)
        self.operationDateInput.setDate(QtCore.QDate(self.__transaction.operation_date.year,\
            self.__transaction.operation_date.month, self.__transaction.operation_date.day))
        self.totalValueLabel.setText("%0.2f" %self.__transaction.total_price)

# SLOT - Process the edit/save button clicked
#----------------------------------------------------------------------------------------------------------------------  
    def on_edit_button_clicked(self):
        if not self.__is_editting:
            self.__is_editting = True
            self.editButton.setText("Salvar")
            self.categoryInput.setEnabled(True)
            self.priceInput.setEnabled(True)
            self.ammountInput.setEnabled(True)
            self.faresInput.setEnabled(True)
            self.operationTypeInput.setEnabled(True)
            self.operationDateInput.setEnabled(True)
        else:
            self.__is_editting = False
            self.editButton.setText("Editar")
            self.categoryInput.setEnabled(False)
            self.priceInput.setEnabled(False)
            self.ammountInput.setEnabled(False)
            self.faresInput.setEnabled(False)
            self.operationTypeInput.setEnabled(False)
            self.operationDateInput.setEnabled(False)
            self.update_transaction()
