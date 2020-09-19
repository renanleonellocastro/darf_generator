# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'transaction.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Transaction(object):
    def setupUi(self, Transaction):
        if not Transaction.objectName():
            Transaction.setObjectName(u"Transaction")
        Transaction.resize(550, 215)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Transaction.sizePolicy().hasHeightForWidth())
        Transaction.setSizePolicy(sizePolicy)
        Transaction.setMinimumSize(QSize(0, 215))
        Transaction.setMaximumSize(QSize(16777215, 215))
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
        Transaction.setPalette(palette)
        Transaction.setFocusPolicy(Qt.NoFocus)
        self.TransactionFormLayout = QVBoxLayout(Transaction)
        self.TransactionFormLayout.setObjectName(u"TransactionFormLayout")
        self.transactionMainFrame = QFrame(Transaction)
        self.transactionMainFrame.setObjectName(u"transactionMainFrame")
        self.transactionMainFrame.setFrameShape(QFrame.StyledPanel)
        self.transactionMainFrame.setFrameShadow(QFrame.Raised)
        self.transactionMainFrameLayout = QVBoxLayout(self.transactionMainFrame)
        self.transactionMainFrameLayout.setObjectName(u"transactionMainFrameLayout")
        self.transactionMainFrameLayout.setContentsMargins(7, 7, 7, 7)
        self.transactionEditLayout = QHBoxLayout()
        self.transactionEditLayout.setSpacing(6)
        self.transactionEditLayout.setObjectName(u"transactionEditLayout")
        self.transactionLabel = QLabel(self.transactionMainFrame)
        self.transactionLabel.setObjectName(u"transactionLabel")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.transactionLabel.setFont(font)

        self.transactionEditLayout.addWidget(self.transactionLabel)

        self.editButton = QPushButton(self.transactionMainFrame)
        self.editButton.setObjectName(u"editButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.editButton.sizePolicy().hasHeightForWidth())
        self.editButton.setSizePolicy(sizePolicy1)
        self.editButton.setCheckable(False)
        self.editButton.setFlat(False)

        self.transactionEditLayout.addWidget(self.editButton)

        self.transactionEditLayout.setStretch(0, 3)
        self.transactionEditLayout.setStretch(1, 1)

        self.transactionMainFrameLayout.addLayout(self.transactionEditLayout)

        self.transactionPropertiesLayout = QHBoxLayout()
        self.transactionPropertiesLayout.setSpacing(6)
        self.transactionPropertiesLayout.setObjectName(u"transactionPropertiesLayout")
        self.idNameCategoryTotalLayout = QVBoxLayout()
        self.idNameCategoryTotalLayout.setObjectName(u"idNameCategoryTotalLayout")
        self.idLayout = QHBoxLayout()
        self.idLayout.setObjectName(u"idLayout")
        self.idLabel = QLabel(self.transactionMainFrame)
        self.idLabel.setObjectName(u"idLabel")
        self.idLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.idLayout.addWidget(self.idLabel)

        self.idInput = QSpinBox(self.transactionMainFrame)
        self.idInput.setObjectName(u"idInput")
        self.idInput.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.idInput.sizePolicy().hasHeightForWidth())
        self.idInput.setSizePolicy(sizePolicy1)
        self.idInput.setMaximum(999999999)

        self.idLayout.addWidget(self.idInput)

        self.idLayout.setStretch(0, 1)
        self.idLayout.setStretch(1, 10)

        self.idNameCategoryTotalLayout.addLayout(self.idLayout)

        self.categoryInput = QComboBox(self.transactionMainFrame)
        self.categoryInput.addItem("")
        self.categoryInput.addItem("")
        self.categoryInput.setObjectName(u"categoryInput")
        self.categoryInput.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.categoryInput.sizePolicy().hasHeightForWidth())
        self.categoryInput.setSizePolicy(sizePolicy1)
        self.categoryInput.setMaxVisibleItems(2)
        self.categoryInput.setMaxCount(2)

        self.idNameCategoryTotalLayout.addWidget(self.categoryInput)

        self.operationTypeInput = QComboBox(self.transactionMainFrame)
        self.operationTypeInput.addItem("")
        self.operationTypeInput.addItem("")
        self.operationTypeInput.setObjectName(u"operationTypeInput")
        self.operationTypeInput.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.operationTypeInput.sizePolicy().hasHeightForWidth())
        self.operationTypeInput.setSizePolicy(sizePolicy1)
        self.operationTypeInput.setMaxVisibleItems(2)
        self.operationTypeInput.setMaxCount(2)

        self.idNameCategoryTotalLayout.addWidget(self.operationTypeInput)

        self.totalValueLayout = QHBoxLayout()
        self.totalValueLayout.setObjectName(u"totalValueLayout")
        self.realSymbolLabel = QLabel(self.transactionMainFrame)
        self.realSymbolLabel.setObjectName(u"realSymbolLabel")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setWeight(75)
        self.realSymbolLabel.setFont(font1)

        self.totalValueLayout.addWidget(self.realSymbolLabel)

        self.totalValueLabel = QLabel(self.transactionMainFrame)
        self.totalValueLabel.setObjectName(u"totalValueLabel")
        self.totalValueLabel.setFont(font1)

        self.totalValueLayout.addWidget(self.totalValueLabel)

        self.totalValueSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.totalValueLayout.addItem(self.totalValueSpacer)

        self.totalValueLayout.setStretch(0, 1)
        self.totalValueLayout.setStretch(1, 1)
        self.totalValueLayout.setStretch(2, 10)

        self.idNameCategoryTotalLayout.addLayout(self.totalValueLayout)


        self.transactionPropertiesLayout.addLayout(self.idNameCategoryTotalLayout)

        self.mainHorizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.transactionPropertiesLayout.addItem(self.mainHorizontalSpacer)

        self.dateValueAmmountFaresLayout = QVBoxLayout()
        self.dateValueAmmountFaresLayout.setObjectName(u"dateValueAmmountFaresLayout")
        self.operationDateLayout = QHBoxLayout()
        self.operationDateLayout.setObjectName(u"operationDateLayout")
        self.operationDateLabel = QLabel(self.transactionMainFrame)
        self.operationDateLabel.setObjectName(u"operationDateLabel")
        self.operationDateLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.operationDateLayout.addWidget(self.operationDateLabel)

        self.operationDateInput = QDateEdit(self.transactionMainFrame)
        self.operationDateInput.setObjectName(u"operationDateInput")
        self.operationDateInput.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.operationDateInput.sizePolicy().hasHeightForWidth())
        self.operationDateInput.setSizePolicy(sizePolicy1)
        self.operationDateInput.setCalendarPopup(True)
        self.operationDateInput.setDate(QDate(2020, 1, 1))

        self.operationDateLayout.addWidget(self.operationDateInput)

        self.operationDateLayout.setStretch(0, 1)
        self.operationDateLayout.setStretch(1, 2)

        self.dateValueAmmountFaresLayout.addLayout(self.operationDateLayout)

        self.priceLayout = QHBoxLayout()
        self.priceLayout.setObjectName(u"priceLayout")
        self.priceLabel = QLabel(self.transactionMainFrame)
        self.priceLabel.setObjectName(u"priceLabel")
        self.priceLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.priceLayout.addWidget(self.priceLabel)

        self.priceInput = QDoubleSpinBox(self.transactionMainFrame)
        self.priceInput.setObjectName(u"priceInput")
        self.priceInput.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.priceInput.sizePolicy().hasHeightForWidth())
        self.priceInput.setSizePolicy(sizePolicy1)
        self.priceInput.setMaximum(9999999.000000000000000)

        self.priceLayout.addWidget(self.priceInput)

        self.priceLayout.setStretch(0, 1)
        self.priceLayout.setStretch(1, 2)

        self.dateValueAmmountFaresLayout.addLayout(self.priceLayout)

        self.ammountLayout = QHBoxLayout()
        self.ammountLayout.setObjectName(u"ammountLayout")
        self.ammountLabel = QLabel(self.transactionMainFrame)
        self.ammountLabel.setObjectName(u"ammountLabel")
        self.ammountLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.ammountLayout.addWidget(self.ammountLabel)

        self.ammountInput = QSpinBox(self.transactionMainFrame)
        self.ammountInput.setObjectName(u"ammountInput")
        self.ammountInput.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.ammountInput.sizePolicy().hasHeightForWidth())
        self.ammountInput.setSizePolicy(sizePolicy1)
        self.ammountInput.setMaximum(999999)

        self.ammountLayout.addWidget(self.ammountInput)

        self.ammountLayout.setStretch(0, 1)
        self.ammountLayout.setStretch(1, 2)

        self.dateValueAmmountFaresLayout.addLayout(self.ammountLayout)

        self.faresLayout = QHBoxLayout()
        self.faresLayout.setObjectName(u"faresLayout")
        self.faresLabel = QLabel(self.transactionMainFrame)
        self.faresLabel.setObjectName(u"faresLabel")
        self.faresLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.faresLayout.addWidget(self.faresLabel)

        self.faresInput = QDoubleSpinBox(self.transactionMainFrame)
        self.faresInput.setObjectName(u"faresInput")
        self.faresInput.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.faresInput.sizePolicy().hasHeightForWidth())
        self.faresInput.setSizePolicy(sizePolicy1)
        self.faresInput.setMaximum(99999999.000000000000000)

        self.faresLayout.addWidget(self.faresInput)

        self.faresLayout.setStretch(0, 1)
        self.faresLayout.setStretch(1, 2)

        self.dateValueAmmountFaresLayout.addLayout(self.faresLayout)


        self.transactionPropertiesLayout.addLayout(self.dateValueAmmountFaresLayout)


        self.transactionMainFrameLayout.addLayout(self.transactionPropertiesLayout)

        self.transactionMainFrameLayout.setStretch(0, 2)
        self.transactionMainFrameLayout.setStretch(1, 8)

        self.TransactionFormLayout.addWidget(self.transactionMainFrame)


        self.retranslateUi(Transaction)

        self.categoryInput.setCurrentIndex(1)
        self.operationTypeInput.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Transaction)
    # setupUi

    def retranslateUi(self, Transaction):
        Transaction.setWindowTitle(QCoreApplication.translate("Transaction", u"Gerador de Darf", None))
        self.transactionLabel.setText(QCoreApplication.translate("Transaction", u"Transa\u00e7\u00e3o", None))
        self.editButton.setText(QCoreApplication.translate("Transaction", u"Editar", None))
        self.idLabel.setText(QCoreApplication.translate("Transaction", u"ID:", None))
        self.categoryInput.setItemText(0, QCoreApplication.translate("Transaction", u"Fundo Imobili\u00e1rio", None))
        self.categoryInput.setItemText(1, QCoreApplication.translate("Transaction", u"Normal", None))

        self.operationTypeInput.setItemText(0, QCoreApplication.translate("Transaction", u"Compra", None))
        self.operationTypeInput.setItemText(1, QCoreApplication.translate("Transaction", u"Venda", None))

        self.realSymbolLabel.setText(QCoreApplication.translate("Transaction", u"R$", None))
        self.totalValueLabel.setText(QCoreApplication.translate("Transaction", u"1000.00", None))
        self.operationDateLabel.setText(QCoreApplication.translate("Transaction", u"Data:", None))
        self.operationDateInput.setDisplayFormat(QCoreApplication.translate("Transaction", u"dd/MM/yyyy", None))
        self.priceLabel.setText(QCoreApplication.translate("Transaction", u"Valor:", None))
        self.ammountLabel.setText(QCoreApplication.translate("Transaction", u"Quantidade:", None))
        self.faresLabel.setText(QCoreApplication.translate("Transaction", u"Taxas:", None))
    # retranslateUi

