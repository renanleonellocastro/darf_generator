#!/usr/bin/python3

from PySide2 import QtCore
from PySide2 import QtWidgets
from include.stock import Stock
from include.stock import StockTypes
from include.transaction import Transaction
from include.transaction import TransactionTypes
from include.transaction_widget import TransactionWidget
from include.transaction_list_ui import Ui_TransactionList

class TransactionListScreen(QtWidgets.QWidget, Ui_TransactionList):

# Definition of Qt Signals
#----------------------------------------------------------------------------------------------------------------------
    exit_consult_transactions_signal = QtCore.Signal()

# Constructor
#----------------------------------------------------------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        super(TransactionListScreen, self).__init__()
        self.setupUi(self)
        self.backButton.clicked.connect(self.on_back_button_clicked)

# Add a new transaction widget to the list
#----------------------------------------------------------------------------------------------------------------------  
    def add_transaction(self, new_transaction):
        new_transaction_widget = TransactionWidget([])
        new_transaction_widget.transactionLabel.setText(new_transaction.name)
        new_transaction_widget.priceInput.setValue(new_transaction.price)
        new_transaction_widget.ammountInput.setValue(new_transaction.ammount)
        new_transaction_widget.faresInput.setValue(new_transaction.paid_fares)
        new_transaction_widget.categoryInput.setCurrentIndex(0 if new_transaction.category == StockTypes.FI else 1)
        new_transaction_widget.idInput.setValue(new_transaction.operation_id)
        new_transaction_widget.operationTypeInput.setCurrentIndex(0 if new_transaction.operation_type ==\
            TransactionTypes.PURCHASE else 1)
        new_transaction_widget.operationDateInput.setDate(QtCore.QDate(new_transaction.operation_date.year,\
            new_transaction.operation_date.month, new_transaction.operation_date.day))
        new_transaction_widget.totalValueLabel.setText("%0.2f" %new_transaction.total_price)
        self.transactionListLayout.insertWidget(self.transactionListLayout.count() -1, new_transaction_widget)

# SLOT - Process the back button clicked
#----------------------------------------------------------------------------------------------------------------------  
    def on_back_button_clicked(self):
        self.exit_consult_transactions_signal.emit()

# SLOT - Fires when receive an add transaction signal from the control
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot(Transaction)
    def update_transaction_list_slot(self, new_transaction):
        self.add_transaction(new_transaction)
#----------------------------------------------------------------------------------------------------------------------