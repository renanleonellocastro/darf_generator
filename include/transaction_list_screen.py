#!/usr/bin/python3

from PySide2 import QtCore
from PySide2 import QtWidgets
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

# SLOT - Process the back button clicked
#----------------------------------------------------------------------------------------------------------------------  
    def on_back_button_clicked(self):
        self.exit_consult_transactions_signal.emit()
