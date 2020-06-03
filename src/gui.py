#!/usr/bin/python3

import logging
from PySide2 import QtCore
from PySide2 import QtWidgets
from include.gui_ui import Ui_Gui
from include.stock_add_screen import StockAddScreen
from include.stock_list_screen import StockListScreen
from include.transaction_add_screen import TransactionAddScreen
from include.transaction_list_screen import TransactionListScreen

class Gui(QtWidgets.QWidget, Ui_Gui):

# Constructor
#----------------------------------------------------------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stock_add_screen = StockAddScreen(self)
        self.stock_list_screen = StockListScreen(self)
        self.__transaction_add_screen = TransactionAddScreen(self)
        self.__transaction_list_screen = TransactionListScreen(self)
        self.setupUi(self)
        self.center(self)
        self.center(self.stock_add_screen)
        self.center(self.stock_list_screen)
        self.center(self.__transaction_add_screen)
        self.center(self.__transaction_list_screen)
        self.addStockButton.clicked.connect(self.on_add_stock_button_clicked)
        self.consultStockButton.clicked.connect(self.on_consult_stocks_button_clicked)
        self.addTransactionButton.clicked.connect(self.on_add_transaction_button_clicked)
        self.consultTransactionButton.clicked.connect(self.on_consult_transactions_button_clicked)
        self.stock_add_screen.exit_add_stock_signal.connect(self.exit_add_stock)
        self.stock_list_screen.exit_consult_stocks_signal.connect(self.exit_consult_stocks)
        self.__transaction_add_screen.exit_add_transaction_signal.connect(self.exit_add_transaction)
        self.__transaction_list_screen.exit_consult_transactions_signal.connect(self.exit_consult_transactions)

# Center the widget in the middle of the display
#----------------------------------------------------------------------------------------------------------------------
    def center(self, screen):
        frame = screen.frameGeometry()
        centerPosition = QtWidgets.QDesktopWidget().availableGeometry().center()
        frame.moveCenter(centerPosition)
        screen.move(frame.topLeft())

# SLOT - Add stock button clicked
#----------------------------------------------------------------------------------------------------------------------
    def on_add_stock_button_clicked(self):
        self.stock_add_screen.show()
        self.close()

# SLOT - Consult the user stocks button clicked
#----------------------------------------------------------------------------------------------------------------------
    def on_consult_stocks_button_clicked(self):
        self.stock_list_screen.show()
        self.close()

# SLOT - Add transaction button clicked
#----------------------------------------------------------------------------------------------------------------------
    def on_add_transaction_button_clicked(self):
        self.__transaction_add_screen.show()
        self.close()

# SLOT - Consult the user transactions button clicked
#----------------------------------------------------------------------------------------------------------------------
    def on_consult_transactions_button_clicked(self):
        self.__transaction_list_screen.show()
        self.close()

# SLOT - Fires when user click in back button on add stock screen
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot()
    def exit_add_stock(self):
        self.show()
        self.stock_add_screen.close()

# SLOT - Fires when user click in back button on consult stocks screen
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot()
    def exit_consult_stocks(self):
        self.show()
        self.stock_list_screen.close()

# SLOT - Fires when user click in back button on add transaction screen
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot()
    def exit_add_transaction(self):
        self.show()
        self.__transaction_add_screen.close()

# SLOT - Fires when user click in back button on consult transactions screen
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot()
    def exit_consult_transactions(self):
        self.show()
        self.__transaction_list_screen.close()

# Runs when the screen in closing
#----------------------------------------------------------------------------------------------------------------------
    def closeEvent(self, event):
        logging.debug("Fechando...")

#----------------------------------------------------------------------------------------------------------------------
