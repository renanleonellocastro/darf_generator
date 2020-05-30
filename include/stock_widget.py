#!/usr/bin/python3

from PySide2 import QtCore
from PySide2 import QtWidgets
from include.stock_ui import Ui_Stock

class StockWidget(QtWidgets.QWidget, Ui_Stock):

# Constructor
#----------------------------------------------------------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        super(StockWidget, self).__init__()
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
            self.valueInput.setEnabled(True)
            self.ammountInput.setEnabled(True)
            self.faresInput.setEnabled(True)
        else:
            self.__is_editting = False
            self.editButton.setText("Editar")
            self.categoryInput.setEnabled(False)
            self.valueInput.setEnabled(False)
            self.ammountInput.setEnabled(False)
            self.faresInput.setEnabled(False)
