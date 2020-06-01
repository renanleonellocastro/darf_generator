#!/usr/bin/python3

from PySide2 import QtCore
from PySide2 import QtWidgets
from include.transaction_add_ui import Ui_TransactionAdd

class TransactionAddScreen(QtWidgets.QWidget, Ui_TransactionAdd):

# Definition of Qt Signals
#----------------------------------------------------------------------------------------------------------------------
    exit_add_transaction_signal = QtCore.Signal()

# Constructor
#----------------------------------------------------------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        super(TransactionAddScreen, self).__init__()
        self.setupUi(self)
        self.totalValueLabel.setText("0.00")
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
        if self.nameInput.text() == "":
            self.errorLabel.setStyleSheet("color: red")
            self.errorLabel.setText("Erro! Nome da transação inválido")
        elif self.ammountInput.value() == 0:
            self.errorLabel.setStyleSheet("color: red")
            self.errorLabel.setText("Erro! Quantidade não pode ser 0")
        else:
            self.errorLabel.setStyleSheet("color: green")
            self.errorLabel.setText("Transação %s salva com sucesso!" %self.nameInput.text())
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
