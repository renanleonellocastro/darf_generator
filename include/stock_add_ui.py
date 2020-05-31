# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stock_add.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_StockAdd(object):
    def setupUi(self, StockAdd):
        if not StockAdd.objectName():
            StockAdd.setObjectName(u"StockAdd")
        StockAdd.resize(500, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StockAdd.sizePolicy().hasHeightForWidth())
        StockAdd.setSizePolicy(sizePolicy)
        StockAdd.setMinimumSize(QSize(500, 600))
        StockAdd.setMaximumSize(QSize(500, 600))
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
        StockAdd.setPalette(palette)
        StockAdd.setFocusPolicy(Qt.NoFocus)
        self.StockAddLayout = QVBoxLayout(StockAdd)
        self.StockAddLayout.setObjectName(u"StockAddLayout")
        self.backButtonLayout = QHBoxLayout()
        self.backButtonLayout.setObjectName(u"backButtonLayout")
        self.backButton = QPushButton(StockAdd)
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

        self.errorLabel = QLabel(StockAdd)
        self.errorLabel.setObjectName(u"errorLabel")
        font1 = QFont()
        font1.setPointSize(15)
        self.errorLabel.setFont(font1)
        self.errorLabel.setStyleSheet(u"color: red")
        self.errorLabel.setAlignment(Qt.AlignCenter)

        self.backButtonLayout.addWidget(self.errorLabel)

        self.backButtonLayout.setStretch(0, 2)
        self.backButtonLayout.setStretch(1, 7)

        self.StockAddLayout.addLayout(self.backButtonLayout)

        self.stockAddFrame = QFrame(StockAdd)
        self.stockAddFrame.setObjectName(u"stockAddFrame")
        self.stockAddFrame.setFrameShape(QFrame.StyledPanel)
        self.stockAddFrame.setFrameShadow(QFrame.Raised)
        self.stockAddFrameLayout = QVBoxLayout(self.stockAddFrame)
        self.stockAddFrameLayout.setObjectName(u"stockAddFrameLayout")
        self.titleLayout = QHBoxLayout()
        self.titleLayout.setObjectName(u"titleLayout")
        self.titleLayout.setContentsMargins(-1, -1, -1, 5)
        self.stockNameLabel = QLabel(self.stockAddFrame)
        self.stockNameLabel.setObjectName(u"stockNameLabel")
        font2 = QFont()
        font2.setPointSize(25)
        font2.setBold(True)
        font2.setUnderline(True)
        font2.setWeight(75)
        self.stockNameLabel.setFont(font2)

        self.titleLayout.addWidget(self.stockNameLabel)

        self.titleSaveSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.titleLayout.addItem(self.titleSaveSpacer)

        self.saveButton = QPushButton(self.stockAddFrame)
        self.saveButton.setObjectName(u"saveButton")
        sizePolicy1.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setWeight(75)
        self.saveButton.setFont(font3)

        self.titleLayout.addWidget(self.saveButton)

        self.titleLayout.setStretch(0, 1)
        self.titleLayout.setStretch(1, 1)
        self.titleLayout.setStretch(2, 1)

        self.stockAddFrameLayout.addLayout(self.titleLayout)

        self.titleHorizontalLine = QFrame(self.stockAddFrame)
        self.titleHorizontalLine.setObjectName(u"titleHorizontalLine")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleHorizontalLine.sizePolicy().hasHeightForWidth())
        self.titleHorizontalLine.setSizePolicy(sizePolicy2)
        self.titleHorizontalLine.setFrameShape(QFrame.HLine)
        self.titleHorizontalLine.setFrameShadow(QFrame.Sunken)

        self.stockAddFrameLayout.addWidget(self.titleHorizontalLine)

        self.nameInputLayout = QHBoxLayout()
        self.nameInputLayout.setObjectName(u"nameInputLayout")
        self.nameInputLayout.setContentsMargins(-1, 5, -1, 5)
        self.nameLabel = QLabel(self.stockAddFrame)
        self.nameLabel.setObjectName(u"nameLabel")
        font4 = QFont()
        font4.setPointSize(15)
        font4.setUnderline(True)
        self.nameLabel.setFont(font4)
        self.nameLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.nameInputLayout.addWidget(self.nameLabel)

        self.nameInput = QLineEdit(self.stockAddFrame)
        self.nameInput.setObjectName(u"nameInput")
        sizePolicy1.setHeightForWidth(self.nameInput.sizePolicy().hasHeightForWidth())
        self.nameInput.setSizePolicy(sizePolicy1)
        self.nameInput.setFont(font1)

        self.nameInputLayout.addWidget(self.nameInput)

        self.nameInputLayout.setStretch(0, 1)
        self.nameInputLayout.setStretch(1, 2)

        self.stockAddFrameLayout.addLayout(self.nameInputLayout)

        self.categoryInputLayout = QHBoxLayout()
        self.categoryInputLayout.setObjectName(u"categoryInputLayout")
        self.categoryInputLayout.setContentsMargins(-1, 5, -1, 5)
        self.categoryLabel = QLabel(self.stockAddFrame)
        self.categoryLabel.setObjectName(u"categoryLabel")
        self.categoryLabel.setFont(font4)
        self.categoryLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.categoryInputLayout.addWidget(self.categoryLabel)

        self.categoryInput = QComboBox(self.stockAddFrame)
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

        self.stockAddFrameLayout.addLayout(self.categoryInputLayout)

        self.priceInputLayout = QHBoxLayout()
        self.priceInputLayout.setObjectName(u"priceInputLayout")
        self.priceInputLayout.setContentsMargins(-1, 5, -1, 5)
        self.priceLabel = QLabel(self.stockAddFrame)
        self.priceLabel.setObjectName(u"priceLabel")
        self.priceLabel.setFont(font4)
        self.priceLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.priceInputLayout.addWidget(self.priceLabel)

        self.priceInput = QDoubleSpinBox(self.stockAddFrame)
        self.priceInput.setObjectName(u"priceInput")
        self.priceInput.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.priceInput.sizePolicy().hasHeightForWidth())
        self.priceInput.setSizePolicy(sizePolicy1)
        self.priceInput.setFont(font1)
        self.priceInput.setMaximum(99999999999999.000000000000000)

        self.priceInputLayout.addWidget(self.priceInput)

        self.priceInputLayout.setStretch(0, 1)
        self.priceInputLayout.setStretch(1, 2)

        self.stockAddFrameLayout.addLayout(self.priceInputLayout)

        self.ammountInputLayout = QHBoxLayout()
        self.ammountInputLayout.setObjectName(u"ammountInputLayout")
        self.ammountInputLayout.setContentsMargins(-1, 5, -1, 5)
        self.ammountLabel = QLabel(self.stockAddFrame)
        self.ammountLabel.setObjectName(u"ammountLabel")
        self.ammountLabel.setFont(font4)
        self.ammountLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.ammountInputLayout.addWidget(self.ammountLabel)

        self.ammountInput = QSpinBox(self.stockAddFrame)
        self.ammountInput.setObjectName(u"ammountInput")
        self.ammountInput.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.ammountInput.sizePolicy().hasHeightForWidth())
        self.ammountInput.setSizePolicy(sizePolicy1)
        self.ammountInput.setFont(font1)
        self.ammountInput.setMaximum(999999999)

        self.ammountInputLayout.addWidget(self.ammountInput)

        self.ammountInputLayout.setStretch(0, 1)
        self.ammountInputLayout.setStretch(1, 2)

        self.stockAddFrameLayout.addLayout(self.ammountInputLayout)

        self.faresInputLayout = QHBoxLayout()
        self.faresInputLayout.setObjectName(u"faresInputLayout")
        self.faresInputLayout.setContentsMargins(-1, 5, -1, 5)
        self.faresLabel = QLabel(self.stockAddFrame)
        self.faresLabel.setObjectName(u"faresLabel")
        self.faresLabel.setFont(font4)
        self.faresLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.faresInputLayout.addWidget(self.faresLabel)

        self.faresInput = QDoubleSpinBox(self.stockAddFrame)
        self.faresInput.setObjectName(u"faresInput")
        self.faresInput.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.faresInput.sizePolicy().hasHeightForWidth())
        self.faresInput.setSizePolicy(sizePolicy1)
        self.faresInput.setFont(font1)
        self.faresInput.setMaximum(9999999999.000000000000000)

        self.faresInputLayout.addWidget(self.faresInput)

        self.faresInputLayout.setStretch(0, 1)
        self.faresInputLayout.setStretch(1, 2)

        self.stockAddFrameLayout.addLayout(self.faresInputLayout)

        self.totalHorizontalLine = QFrame(self.stockAddFrame)
        self.totalHorizontalLine.setObjectName(u"totalHorizontalLine")
        sizePolicy2.setHeightForWidth(self.totalHorizontalLine.sizePolicy().hasHeightForWidth())
        self.totalHorizontalLine.setSizePolicy(sizePolicy2)
        self.totalHorizontalLine.setFrameShape(QFrame.HLine)
        self.totalHorizontalLine.setFrameShadow(QFrame.Sunken)

        self.stockAddFrameLayout.addWidget(self.totalHorizontalLine)

        self.totalLayout = QHBoxLayout()
        self.totalLayout.setObjectName(u"totalLayout")
        self.totalTitleLabel = QLabel(self.stockAddFrame)
        self.totalTitleLabel.setObjectName(u"totalTitleLabel")
        font5 = QFont()
        font5.setPointSize(25)
        font5.setBold(False)
        font5.setUnderline(True)
        font5.setWeight(50)
        self.totalTitleLabel.setFont(font5)
        self.totalTitleLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.totalLayout.addWidget(self.totalTitleLabel)

        self.realSymbolLabel = QLabel(self.stockAddFrame)
        self.realSymbolLabel.setObjectName(u"realSymbolLabel")
        self.realSymbolLabel.setFont(font2)

        self.totalLayout.addWidget(self.realSymbolLabel)

        self.totalValueLabel = QLabel(self.stockAddFrame)
        self.totalValueLabel.setObjectName(u"totalValueLabel")
        self.totalValueLabel.setFont(font2)

        self.totalLayout.addWidget(self.totalValueLabel)

        self.totalLayout.setStretch(0, 10)
        self.totalLayout.setStretch(1, 1)
        self.totalLayout.setStretch(2, 6)

        self.stockAddFrameLayout.addLayout(self.totalLayout)


        self.StockAddLayout.addWidget(self.stockAddFrame)

        self.StockAddLayout.setStretch(0, 1)
        self.StockAddLayout.setStretch(1, 20)

        self.retranslateUi(StockAdd)

        self.categoryInput.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(StockAdd)
    # setupUi

    def retranslateUi(self, StockAdd):
        StockAdd.setWindowTitle(QCoreApplication.translate("StockAdd", u"Adicionar A\u00e7oes", None))
        self.backButton.setText(QCoreApplication.translate("StockAdd", u"<<", None))
        self.errorLabel.setText("")
        self.stockNameLabel.setText(QCoreApplication.translate("StockAdd", u"A\u00e7\u00e3o", None))
        self.saveButton.setText(QCoreApplication.translate("StockAdd", u"Salvar", None))
        self.nameLabel.setText(QCoreApplication.translate("StockAdd", u"Nome:", None))
        self.nameInput.setPlaceholderText(QCoreApplication.translate("StockAdd", u"Nome", None))
        self.categoryLabel.setText(QCoreApplication.translate("StockAdd", u"Tipo:", None))
        self.categoryInput.setItemText(0, QCoreApplication.translate("StockAdd", u"Fundo Imobili\u00e1rio", None))
        self.categoryInput.setItemText(1, QCoreApplication.translate("StockAdd", u"Normal", None))

        self.priceLabel.setText(QCoreApplication.translate("StockAdd", u"Valor:", None))
        self.ammountLabel.setText(QCoreApplication.translate("StockAdd", u"Quantidade:", None))
        self.faresLabel.setText(QCoreApplication.translate("StockAdd", u"Taxas:", None))
        self.totalTitleLabel.setText(QCoreApplication.translate("StockAdd", u"Total:", None))
        self.realSymbolLabel.setText(QCoreApplication.translate("StockAdd", u"R$", None))
        self.totalValueLabel.setText(QCoreApplication.translate("StockAdd", u"0.00", None))
    # retranslateUi

