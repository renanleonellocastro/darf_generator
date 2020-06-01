#!/usr/bin/python3

from PySide2 import QtCore
from PySide2 import QtWidgets
from include.transaction_ui import Ui_Transaction

class TransactionWidget(QtWidgets.QWidget, Ui_Transaction):

# Constructor
#----------------------------------------------------------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        super(TransactionWidget, self).__init__()
        self.setupUi(self)
        self.__is_editting = False
        self.editButton.clicked.connect(self.on_edit_button_clicked)

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
