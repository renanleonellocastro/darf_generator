#!/usr/bin/python3

import sys
import logging
from PySide2 import QtCore
from PySide2 import QtWidgets
from include.gui_ui import Ui_Gui
from include.stock_list_screen import StockListScreen

class Gui(QtWidgets.QWidget, Ui_Gui):

# Constructor
#----------------------------------------------------------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__stock_list_screen = StockListScreen(self)
        self.setupUi(self)
        self.center(self)
        self.center(self.__stock_list_screen)
        self.consultStockButton.clicked.connect(self.on_consult_stocks_button_clicked)
        self.__stock_list_screen.exit_consult_stocks_signal.connect(self.exit_consult_stocks)

# Center the widget in the middle of the display
#----------------------------------------------------------------------------------------------------------------------
    def center(self, screen):
        frame = screen.frameGeometry()
        centerPosition = QtWidgets.QDesktopWidget().availableGeometry().center()
        frame.moveCenter(centerPosition)
        screen.move(frame.topLeft())

# SLOT - Consult the user stocks button clicked
#----------------------------------------------------------------------------------------------------------------------
    def on_consult_stocks_button_clicked(self):
        self.__stock_list_screen.show()
        self.close()

# SLOT - Fires when user click in back button on consult stocks screen
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot()
    def exit_consult_stocks(self):
        self.show()
        self.__stock_list_screen.close()

# Runs when the screen in closing
#----------------------------------------------------------------------------------------------------------------------
    def closeEvent(self, event):
        logging.debug("Fechando...")

# Executable lines
#----------------------------------------------------------------------------------------------------------------------
app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')
application = Gui()
application.show()
app.exec_()
#----------------------------------------------------------------------------------------------------------------------
