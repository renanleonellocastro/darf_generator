#!/usr/bin/python3

import copy
from PySide2 import QtCore
from PySide2 import QtWidgets
from darf_generator.include.stock import Stock
from darf_generator.include.stock import StockTypes
from darf_generator.include.transaction import Transaction
from darf_generator.include.transaction import TransactionTypes
from darf_generator.include.transaction_ui import Ui_Transaction

class TransactionWidget(QtWidgets.QWidget, Ui_Transaction):

# Definition of Qt Signals
#----------------------------------------------------------------------------------------------------------------------
    edit_transaction_signal = QtCore.Signal(Transaction)

# Constructor
#----------------------------------------------------------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        super(TransactionWidget, self).__init__()
        self.setupUi(self)
        self.__is_editting = False
        self.__transaction = Transaction()
        self.editButton.clicked.connect(self.on_edit_button_clicked)

# Send a signal to the control module to update the transaction properties
#----------------------------------------------------------------------------------------------------------------------
    def send_signal_to_control_to_update_the_transaction(self):
        category = StockTypes.FI if self.categoryInput.currentIndex() == 0 else StockTypes.NORMAL
        operation_type = TransactionTypes.PURCHASE if self.operationTypeInput.currentIndex() == 0\
            else TransactionTypes.SALE
        new_transaction = Transaction(self.transactionLabel.text(),self.priceInput.value(),category,\
            self.ammountInput.value(),self.faresInput.value(), self.operationDateInput.date().day(),\
            self.operationDateInput.date().month(), self.operationDateInput.date().year(),\
            operation_type, self.idInput.value())
        self.edit_transaction_signal.emit(new_transaction)

# Update graphical elements of the widget with the updated transaction values
#----------------------------------------------------------------------------------------------------------------------
    def update_transaction(self, updated_transaction):
        self.__transaction = copy.deepcopy(updated_transaction)
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
            self.send_signal_to_control_to_update_the_transaction()
