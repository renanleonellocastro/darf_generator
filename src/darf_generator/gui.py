#!/usr/bin/python3

import logging
from datetime import date
from PySide2 import QtCore
from PySide2 import QtWidgets
from darf_generator.include.gui_ui import Ui_Gui
from darf_generator.include.stock_add_screen import StockAddScreen
from darf_generator.include.stock_list_screen import StockListScreen
from darf_generator.include.transaction_add_screen import TransactionAddScreen
from darf_generator.include.transaction_list_screen import TransactionListScreen
from darf_generator.include.darf_generation_screen import DarfGenerationScreen

class Gui(QtWidgets.QWidget, Ui_Gui):

# Definition of Qt Signals
#----------------------------------------------------------------------------------------------------------------------
    cei_login_signal = QtCore.Signal(str, str)
    cei_import_stocks_signal = QtCore.Signal(date)
    cei_import_transactions_signal = QtCore.Signal(date)

# Constructor
#----------------------------------------------------------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stock_add_screen = StockAddScreen(self)
        self.stock_list_screen = StockListScreen(self)
        self.transaction_add_screen = TransactionAddScreen(self)
        self.transaction_list_screen = TransactionListScreen(self)
        self.darf_generation_screen = DarfGenerationScreen(self)
        self.setupUi(self)
        self.center(self)
        self.show_cei_login_buttons()
        self.hide_cei_import_buttons()
        self.hide_cei_progress_bar()
        self.hide_cei_error_message()
        self.timer_cei_login = QtCore.QTimer()
        self.timer_cei_import = QtCore.QTimer()
        self.timer_cei_login.setInterval(3000)
        self.timer_cei_import.setInterval(3000)
        self.ceiLoginButton.setFocus()
        self.ceiLoginButton.clicked.connect(self.on_cei_login_button_clicked)
        self.ceiImportStocksButton.clicked.connect(self.on_cei_import_stocks_button_clicked)
        self.ceiImportTransactionsButton.clicked.connect(self.on_cei_import_transactions_button_clicked)
        self.addStockButton.clicked.connect(self.on_add_stock_button_clicked)
        self.consultStockButton.clicked.connect(self.on_consult_stocks_button_clicked)
        self.addTransactionButton.clicked.connect(self.on_add_transaction_button_clicked)
        self.consultTransactionButton.clicked.connect(self.on_consult_transactions_button_clicked)
        self.darfGenerationButton.clicked.connect(self.on_darf_generation_button_clicked)
        self.stock_add_screen.exit_add_stock_signal.connect(self.exit_add_stock)
        self.stock_list_screen.exit_consult_stocks_signal.connect(self.exit_consult_stocks)
        self.transaction_add_screen.exit_add_transaction_signal.connect(self.exit_add_transaction)
        self.transaction_list_screen.exit_consult_transactions_signal.connect(self.exit_consult_transactions)
        self.darf_generation_screen.exit_darf_generation_signal.connect(self.exit_darf_generation)
        self.timer_cei_login.timeout.connect(self.back_to_cei_screen_state_before_login)
        self.timer_cei_import.timeout.connect(self.back_to_cei_screen_state_before_import)

# Center the widget in the middle of the display
#----------------------------------------------------------------------------------------------------------------------
    def center(self, screen):
        frame = screen.frameGeometry()
        centerPosition = QtWidgets.QDesktopWidget().availableGeometry().center()
        frame.moveCenter(centerPosition)
        screen.move(frame.topLeft())

# Convert python date to month name in portuguese and year
#----------------------------------------------------------------------------------------------------------------------
    def date_to_month_name_and_year(self, date_to_convert):
        month_name_list = ['','JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO',
            'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']
        return month_name_list[date_to_convert.month] + '/' + str(date_to_convert.year)

# Convert month name in portuguese and year to python date
#----------------------------------------------------------------------------------------------------------------------
    def month_name_and_year_to_date(self, month_and_year_to_convert):
        month_convert_dict = {'JANEIRO': 1, 'FEVEREIRO': 2, 'MARÇO': 3, 'ABRIL': 4, 'MAIO': 5, 'JUNHO': 6, 'JULHO': 7,
            'AGOSTO': 8, 'SETEMBRO': 9, 'OUTUBRO': 10, 'NOVEMBRO': 11, 'DEZEMBRO': 12}
        day = 1
        month = month_convert_dict[month_and_year_to_convert.split('/')[0]]
        year = int(month_and_year_to_convert.split('/')[1])
        return date(year, month, day)

# Hide the cei import buttons in the screen
#----------------------------------------------------------------------------------------------------------------------
    def hide_cei_import_buttons(self):
        self.ceiImportStocksButton.hide()
        self.ceiImportTransactionsButton.hide()
        self.ceiMonthsList.hide()
        self.ceiOptionsFrame.hide()

# Hide the cei progress bar in the screen
#----------------------------------------------------------------------------------------------------------------------
    def hide_cei_progress_bar(self):
        self.ceiProgressBar.hide()

# Hide the cei login buttons in the screen
#----------------------------------------------------------------------------------------------------------------------
    def hide_cei_login_buttons(self):
        self.ceiCpfInput.hide()
        self.ceiPasswordInput.hide()
        self.ceiLoginButton.hide()
        self.ceiLoginFrame.hide()

# Hide the cei error message in the screen
#----------------------------------------------------------------------------------------------------------------------
    def hide_cei_error_message(self):
        self.ceiErrorMessage.hide()

# Show the cei import buttons in the screen
#----------------------------------------------------------------------------------------------------------------------
    def show_cei_import_buttons(self):
        self.ceiImportStocksButton.show()
        self.ceiImportTransactionsButton.show()
        self.ceiMonthsList.show()
        self.ceiOptionsFrame.show()

# Show the cei progress bar in the screen
#----------------------------------------------------------------------------------------------------------------------
    def show_cei_progress_bar(self):
        self.ceiProgressBar.show()

# Show the cei login buttons in the screen
#----------------------------------------------------------------------------------------------------------------------
    def show_cei_login_buttons(self):
        self.ceiCpfInput.show()
        self.ceiPasswordInput.show()
        self.ceiLoginButton.show()
        self.ceiLoginFrame.show()

# Show the cei error message in the screen
#----------------------------------------------------------------------------------------------------------------------
    def show_cei_error_message(self, error_message):
        self.ceiErrorMessage.setText(error_message)
        self.ceiErrorMessage.show()

# Change cei screen widgets to go back to state before cei login
#----------------------------------------------------------------------------------------------------------------------
    def back_to_cei_screen_state_before_login(self):
        self.timer_cei_login.stop()
        self.hide_cei_progress_bar()
        self.hide_cei_error_message()
        self.show_cei_login_buttons()

# Change cei screen widgets to go back to state before cei import
#----------------------------------------------------------------------------------------------------------------------
    def back_to_cei_screen_state_before_import(self):
        self.timer_cei_import.stop()
        self.hide_cei_progress_bar()
        self.hide_cei_error_message()
        self.show_cei_import_buttons()

# Enable or disable the darf generation button and update the darf value in darf generation screen
#----------------------------------------------------------------------------------------------------------------------
    def update_darf_generation_info(self, total_darf_value):
        self.darf_generation_screen.value = total_darf_value
        if self.darf_generation_screen.value > 10:
            self.darfGenerationButton.setEnabled(True)
        else:
            self.darfGenerationButton.setEnabled(False)

# SLOT - Cei login button clicked
#----------------------------------------------------------------------------------------------------------------------
    def on_cei_login_button_clicked(self):
        self.hide_cei_login_buttons()
        self.show_cei_progress_bar()
        self.cei_login_signal.emit(self.ceiCpfInput.text(), self.ceiPasswordInput.text())

# SLOT - Cei import stocks button clicked
#----------------------------------------------------------------------------------------------------------------------
    def on_cei_import_stocks_button_clicked(self):
        self.hide_cei_import_buttons()
        self.show_cei_progress_bar()
        self.cei_import_stocks_signal.emit(self.month_name_and_year_to_date(self.ceiMonthsList.currentText()))

# SLOT - Cei import transactions button clicked
#----------------------------------------------------------------------------------------------------------------------
    def on_cei_import_transactions_button_clicked(self):
        self.hide_cei_import_buttons()
        self.show_cei_progress_bar()
        self.cei_import_transactions_signal.emit(self.month_name_and_year_to_date(self.ceiMonthsList.currentText()))

# SLOT - Add stock button clicked
#----------------------------------------------------------------------------------------------------------------------
    def on_add_stock_button_clicked(self):
        self.stock_add_screen.setGeometry(self.geometry())
        self.stock_add_screen.show()
        self.close()

# SLOT - Consult the user stocks button clicked
#----------------------------------------------------------------------------------------------------------------------
    def on_consult_stocks_button_clicked(self):
        self.stock_list_screen.setGeometry(self.geometry())
        self.stock_list_screen.show()
        self.close()

# SLOT - Add transaction button clicked
#----------------------------------------------------------------------------------------------------------------------
    def on_add_transaction_button_clicked(self):
        self.transaction_add_screen.setGeometry(self.geometry())
        self.transaction_add_screen.show()
        self.close()

# SLOT - Consult the user transactions button clicked
#----------------------------------------------------------------------------------------------------------------------
    def on_consult_transactions_button_clicked(self):
        self.transaction_list_screen.setGeometry(self.geometry())
        self.transaction_list_screen.show()
        self.close()

# SLOT - Darf generation button clicked
#----------------------------------------------------------------------------------------------------------------------
    def on_darf_generation_button_clicked(self):
        self.darf_generation_screen.setGeometry(self.geometry())
        self.darf_generation_screen.show()
        self.close()

# SLOT - Fires when user click in back button on add stock screen
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot()
    def exit_add_stock(self):
        self.setGeometry(self.stock_add_screen.geometry())
        self.show()
        self.stock_add_screen.close()

# SLOT - Fires when user click in back button on consult stocks screen
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot()
    def exit_consult_stocks(self):
        self.setGeometry(self.stock_list_screen.geometry())
        self.show()
        self.stock_list_screen.close()

# SLOT - Fires when user click in back button on add transaction screen
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot()
    def exit_add_transaction(self):
        self.setGeometry(self.transaction_add_screen.geometry())
        self.show()
        self.transaction_add_screen.close()

# SLOT - Fires when user click in back button on consult transactions screen
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot()
    def exit_consult_transactions(self):
        self.setGeometry(self.transaction_list_screen.geometry())
        self.show()
        self.transaction_list_screen.close()

# SLOT - Fires when user click in back button on darf generation screen
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot()
    def exit_darf_generation(self):
        self.setGeometry(self.darf_generation_screen.geometry())
        self.show()
        self.darf_generation_screen.close()

# SLOT - Fires when receive a signal meaning that the user logged in cei or failed to log in cei
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot(list, str)
    def update_cei_login_slot(self, last_five_months, error_message):
        if error_message == "":
            self.hide_cei_progress_bar()
            self.show_cei_import_buttons()
            for month in last_five_months:
                self.ceiMonthsList.addItem(self.date_to_month_name_and_year(month))
        else:
            self.show_cei_error_message(error_message)
            self.timer_cei_login.start()

# SLOT - Fires when receive a signal meaning that the user imported cei stocks or failed to import
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot(str)
    def update_cei_import_stocks_slot(self, error_message):
        if error_message == "":
            self.hide_cei_progress_bar()
            self.show_cei_import_buttons()
            self.ceiImportStocksButton.setEnabled(False)
        else:
            self.show_cei_error_message(error_message)
            self.timer_cei_import.start()

# SLOT - Fires when receive a signal meaning that the user imported cei transactions or failed to import
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot(str)
    def update_cei_import_transactions_slot(self, error_message):
        if error_message == "":
            self.hide_cei_progress_bar()
            self.show_cei_import_buttons()
            self.ceiImportTransactionsButton.setEnabled(False)
        else:
            self.show_cei_error_message(error_message)
            self.timer_cei_import.start()

# SLOT - Fires when receive a signal with the purchase values from the control
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot(float, float, float)
    def update_purchase_values_slot(self, swing_trade, day_trade, fi):
        self.swingTradeTotalPurchaseLabel.setText("R$ %.2f"%swing_trade)
        self.dayTradeTotalPurchaseLabel.setText("R$ %.2f"%day_trade)
        self.realEstateFundsTotalPurchaseLabel.setText("R$ %.2f"%fi)

# SLOT - Fires when receive a signal with the sale values from the control
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot(float, float, float)
    def update_sale_values_slot(self, swing_trade, day_trade, fi):
        self.swingTradeTotalSoldLabel.setText("R$ %.2f"%swing_trade)
        self.dayTradeTotalSoldLabel.setText("R$ %.2f"%day_trade)
        self.realEstateFundsTotalSoldLabel.setText("R$ %.2f"%fi)

# SLOT - Fires when receive a signal with the profit values from the control
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot(float, float, float)
    def update_profit_values_slot(self, swing_trade, day_trade, fi):
        self.swingTradeTotalProfitLabel.setText("R$ %.2f"%swing_trade)
        self.dayTradeTotalProfitLabel.setText("R$ %.2f"%day_trade)
        self.realEstateFundsTotalProfitLabel.setText("R$ %.2f"%fi)

# SLOT - Fires when receive a signal with the accumulated loss values from the control
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot(float, float, float)
    def update_accumulated_loss_values_slot(self, swing_trade, day_trade, fi):
        self.swingTradeAccumulatedLossLabel.setText("R$ %.2f"%swing_trade)
        self.dayTradeAccumulatedLossLabel.setText("R$ %.2f"%day_trade)
        self.realEstateFundsAccumulatedLossLabel.setText("R$ %.2f"%fi)

# SLOT - Fires when receive a signal with the due tax values from the control
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot(float, float, float, float)
    def update_due_tax_values_slot(self, swing_trade, day_trade, fi, total_darf):
        self.swingTradeDueTaxLabel.setText("R$ %.2f"%swing_trade)
        self.dayTradeDueTaxLabel.setText("R$ %.2f"%day_trade)
        self.realEstateFundsDueTaxLabel.setText("R$ %.2f"%fi)
        self.darfValueOutputLabel.setText("R$ %.2f"%total_darf)
        self.update_darf_generation_info(total_darf)

# Runs when the screen in closing
#----------------------------------------------------------------------------------------------------------------------
    def closeEvent(self, event):
        logging.debug("Fechando...")

#----------------------------------------------------------------------------------------------------------------------
