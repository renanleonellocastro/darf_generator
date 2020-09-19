# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stock.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Stock(object):
    def setupUi(self, Stock):
        if not Stock.objectName():
            Stock.setObjectName(u"Stock")
        Stock.resize(450, 165)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Stock.sizePolicy().hasHeightForWidth())
        Stock.setSizePolicy(sizePolicy)
        Stock.setMinimumSize(QSize(450, 0))
        Stock.setMaximumSize(QSize(16777215, 165))
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
        Stock.setPalette(palette)
        Stock.setFocusPolicy(Qt.NoFocus)
        self.StockLayout = QVBoxLayout(Stock)
        self.StockLayout.setObjectName(u"StockLayout")
        self.StockLayout.setContentsMargins(2, 2, 2, 2)
        self.stockMainFrame = QFrame(Stock)
        self.stockMainFrame.setObjectName(u"stockMainFrame")
        self.stockMainFrame.setFrameShape(QFrame.StyledPanel)
        self.stockMainFrame.setFrameShadow(QFrame.Raised)
        self.stockMainFrameLayout = QVBoxLayout(self.stockMainFrame)
        self.stockMainFrameLayout.setObjectName(u"stockMainFrameLayout")
        self.stockMainFrameLayout.setContentsMargins(7, 7, 7, 7)
        self.stockEditLayout = QHBoxLayout()
        self.stockEditLayout.setSpacing(6)
        self.stockEditLayout.setObjectName(u"stockEditLayout")
        self.stockLabel = QLabel(self.stockMainFrame)
        self.stockLabel.setObjectName(u"stockLabel")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.stockLabel.setFont(font)

        self.stockEditLayout.addWidget(self.stockLabel)

        self.editButton = QPushButton(self.stockMainFrame)
        self.editButton.setObjectName(u"editButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.editButton.sizePolicy().hasHeightForWidth())
        self.editButton.setSizePolicy(sizePolicy1)
        self.editButton.setCheckable(False)
        self.editButton.setFlat(False)

        self.stockEditLayout.addWidget(self.editButton)

        self.stockEditLayout.setStretch(0, 3)
        self.stockEditLayout.setStretch(1, 1)

        self.stockMainFrameLayout.addLayout(self.stockEditLayout)

        self.stockPropertiesLayout = QHBoxLayout()
        self.stockPropertiesLayout.setSpacing(10)
        self.stockPropertiesLayout.setObjectName(u"stockPropertiesLayout")
        self.nameCategoryTotalLayout = QVBoxLayout()
        self.nameCategoryTotalLayout.setObjectName(u"nameCategoryTotalLayout")
        self.nameCategoryTotalPriceSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.nameCategoryTotalLayout.addItem(self.nameCategoryTotalPriceSpacer)

        self.categoryInput = QComboBox(self.stockMainFrame)
        self.categoryInput.addItem("")
        self.categoryInput.addItem("")
        self.categoryInput.setObjectName(u"categoryInput")
        self.categoryInput.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.categoryInput.sizePolicy().hasHeightForWidth())
        self.categoryInput.setSizePolicy(sizePolicy1)
        self.categoryInput.setMaxVisibleItems(2)
        self.categoryInput.setMaxCount(2)

        self.nameCategoryTotalLayout.addWidget(self.categoryInput)

        self.totalValueLayout = QHBoxLayout()
        self.totalValueLayout.setObjectName(u"totalValueLayout")
        self.realSymbolLabel = QLabel(self.stockMainFrame)
        self.realSymbolLabel.setObjectName(u"realSymbolLabel")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setWeight(75)
        self.realSymbolLabel.setFont(font1)

        self.totalValueLayout.addWidget(self.realSymbolLabel)

        self.totalValueLabel = QLabel(self.stockMainFrame)
        self.totalValueLabel.setObjectName(u"totalValueLabel")
        self.totalValueLabel.setFont(font1)

        self.totalValueLayout.addWidget(self.totalValueLabel)

        self.totalValueSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.totalValueLayout.addItem(self.totalValueSpacer)

        self.totalValueLayout.setStretch(0, 1)
        self.totalValueLayout.setStretch(1, 1)
        self.totalValueLayout.setStretch(2, 10)

        self.nameCategoryTotalLayout.addLayout(self.totalValueLayout)

        self.nameCategoryTotalLayout.setStretch(0, 1)
        self.nameCategoryTotalLayout.setStretch(1, 2)
        self.nameCategoryTotalLayout.setStretch(2, 2)

        self.stockPropertiesLayout.addLayout(self.nameCategoryTotalLayout)

        self.valueAmmountFaresLayout = QVBoxLayout()
        self.valueAmmountFaresLayout.setObjectName(u"valueAmmountFaresLayout")
        self.valueAmmountFaresLayout.setContentsMargins(10, -1, -1, -1)
        self.valueLayout = QHBoxLayout()
        self.valueLayout.setObjectName(u"valueLayout")
        self.valueLabel = QLabel(self.stockMainFrame)
        self.valueLabel.setObjectName(u"valueLabel")
        self.valueLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.valueLayout.addWidget(self.valueLabel)

        self.valueInput = QDoubleSpinBox(self.stockMainFrame)
        self.valueInput.setObjectName(u"valueInput")
        self.valueInput.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.valueInput.sizePolicy().hasHeightForWidth())
        self.valueInput.setSizePolicy(sizePolicy1)
        self.valueInput.setMaximum(999999999.000000000000000)

        self.valueLayout.addWidget(self.valueInput)

        self.valueLayout.setStretch(0, 1)
        self.valueLayout.setStretch(1, 2)

        self.valueAmmountFaresLayout.addLayout(self.valueLayout)

        self.ammountLayout = QHBoxLayout()
        self.ammountLayout.setObjectName(u"ammountLayout")
        self.ammountLabel = QLabel(self.stockMainFrame)
        self.ammountLabel.setObjectName(u"ammountLabel")
        self.ammountLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.ammountLayout.addWidget(self.ammountLabel)

        self.ammountInput = QSpinBox(self.stockMainFrame)
        self.ammountInput.setObjectName(u"ammountInput")
        self.ammountInput.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.ammountInput.sizePolicy().hasHeightForWidth())
        self.ammountInput.setSizePolicy(sizePolicy1)
        self.ammountInput.setMaximum(999999)

        self.ammountLayout.addWidget(self.ammountInput)

        self.ammountLayout.setStretch(0, 1)
        self.ammountLayout.setStretch(1, 2)

        self.valueAmmountFaresLayout.addLayout(self.ammountLayout)

        self.faresLayout = QHBoxLayout()
        self.faresLayout.setObjectName(u"faresLayout")
        self.faresLabel = QLabel(self.stockMainFrame)
        self.faresLabel.setObjectName(u"faresLabel")
        self.faresLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.faresLayout.addWidget(self.faresLabel)

        self.faresInput = QDoubleSpinBox(self.stockMainFrame)
        self.faresInput.setObjectName(u"faresInput")
        self.faresInput.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.faresInput.sizePolicy().hasHeightForWidth())
        self.faresInput.setSizePolicy(sizePolicy1)
        self.faresInput.setMaximum(9999999.000000000000000)

        self.faresLayout.addWidget(self.faresInput)

        self.faresLayout.setStretch(0, 1)
        self.faresLayout.setStretch(1, 2)

        self.valueAmmountFaresLayout.addLayout(self.faresLayout)


        self.stockPropertiesLayout.addLayout(self.valueAmmountFaresLayout)

        self.stockPropertiesLayout.setStretch(0, 2)
        self.stockPropertiesLayout.setStretch(1, 3)

        self.stockMainFrameLayout.addLayout(self.stockPropertiesLayout)

        self.stockMainFrameLayout.setStretch(0, 2)
        self.stockMainFrameLayout.setStretch(1, 8)

        self.StockLayout.addWidget(self.stockMainFrame)


        self.retranslateUi(Stock)

        self.categoryInput.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Stock)
    # setupUi

    def retranslateUi(self, Stock):
        Stock.setWindowTitle(QCoreApplication.translate("Stock", u"Gerador de Darf", None))
        self.stockLabel.setText(QCoreApplication.translate("Stock", u"A\u00e7\u00e3o", None))
        self.editButton.setText(QCoreApplication.translate("Stock", u"Editar", None))
        self.categoryInput.setItemText(0, QCoreApplication.translate("Stock", u"Fundo Imobili\u00e1rio", None))
        self.categoryInput.setItemText(1, QCoreApplication.translate("Stock", u"Normal", None))

        self.realSymbolLabel.setText(QCoreApplication.translate("Stock", u"R$", None))
        self.totalValueLabel.setText(QCoreApplication.translate("Stock", u"1000.00", None))
        self.valueLabel.setText(QCoreApplication.translate("Stock", u"Valor:", None))
        self.ammountLabel.setText(QCoreApplication.translate("Stock", u"Quantidade:", None))
        self.faresLabel.setText(QCoreApplication.translate("Stock", u"Taxas:", None))
    # retranslateUi

