# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'transaction_add.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TransactionAdd(object):
    def setupUi(self, TransactionAdd):
        if not TransactionAdd.objectName():
            TransactionAdd.setObjectName(u"TransactionAdd")
        TransactionAdd.resize(500, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TransactionAdd.sizePolicy().hasHeightForWidth())
        TransactionAdd.setSizePolicy(sizePolicy)
        TransactionAdd.setMinimumSize(QSize(500, 600))
        TransactionAdd.setMaximumSize(QSize(500, 600))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(216, 216, 216, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(235, 235, 235, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(108, 108, 108, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(144, 144, 144, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush6 = QBrush(QColor(255, 255, 220, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 128))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        TransactionAdd.setPalette(palette)
        TransactionAdd.setFocusPolicy(Qt.NoFocus)
        self.TransactionAddLayout = QVBoxLayout(TransactionAdd)
        self.TransactionAddLayout.setObjectName(u"TransactionAddLayout")
        self.backButtonLayout = QHBoxLayout()
        self.backButtonLayout.setObjectName(u"backButtonLayout")
        self.backButton = QPushButton(TransactionAdd)
        self.backButton.setObjectName(u"backButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.backButton.setFont(font)

        self.backButtonLayout.addWidget(self.backButton)

        self.errorLabel = QLabel(TransactionAdd)
        self.errorLabel.setObjectName(u"errorLabel")
        font1 = QFont()
        font1.setPointSize(15)
        self.errorLabel.setFont(font1)
        self.errorLabel.setStyleSheet(u"color: red")
        self.errorLabel.setAlignment(Qt.AlignCenter)

        self.backButtonLayout.addWidget(self.errorLabel)

        self.backButtonLayout.setStretch(0, 2)
        self.backButtonLayout.setStretch(1, 7)

        self.TransactionAddLayout.addLayout(self.backButtonLayout)

        self.transactionAddFrame = QFrame(TransactionAdd)
        self.transactionAddFrame.setObjectName(u"transactionAddFrame")
        self.transactionAddFrame.setFrameShape(QFrame.StyledPanel)
        self.transactionAddFrame.setFrameShadow(QFrame.Raised)
        self.transactionAddFrameLayout = QVBoxLayout(self.transactionAddFrame)
        self.transactionAddFrameLayout.setObjectName(u"transactionAddFrameLayout")
        self.titleLayout = QHBoxLayout()
        self.titleLayout.setObjectName(u"titleLayout")
        self.titleLayout.setContentsMargins(-1, -1, -1, 0)
        self.transactionNameLabel = QLabel(self.transactionAddFrame)
        self.transactionNameLabel.setObjectName(u"transactionNameLabel")
        font2 = QFont()
        font2.setPointSize(25)
        font2.setBold(True)
        font2.setUnderline(True)
        font2.setWeight(75)
        self.transactionNameLabel.setFont(font2)

        self.titleLayout.addWidget(self.transactionNameLabel)

        self.titleSaveSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.titleLayout.addItem(self.titleSaveSpacer)

        self.saveButton = QPushButton(self.transactionAddFrame)
        self.saveButton.setObjectName(u"saveButton")
        sizePolicy1.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setWeight(75)
        self.saveButton.setFont(font3)

        self.titleLayout.addWidget(self.saveButton)

        self.titleLayout.setStretch(0, 3)
        self.titleLayout.setStretch(1, 2)
        self.titleLayout.setStretch(2, 3)

        self.transactionAddFrameLayout.addLayout(self.titleLayout)

        self.titleHorizontalLine = QFrame(self.transactionAddFrame)
        self.titleHorizontalLine.setObjectName(u"titleHorizontalLine")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleHorizontalLine.sizePolicy().hasHeightForWidth())
        self.titleHorizontalLine.setSizePolicy(sizePolicy2)
        self.titleHorizontalLine.setFrameShape(QFrame.HLine)
        self.titleHorizontalLine.setFrameShadow(QFrame.Sunken)

        self.transactionAddFrameLayout.addWidget(self.titleHorizontalLine)

        self.nameInputLayout = QHBoxLayout()
        self.nameInputLayout.setObjectName(u"nameInputLayout")
        self.nameInputLayout.setContentsMargins(-1, 3, -1, 3)
        self.nameLabel = QLabel(self.transactionAddFrame)
        self.nameLabel.setObjectName(u"nameLabel")
        font4 = QFont()
        font4.setPointSize(15)
        font4.setUnderline(True)
        self.nameLabel.setFont(font4)
        self.nameLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.nameInputLayout.addWidget(self.nameLabel)

        self.nameInput = QLineEdit(self.transactionAddFrame)
        self.nameInput.setObjectName(u"nameInput")
        sizePolicy1.setHeightForWidth(self.nameInput.sizePolicy().hasHeightForWidth())
        self.nameInput.setSizePolicy(sizePolicy1)
        self.nameInput.setFont(font1)

        self.nameInputLayout.addWidget(self.nameInput)

        self.nameInputLayout.setStretch(0, 1)
        self.nameInputLayout.setStretch(1, 2)

        self.transactionAddFrameLayout.addLayout(self.nameInputLayout)

        self.idInputLayout = QHBoxLayout()
        self.idInputLayout.setObjectName(u"idInputLayout")
        self.idInputLayout.setContentsMargins(-1, 3, -1, 3)
        self.idLabel = QLabel(self.transactionAddFrame)
        self.idLabel.setObjectName(u"idLabel")
        self.idLabel.setFont(font4)
        self.idLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.idInputLayout.addWidget(self.idLabel)

        self.idInput = QSpinBox(self.transactionAddFrame)
        self.idInput.setObjectName(u"idInput")
        self.idInput.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.idInput.sizePolicy().hasHeightForWidth())
        self.idInput.setSizePolicy(sizePolicy1)
        self.idInput.setFont(font1)
        self.idInput.setMaximum(999999999)

        self.idInputLayout.addWidget(self.idInput)

        self.idInputLayout.setStretch(0, 1)
        self.idInputLayout.setStretch(1, 2)

        self.transactionAddFrameLayout.addLayout(self.idInputLayout)

        self.operationDateLayout = QHBoxLayout()
        self.operationDateLayout.setObjectName(u"operationDateLayout")
        self.operationDateLayout.setContentsMargins(-1, 3, -1, 3)
        self.operationDateLabel = QLabel(self.transactionAddFrame)
        self.operationDateLabel.setObjectName(u"operationDateLabel")
        self.operationDateLabel.setFont(font1)
        self.operationDateLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.operationDateLayout.addWidget(self.operationDateLabel)

        self.operationDateInput = QDateEdit(self.transactionAddFrame)
        self.operationDateInput.setObjectName(u"operationDateInput")
        self.operationDateInput.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.operationDateInput.sizePolicy().hasHeightForWidth())
        self.operationDateInput.setSizePolicy(sizePolicy1)
        self.operationDateInput.setFont(font1)
        self.operationDateInput.setCalendarPopup(True)
        self.operationDateInput.setDate(QDate(2020, 1, 1))

        self.operationDateLayout.addWidget(self.operationDateInput)

        self.operationDateLayout.setStretch(0, 1)
        self.operationDateLayout.setStretch(1, 2)

        self.transactionAddFrameLayout.addLayout(self.operationDateLayout)

        self.categoryInputLayout = QHBoxLayout()
        self.categoryInputLayout.setObjectName(u"categoryInputLayout")
        self.categoryInputLayout.setContentsMargins(-1, 3, -1, 3)
        self.categoryLabel = QLabel(self.transactionAddFrame)
        self.categoryLabel.setObjectName(u"categoryLabel")
        self.categoryLabel.setFont(font4)
        self.categoryLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.categoryInputLayout.addWidget(self.categoryLabel)

        self.categoryInput = QComboBox(self.transactionAddFrame)
        self.categoryInput.addItem("")
        self.categoryInput.addItem("")
        self.categoryInput.setObjectName(u"categoryInput")
        self.categoryInput.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.categoryInput.sizePolicy().hasHeightForWidth())
        self.categoryInput.setSizePolicy(sizePolicy1)
        self.categoryInput.setFont(font1)
        self.categoryInput.setMaxVisibleItems(2)
        self.categoryInput.setMaxCount(2)

        self.categoryInputLayout.addWidget(self.categoryInput)

        self.categoryInputLayout.setStretch(0, 1)
        self.categoryInputLayout.setStretch(1, 2)

        self.transactionAddFrameLayout.addLayout(self.categoryInputLayout)

        self.operationTypeInputLayout = QHBoxLayout()
        self.operationTypeInputLayout.setObjectName(u"operationTypeInputLayout")
        self.operationTypeInputLayout.setContentsMargins(-1, 3, -1, 3)
        self.operationTypeLabel = QLabel(self.transactionAddFrame)
        self.operationTypeLabel.setObjectName(u"operationTypeLabel")
        self.operationTypeLabel.setFont(font4)
        self.operationTypeLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.operationTypeInputLayout.addWidget(self.operationTypeLabel)

        self.operationTypeInput = QComboBox(self.transactionAddFrame)
        self.operationTypeInput.addItem("")
        self.operationTypeInput.addItem("")
        self.operationTypeInput.setObjectName(u"operationTypeInput")
        self.operationTypeInput.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.operationTypeInput.sizePolicy().hasHeightForWidth())
        self.operationTypeInput.setSizePolicy(sizePolicy1)
        self.operationTypeInput.setFont(font1)
        self.operationTypeInput.setMaxVisibleItems(2)
        self.operationTypeInput.setMaxCount(2)

        self.operationTypeInputLayout.addWidget(self.operationTypeInput)

        self.operationTypeInputLayout.setStretch(0, 1)
        self.operationTypeInputLayout.setStretch(1, 2)

        self.transactionAddFrameLayout.addLayout(self.operationTypeInputLayout)

        self.priceInputLayout = QHBoxLayout()
        self.priceInputLayout.setObjectName(u"priceInputLayout")
        self.priceInputLayout.setContentsMargins(-1, 3, -1, 3)
        self.priceLabel = QLabel(self.transactionAddFrame)
        self.priceLabel.setObjectName(u"priceLabel")
        self.priceLabel.setFont(font4)
        self.priceLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.priceInputLayout.addWidget(self.priceLabel)

        self.priceInput = QDoubleSpinBox(self.transactionAddFrame)
        self.priceInput.setObjectName(u"priceInput")
        self.priceInput.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.priceInput.sizePolicy().hasHeightForWidth())
        self.priceInput.setSizePolicy(sizePolicy1)
        self.priceInput.setFont(font1)
        self.priceInput.setMaximum(99999999999999.000000000000000)

        self.priceInputLayout.addWidget(self.priceInput)

        self.priceInputLayout.setStretch(0, 1)
        self.priceInputLayout.setStretch(1, 2)

        self.transactionAddFrameLayout.addLayout(self.priceInputLayout)

        self.ammountInputLayout = QHBoxLayout()
        self.ammountInputLayout.setObjectName(u"ammountInputLayout")
        self.ammountInputLayout.setContentsMargins(-1, 3, -1, 3)
        self.ammountLabel = QLabel(self.transactionAddFrame)
        self.ammountLabel.setObjectName(u"ammountLabel")
        self.ammountLabel.setFont(font4)
        self.ammountLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.ammountInputLayout.addWidget(self.ammountLabel)

        self.ammountInput = QSpinBox(self.transactionAddFrame)
        self.ammountInput.setObjectName(u"ammountInput")
        self.ammountInput.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.ammountInput.sizePolicy().hasHeightForWidth())
        self.ammountInput.setSizePolicy(sizePolicy1)
        self.ammountInput.setFont(font1)
        self.ammountInput.setMaximum(999999999)

        self.ammountInputLayout.addWidget(self.ammountInput)

        self.ammountInputLayout.setStretch(0, 1)
        self.ammountInputLayout.setStretch(1, 2)

        self.transactionAddFrameLayout.addLayout(self.ammountInputLayout)

        self.faresInputLayout = QHBoxLayout()
        self.faresInputLayout.setObjectName(u"faresInputLayout")
        self.faresInputLayout.setContentsMargins(-1, 3, -1, 3)
        self.faresLabel = QLabel(self.transactionAddFrame)
        self.faresLabel.setObjectName(u"faresLabel")
        self.faresLabel.setFont(font4)
        self.faresLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.faresInputLayout.addWidget(self.faresLabel)

        self.faresInput = QDoubleSpinBox(self.transactionAddFrame)
        self.faresInput.setObjectName(u"faresInput")
        self.faresInput.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.faresInput.sizePolicy().hasHeightForWidth())
        self.faresInput.setSizePolicy(sizePolicy1)
        self.faresInput.setFont(font1)
        self.faresInput.setMaximum(9999999999.000000000000000)

        self.faresInputLayout.addWidget(self.faresInput)

        self.faresInputLayout.setStretch(0, 1)
        self.faresInputLayout.setStretch(1, 2)

        self.transactionAddFrameLayout.addLayout(self.faresInputLayout)

        self.totalHorizontalLine = QFrame(self.transactionAddFrame)
        self.totalHorizontalLine.setObjectName(u"totalHorizontalLine")
        sizePolicy2.setHeightForWidth(self.totalHorizontalLine.sizePolicy().hasHeightForWidth())
        self.totalHorizontalLine.setSizePolicy(sizePolicy2)
        self.totalHorizontalLine.setFrameShape(QFrame.HLine)
        self.totalHorizontalLine.setFrameShadow(QFrame.Sunken)

        self.transactionAddFrameLayout.addWidget(self.totalHorizontalLine)

        self.totalLayout = QHBoxLayout()
        self.totalLayout.setObjectName(u"totalLayout")
        self.totalTitleLabel = QLabel(self.transactionAddFrame)
        self.totalTitleLabel.setObjectName(u"totalTitleLabel")
        font5 = QFont()
        font5.setPointSize(25)
        font5.setBold(False)
        font5.setUnderline(True)
        font5.setWeight(50)
        self.totalTitleLabel.setFont(font5)
        self.totalTitleLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.totalLayout.addWidget(self.totalTitleLabel)

        self.realSymbolLabel = QLabel(self.transactionAddFrame)
        self.realSymbolLabel.setObjectName(u"realSymbolLabel")
        self.realSymbolLabel.setFont(font2)

        self.totalLayout.addWidget(self.realSymbolLabel)

        self.totalValueLabel = QLabel(self.transactionAddFrame)
        self.totalValueLabel.setObjectName(u"totalValueLabel")
        self.totalValueLabel.setFont(font2)

        self.totalLayout.addWidget(self.totalValueLabel)

        self.totalLayout.setStretch(0, 10)
        self.totalLayout.setStretch(1, 1)
        self.totalLayout.setStretch(2, 6)

        self.transactionAddFrameLayout.addLayout(self.totalLayout)

        self.transactionAddFrameLayout.setStretch(0, 3)
        self.transactionAddFrameLayout.setStretch(1, 2)
        self.transactionAddFrameLayout.setStretch(2, 2)
        self.transactionAddFrameLayout.setStretch(3, 2)
        self.transactionAddFrameLayout.setStretch(4, 2)
        self.transactionAddFrameLayout.setStretch(5, 2)
        self.transactionAddFrameLayout.setStretch(6, 2)
        self.transactionAddFrameLayout.setStretch(7, 2)
        self.transactionAddFrameLayout.setStretch(8, 2)
        self.transactionAddFrameLayout.setStretch(9, 2)
        self.transactionAddFrameLayout.setStretch(10, 2)
        self.transactionAddFrameLayout.setStretch(11, 2)

        self.TransactionAddLayout.addWidget(self.transactionAddFrame)

        self.TransactionAddLayout.setStretch(0, 1)
        self.TransactionAddLayout.setStretch(1, 20)

        self.retranslateUi(TransactionAdd)

        self.categoryInput.setCurrentIndex(1)
        self.operationTypeInput.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TransactionAdd)
    # setupUi

    def retranslateUi(self, TransactionAdd):
        TransactionAdd.setWindowTitle(QCoreApplication.translate("TransactionAdd", u"Adicionar A\u00e7oes", None))
        self.backButton.setText(QCoreApplication.translate("TransactionAdd", u"<<", None))
        self.errorLabel.setText("")
        self.transactionNameLabel.setText(QCoreApplication.translate("TransactionAdd", u"Transa\u00e7\u00e3o", None))
        self.saveButton.setText(QCoreApplication.translate("TransactionAdd", u"Salvar", None))
        self.nameLabel.setText(QCoreApplication.translate("TransactionAdd", u"Nome:", None))
        self.nameInput.setPlaceholderText(QCoreApplication.translate("TransactionAdd", u"Nome", None))
        self.idLabel.setText(QCoreApplication.translate("TransactionAdd", u"Id:", None))
        self.operationDateLabel.setText(QCoreApplication.translate("TransactionAdd", u"Data:", None))
        self.operationDateInput.setDisplayFormat(QCoreApplication.translate("TransactionAdd", u"dd/MM/yyyy", None))
        self.categoryLabel.setText(QCoreApplication.translate("TransactionAdd", u"Tipo:", None))
        self.categoryInput.setItemText(0, QCoreApplication.translate("TransactionAdd", u"Fundo Imobili\u00e1rio", None))
        self.categoryInput.setItemText(1, QCoreApplication.translate("TransactionAdd", u"Normal", None))

        self.operationTypeLabel.setText(QCoreApplication.translate("TransactionAdd", u"Opera\u00e7\u00e3o:", None))
        self.operationTypeInput.setItemText(0, QCoreApplication.translate("TransactionAdd", u"Compra", None))
        self.operationTypeInput.setItemText(1, QCoreApplication.translate("TransactionAdd", u"Venda", None))

        self.priceLabel.setText(QCoreApplication.translate("TransactionAdd", u"Valor:", None))
        self.ammountLabel.setText(QCoreApplication.translate("TransactionAdd", u"Quantidade:", None))
        self.faresLabel.setText(QCoreApplication.translate("TransactionAdd", u"Taxas:", None))
        self.totalTitleLabel.setText(QCoreApplication.translate("TransactionAdd", u"Total:", None))
        self.realSymbolLabel.setText(QCoreApplication.translate("TransactionAdd", u"R$", None))
        self.totalValueLabel.setText(QCoreApplication.translate("TransactionAdd", u"0.00", None))
    # retranslateUi

