#!/usr/bin/python3

from PySide2 import QtCore
from PySide2 import QtWidgets
from darf_generator.include.stock import Stock
from darf_generator.include.stock import StockTypes
from darf_generator.include.transaction import Transaction
from darf_generator.include.transaction import TransactionTypes
from darf_generator.include.transaction_add_ui import Ui_TransactionAdd

class TransactionAddScreen(QtWidgets.QWidget, Ui_TransactionAdd):

# Definition of Qt Signals
#----------------------------------------------------------------------------------------------------------------------
    exit_add_transaction_signal = QtCore.Signal()
    add_transaction_signal = QtCore.Signal(Transaction)

# Constructor
#----------------------------------------------------------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        super(TransactionAddScreen, self).__init__()
        self.setupUi(self)
        self.__transaction = Transaction()
        self.totalValueLabel.setText("0.00")
        self.operationDateInput.setDate(QtCore.QDate.currentDate())
        self.nameInput.textChanged.connect(self.on_name_changed)
        self.priceInput.valueChanged.connect(self.on_price_changed)
        self.ammountInput.valueChanged.connect(self.on_ammount_changed)
        self.saveButton.clicked.connect(self.on_save_button_clicked)
        self.backButton.clicked.connect(self.on_back_button_clicked)

# SLOT - Change title name when transaction name changes
#----------------------------------------------------------------------------------------------------------------------  
    def on_name_changed(self, new_name):
        self.transactionNameLabel.setText(new_name)

# SLOT - Change total price when price changed
#----------------------------------------------------------------------------------------------------------------------  
    def on_price_changed(self, new_price):
        self.totalValueLabel.setText("%0.2f" %(new_price * self.ammountInput.value()))

# SLOT - Change total price when ammount changed
#----------------------------------------------------------------------------------------------------------------------  
    def on_ammount_changed(self, new_ammount):
        self.totalValueLabel.setText("%0.2f" %(new_ammount * self.priceInput.value()))

# SLOT - Save the transaction when user press the save button
#----------------------------------------------------------------------------------------------------------------------  
    def on_save_button_clicked(self):
        self.__transaction.name = self.nameInput.text()
        self.__transaction.price = self.priceInput.value()
        self.__transaction.ammount = self.ammountInput.value()
        self.__transaction.paid_fares = self.faresInput.value()
        self.__transaction.category = StockTypes.FI if self.categoryInput.currentIndex() == 0 else StockTypes.NORMAL
        self.__transaction.operation_id = self.idInput.value()
        self.__transaction.operation_type = TransactionTypes.PURCHASE if self.operationTypeInput.currentIndex() == 0\
            else TransactionTypes.SALE
        self.__transaction.set_operation_date(self.operationDateInput.date().year(),\
            self.operationDateInput.date().month(), self.operationDateInput.date().day())
        self.add_transaction_signal.emit(self.__transaction)

# SLOT - Fires when receive the update signal from the control
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot(str)
    def update_add_transaction_slot(self, error_message):
        if error_message != "":
            self.errorLabel.setStyleSheet("color: red")
            self.errorLabel.setText(error_message)
        else:
            self.errorLabel.setStyleSheet("color: green")
            self.errorLabel.setText("Transação %d salva com sucesso!" %self.idInput.value())
            self.nameInput.setText("")
            self.categoryInput.setCurrentIndex(1)
            self.priceInput.setValue(0.0)
            self.ammountInput.setValue(0)
            self.faresInput.setValue(0.0)
            self.idInput.setValue(0)
            self.operationTypeInput.setCurrentIndex(0)
            self.operationDateInput.setDate(QtCore.QDate.currentDate())

# SLOT - Process the back button clicked
#----------------------------------------------------------------------------------------------------------------------  
    def on_back_button_clicked(self):
        self.exit_add_transaction_signal.emit()
