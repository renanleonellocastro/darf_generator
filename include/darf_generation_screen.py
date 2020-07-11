#!/usr/bin/python3

import os
import platform
import subprocess
from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets
from include.darf_generation_ui import Ui_DarfGeneration

class DarfGenerationScreen(QtWidgets.QWidget, Ui_DarfGeneration):

# Definition of Qt Signals
#----------------------------------------------------------------------------------------------------------------------
    exit_darf_generation_signal = QtCore.Signal()
    start_darf_generation_signal = QtCore.Signal(str,str,str,float)
    captcha_solution_signal = QtCore.Signal(str)

# Constructor
#----------------------------------------------------------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        super(DarfGenerationScreen, self).__init__()
        self.setupUi(self)
        self.stateList.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        self.stateList.lineEdit().setReadOnly(True)
        self.progressBar.setValue(0)
        self.captchaFrame.hide()
        self.progressBar.hide()
        self.__value = 0.0
        self.__cpf = ''
        self.__state = ''
        self.__city = ''
        self.__captch_image_path = os.path.dirname(os.path.abspath(__file__)) + '/../downloads/captcha.jpg'
        self.backButton.clicked.connect(self.on_back_button_clicked)
        self.cpfButton.clicked.connect(self.on_cpf_button_clicked)
        self.captchaButton.clicked.connect(self.on_captcha_button_clicked)

# Get class member "value"
#----------------------------------------------------------------------------------------------------------------------
    @property
    def value(self):
        return self.__value

# Set class member "value"
#----------------------------------------------------------------------------------------------------------------------
    @value.setter
    def value(self, new_value):
        self.__value = new_value

# Load a captcha image to screen
#----------------------------------------------------------------------------------------------------------------------
    def load_captcha_image(self):
        image = QtGui.QImage(self.__captch_image_path)
        pixmap = QtGui.QPixmap(image)
        self.captchaImage.setPixmap(pixmap)
        self.progressBar.hide()
        self.captchaFrame.show()

# SLOT - Process the back button clicked
#----------------------------------------------------------------------------------------------------------------------  
    def on_back_button_clicked(self):
        self.progressBar.setValue(0)
        self.cpfFrame.show()
        self.progressBar.hide()
        self.exit_darf_generation_signal.emit()

# SLOT - Process the cpf button clicked
#----------------------------------------------------------------------------------------------------------------------  
    def on_cpf_button_clicked(self):
        self.__cpf = self.cpfInput.text()
        self.__state = self.stateList.currentText()
        self.__city = self.cityInput.text()
        self.backButton.setEnabled(False)
        self.cpfFrame.hide()
        self.progressBar.show()
        self.titleLabel.setText("Gerando a DARF...")
        self.start_darf_generation_signal.emit(self.__cpf, self.__state, self.__city, self.__value)

# SLOT - Process the captcha button clicked
#----------------------------------------------------------------------------------------------------------------------  
    def on_captcha_button_clicked(self):
        solution = self.captchaInput.text()
        self.captchaInput.setText('')
        self.captchaFrame.hide()
        self.progressBar.show()
        self.titleLabel.setText("Gerando boleto...")
        self.errorLabel.setText("")
        self.captcha_solution_signal.emit(solution)

# SLOT - Process the request of the control when it wants the captcha to be solved
#----------------------------------------------------------------------------------------------------------------------  
    @QtCore.Slot(bool)
    def request_captcha_solution_slot(self, error):
        self.load_captcha_image()
        self.titleLabel.setText("Verificação de segurança...")
        if not error:
            self.errorLabel.setText("")
        else:
            self.errorLabel.setStyleSheet("color: red")
            self.errorLabel.setText("Erro: Solução errada. Preencher novamente...")

# SLOT - Process the request of the control when it wants to update the darf generation progress
#---------------------------------------------------------------------------------------------------------------------- 
    @QtCore.Slot(int)
    def update_generation_progress_slot(self, progress):
        self.progressBar.setValue(progress)

# SLOT - Process the request of the control to open the darf file
#----------------------------------------------------------------------------------------------------------------------  
    @QtCore.Slot()
    def open_darf_file_slot(self):
        darf_file = os.path.dirname(os.path.abspath(__file__)) + '/../downloads/darf.png'
        self.backButton.setEnabled(True)
        self.errorLabel.setStyleSheet("color: green")
        self.errorLabel.setText("DARF gerada com sucesso!")
        if platform.system() == 'Darwin':       # macOS
            subprocess.call(('open', darf_file))
        elif platform.system() == 'Windows':    # Windows
            os.startfile(darf_file)
        else:                                   # linux variants
            subprocess.call(('xdg-open', darf_file))
#----------------------------------------------------------------------------------------------------------------------
