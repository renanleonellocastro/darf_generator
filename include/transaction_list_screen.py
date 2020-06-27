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
    edit_transaction_signal = QtCore.Signal(Transaction)

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
        new_transaction_widget.edit_transaction_signal.connect(self.edit_transaction_slot)
        self.transactionListLayout.insertWidget(self.transactionListLayout.count() -1, new_transaction_widget)

# Find a transaction widget in the list and return it's index. In error case, return -1
#----------------------------------------------------------------------------------------------------------------------  
    def find_transaction(self, requested_transaction_id):
        for i in range(self.transactionListLayout.count() - 1):
            transaction_id_input =\
                self.transactionListLayout.itemAt(i).widget().findChild(QtWidgets.QSpinBox, "idInput")
            if transaction_id_input.value() == requested_transaction_id:
                return i
        return -1

# Remove a transaction widget from the list. In error case, return false.
#----------------------------------------------------------------------------------------------------------------------  
    def remove_transaction(self, old_transaction_id):
        transaction_position_in_list = self.find_transaction(old_transaction_id)
        if (transaction_position_in_list != -1):
            item_to_be_removed = self.transactionListLayout.takeAt(transaction_position_in_list)
            item_to_be_removed.widget().deleteLater()
            return True
        else:
            return False

# SLOT - Process the back button clicked
#----------------------------------------------------------------------------------------------------------------------  
    def on_back_button_clicked(self):
        self.exit_consult_transactions_signal.emit()

# SLOT - Fires when receive an update transaction list signal from the control
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot(Transaction)
    def update_transaction_list_slot(self, new_transaction):
        self.add_transaction(new_transaction)

# SLOT - Fires when receive an edit transaction signal from the transaction widget
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot(Transaction)
    def edit_transaction_slot(self, edit_transaction):
        self.edit_transaction_signal.emit(edit_transaction)

# SLOT - Fires when receive an update transaction widget signal from the control
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot(Transaction, bool, str)
    def update_transaction_widget_slot(self, edit_transaction, remove_item, error_message):
        if error_message != "":
            self.errorLabel.setStyleSheet("color: red")
            self.errorLabel.setText(error_message)
        else:
            if remove_item:
                if not self.remove_transaction(edit_transaction.operation_id):
                    error_message = "Erro: item da tabela não existe!"
                    self.errorLabel.setStyleSheet("color: red")
                    self.errorLabel.setText(error_message)
                else:
                    self.errorLabel.setStyleSheet("color: green")
                    self.errorLabel.setText("Transação %d removida com sucesso!" %edit_transaction.operation_id)
            else:
                transaction_widget_index = self.find_transaction(edit_transaction.operation_id)
                if transaction_widget_index != -1:
                    self.transactionListLayout.itemAt(transaction_widget_index).widget().\
                        update_transaction(edit_transaction)
                    self.errorLabel.setStyleSheet("color: green")
                    self.errorLabel.setText("Transação %d editada com sucesso!" %edit_transaction.operation_id)
                else:
                    error_message = "Erro: item da tabela não existe!"
                    self.errorLabel.setStyleSheet("color: red")
                    self.errorLabel.setText(error_message)
#----------------------------------------------------------------------------------------------------------------------
