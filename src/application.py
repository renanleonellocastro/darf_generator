#!/usr/bin/python3

import sys
import logging
from src.gui import Gui
from PySide2 import QtWidgets
from src.control import Control

# Execute the application
#----------------------------------------------------------------------------------------------------------------------
def execute():
    app = QtWidgets.QApplication([])
    app.setStyle('Fusion')
    control = Control()
    graphical_interface = Gui()
    connect_qt_signals_and_slots(graphical_interface, control)
    graphical_interface.show()
    app.exec_()

# Connect Qt Signals and Slots
#----------------------------------------------------------------------------------------------------------------------
def connect_qt_signals_and_slots(view, control):
    view.stock_add_screen.add_stock_signal.connect(control.add_stock_slot)
    view.transaction_add_screen.add_transaction_signal.connect(control.add_transaction_slot)
    view.stock_list_screen.edit_stock_signal.connect(control.edit_stock_slot)
    view.transaction_list_screen.edit_transaction_signal.connect(control.edit_transaction_slot)
    control.update_add_stock_signal.connect(view.stock_add_screen.update_add_stock_slot)
    control.update_add_transaction_signal.connect(view.transaction_add_screen.update_add_transaction_slot)
    control.update_stock_list_signal.connect(view.stock_list_screen.update_stock_list_slot)
    control.update_transaction_list_signal.connect(view.transaction_list_screen.update_transaction_list_slot)
    control.update_stock_widget_signal.connect(view.stock_list_screen.update_stock_widget_slot)
    control.update_transaction_widget_signal.connect(view.transaction_list_screen.update_transaction_widget_slot)
    control.update_purchase_values_signal.connect(view.update_purchase_values_slot)
    control.update_sale_values_signal.connect(view.update_sale_values_slot)
    control.update_profit_values_signal.connect(view.update_profit_values_slot)
    control.update_accumulated_loss_values_signal.connect(view.update_accumulated_loss_values_slot)
    control.update_due_tax_values_signal.connect(view.update_due_tax_values_slot)

# Set log level
#----------------------------------------------------------------------------------------------------------------------
def set_log_level(self, debug):
    if (debug):
        logging.basicConfig(level=1)
        logging.debug('Log debug level activated!')
    else:
        logging.basicConfig(level=logging.INFO)

# Executable lines
#----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    execute()
#----------------------------------------------------------------------------------------------------------------------
