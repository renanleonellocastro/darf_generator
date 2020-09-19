# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Gui(object):
    def setupUi(self, Gui):
        if not Gui.objectName():
            Gui.setObjectName(u"Gui")
        Gui.resize(500, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Gui.sizePolicy().hasHeightForWidth())
        Gui.setSizePolicy(sizePolicy)
        Gui.setMinimumSize(QSize(500, 600))
        Gui.setMaximumSize(QSize(500, 600))
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
        Gui.setPalette(palette)
        Gui.setFocusPolicy(Qt.NoFocus)
        self.guiLayout = QVBoxLayout(Gui)
        self.guiLayout.setObjectName(u"guiLayout")
        self.ceiFrame = QFrame(Gui)
        self.ceiFrame.setObjectName(u"ceiFrame")
        self.ceiFrame.setFocusPolicy(Qt.NoFocus)
        self.ceiFrame.setFrameShape(QFrame.StyledPanel)
        self.ceiFrame.setFrameShadow(QFrame.Raised)
        self.ceiFrameLayout = QVBoxLayout(self.ceiFrame)
        self.ceiFrameLayout.setObjectName(u"ceiFrameLayout")
        self.ceiFrameLayout.setContentsMargins(-1, 0, -1, 9)
        self.ceiLabel = QLabel(self.ceiFrame)
        self.ceiLabel.setObjectName(u"ceiLabel")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.ceiLabel.setFont(font)
        self.ceiLabel.setStyleSheet(u"")
        self.ceiLabel.setAlignment(Qt.AlignCenter)

        self.ceiFrameLayout.addWidget(self.ceiLabel)

        self.ceiLoginFrame = QFrame(self.ceiFrame)
        self.ceiLoginFrame.setObjectName(u"ceiLoginFrame")
        self.ceiLoginFrame.setFrameShape(QFrame.NoFrame)
        self.ceiLoginFrame.setFrameShadow(QFrame.Raised)
        self.ceiLoginFrameLayout = QHBoxLayout(self.ceiLoginFrame)
        self.ceiLoginFrameLayout.setObjectName(u"ceiLoginFrameLayout")
        self.ceiLoginFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.ceiCpfInput = QLineEdit(self.ceiLoginFrame)
        self.ceiCpfInput.setObjectName(u"ceiCpfInput")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ceiCpfInput.sizePolicy().hasHeightForWidth())
        self.ceiCpfInput.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(11)
        self.ceiCpfInput.setFont(font1)
        self.ceiCpfInput.setFocusPolicy(Qt.StrongFocus)
        self.ceiCpfInput.setAlignment(Qt.AlignCenter)

        self.ceiLoginFrameLayout.addWidget(self.ceiCpfInput)

        self.ceiPasswordInput = QLineEdit(self.ceiLoginFrame)
        self.ceiPasswordInput.setObjectName(u"ceiPasswordInput")
        sizePolicy1.setHeightForWidth(self.ceiPasswordInput.sizePolicy().hasHeightForWidth())
        self.ceiPasswordInput.setSizePolicy(sizePolicy1)
        self.ceiPasswordInput.setFont(font1)
        self.ceiPasswordInput.setFocusPolicy(Qt.StrongFocus)
        self.ceiPasswordInput.setEchoMode(QLineEdit.Password)
        self.ceiPasswordInput.setAlignment(Qt.AlignCenter)

        self.ceiLoginFrameLayout.addWidget(self.ceiPasswordInput)


        self.ceiFrameLayout.addWidget(self.ceiLoginFrame)

        self.ceiMonthsList = QComboBox(self.ceiFrame)
        self.ceiMonthsList.setObjectName(u"ceiMonthsList")
        self.ceiMonthsList.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.ceiMonthsList.sizePolicy().hasHeightForWidth())
        self.ceiMonthsList.setSizePolicy(sizePolicy1)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush8 = QBrush(QColor(217, 216, 216, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush9 = QBrush(QColor(236, 235, 235, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush9)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush10 = QBrush(QColor(145, 144, 144, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush10)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush9)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush10)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush10)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.ceiMonthsList.setPalette(palette1)
        self.ceiMonthsList.setLayoutDirection(Qt.LeftToRight)
        self.ceiMonthsList.setStyleSheet(u"QComboBox {padding-left: 180px}")
        self.ceiMonthsList.setEditable(True)
        self.ceiMonthsList.setMaxVisibleItems(99)
        self.ceiMonthsList.setMaxCount(99)

        self.ceiFrameLayout.addWidget(self.ceiMonthsList)

        self.ceiOptionsFrame = QFrame(self.ceiFrame)
        self.ceiOptionsFrame.setObjectName(u"ceiOptionsFrame")
        self.ceiOptionsFrame.setFrameShape(QFrame.NoFrame)
        self.ceiOptionsFrame.setFrameShadow(QFrame.Raised)
        self.ceiOptionsFrameLayout = QHBoxLayout(self.ceiOptionsFrame)
        self.ceiOptionsFrameLayout.setObjectName(u"ceiOptionsFrameLayout")
        self.ceiOptionsFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.ceiImportStocksButton = QPushButton(self.ceiOptionsFrame)
        self.ceiImportStocksButton.setObjectName(u"ceiImportStocksButton")
        sizePolicy1.setHeightForWidth(self.ceiImportStocksButton.sizePolicy().hasHeightForWidth())
        self.ceiImportStocksButton.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(12)
        self.ceiImportStocksButton.setFont(font2)

        self.ceiOptionsFrameLayout.addWidget(self.ceiImportStocksButton)

        self.ceiImportTransactionsButton = QPushButton(self.ceiOptionsFrame)
        self.ceiImportTransactionsButton.setObjectName(u"ceiImportTransactionsButton")
        sizePolicy1.setHeightForWidth(self.ceiImportTransactionsButton.sizePolicy().hasHeightForWidth())
        self.ceiImportTransactionsButton.setSizePolicy(sizePolicy1)
        self.ceiImportTransactionsButton.setFont(font2)

        self.ceiOptionsFrameLayout.addWidget(self.ceiImportTransactionsButton)


        self.ceiFrameLayout.addWidget(self.ceiOptionsFrame)

        self.ceiLoginButton = QPushButton(self.ceiFrame)
        self.ceiLoginButton.setObjectName(u"ceiLoginButton")
        sizePolicy1.setHeightForWidth(self.ceiLoginButton.sizePolicy().hasHeightForWidth())
        self.ceiLoginButton.setSizePolicy(sizePolicy1)
        self.ceiLoginButton.setFont(font2)

        self.ceiFrameLayout.addWidget(self.ceiLoginButton)

        self.ceiProgressBar = QProgressBar(self.ceiFrame)
        self.ceiProgressBar.setObjectName(u"ceiProgressBar")
        sizePolicy1.setHeightForWidth(self.ceiProgressBar.sizePolicy().hasHeightForWidth())
        self.ceiProgressBar.setSizePolicy(sizePolicy1)
        self.ceiProgressBar.setStyleSheet(u"QProgressBar {\n"
"    border: 3px solid grey;\n"
"    border-radius: 8px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: lightblue;\n"
"    border-radius: 8px;\n"
"    width: 3px;\n"
"    margin: 0.5px;\n"
"}")
        self.ceiProgressBar.setMaximum(0)
        self.ceiProgressBar.setValue(0)

        self.ceiFrameLayout.addWidget(self.ceiProgressBar)

        self.ceiErrorMessage = QLabel(self.ceiFrame)
        self.ceiErrorMessage.setObjectName(u"ceiErrorMessage")
        font3 = QFont()
        font3.setPointSize(14)
        self.ceiErrorMessage.setFont(font3)
        self.ceiErrorMessage.setStyleSheet(u"color: red")
        self.ceiErrorMessage.setAlignment(Qt.AlignCenter)
        self.ceiErrorMessage.setWordWrap(True)

        self.ceiFrameLayout.addWidget(self.ceiErrorMessage)

        self.ceiFrameLayout.setStretch(0, 3)
        self.ceiFrameLayout.setStretch(1, 2)
        self.ceiFrameLayout.setStretch(2, 2)
        self.ceiFrameLayout.setStretch(3, 2)
        self.ceiFrameLayout.setStretch(4, 2)
        self.ceiFrameLayout.setStretch(5, 2)

        self.guiLayout.addWidget(self.ceiFrame)

        self.stocksFrame = QFrame(Gui)
        self.stocksFrame.setObjectName(u"stocksFrame")
        self.stocksFrame.setFrameShape(QFrame.NoFrame)
        self.stocksFrame.setFrameShadow(QFrame.Raised)
        self.stocksFrameLayout = QHBoxLayout(self.stocksFrame)
        self.stocksFrameLayout.setSpacing(18)
        self.stocksFrameLayout.setObjectName(u"stocksFrameLayout")
        self.stocksFrameLayout.setContentsMargins(9, 9, -1, 9)
        self.addFrame = QFrame(self.stocksFrame)
        self.addFrame.setObjectName(u"addFrame")
        self.addFrame.setFrameShape(QFrame.NoFrame)
        self.addFrame.setFrameShadow(QFrame.Raised)
        self.addFrameLayout = QVBoxLayout(self.addFrame)
        self.addFrameLayout.setObjectName(u"addFrameLayout")
        self.addFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.addStockButton = QPushButton(self.addFrame)
        self.addStockButton.setObjectName(u"addStockButton")
        sizePolicy1.setHeightForWidth(self.addStockButton.sizePolicy().hasHeightForWidth())
        self.addStockButton.setSizePolicy(sizePolicy1)
        self.addStockButton.setFont(font2)

        self.addFrameLayout.addWidget(self.addStockButton)

        self.addTransactionButton = QPushButton(self.addFrame)
        self.addTransactionButton.setObjectName(u"addTransactionButton")
        sizePolicy1.setHeightForWidth(self.addTransactionButton.sizePolicy().hasHeightForWidth())
        self.addTransactionButton.setSizePolicy(sizePolicy1)
        self.addTransactionButton.setFont(font2)

        self.addFrameLayout.addWidget(self.addTransactionButton)


        self.stocksFrameLayout.addWidget(self.addFrame)

        self.consultFrame = QFrame(self.stocksFrame)
        self.consultFrame.setObjectName(u"consultFrame")
        self.consultFrame.setFrameShape(QFrame.NoFrame)
        self.consultFrame.setFrameShadow(QFrame.Raised)
        self.consultFrameLayout = QVBoxLayout(self.consultFrame)
        self.consultFrameLayout.setObjectName(u"consultFrameLayout")
        self.consultFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.consultStockButton = QPushButton(self.consultFrame)
        self.consultStockButton.setObjectName(u"consultStockButton")
        sizePolicy1.setHeightForWidth(self.consultStockButton.sizePolicy().hasHeightForWidth())
        self.consultStockButton.setSizePolicy(sizePolicy1)
        self.consultStockButton.setFont(font2)

        self.consultFrameLayout.addWidget(self.consultStockButton)

        self.consultTransactionButton = QPushButton(self.consultFrame)
        self.consultTransactionButton.setObjectName(u"consultTransactionButton")
        sizePolicy1.setHeightForWidth(self.consultTransactionButton.sizePolicy().hasHeightForWidth())
        self.consultTransactionButton.setSizePolicy(sizePolicy1)
        self.consultTransactionButton.setFont(font2)

        self.consultFrameLayout.addWidget(self.consultTransactionButton)


        self.stocksFrameLayout.addWidget(self.consultFrame)


        self.guiLayout.addWidget(self.stocksFrame)

        self.summaryFrame = QFrame(Gui)
        self.summaryFrame.setObjectName(u"summaryFrame")
        self.summaryFrame.setFrameShape(QFrame.StyledPanel)
        self.summaryFrame.setFrameShadow(QFrame.Raised)
        self.summaryFrameLayout = QVBoxLayout(self.summaryFrame)
        self.summaryFrameLayout.setObjectName(u"summaryFrameLayout")
        self.titleLayout = QHBoxLayout()
        self.titleLayout.setObjectName(u"titleLayout")
        self.titleLabel = QLabel(self.summaryFrame)
        self.titleLabel.setObjectName(u"titleLabel")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.titleLabel.setFont(font4)
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.titleLayout.addWidget(self.titleLabel)

        self.swingTradeLabel = QLabel(self.summaryFrame)
        self.swingTradeLabel.setObjectName(u"swingTradeLabel")
        self.swingTradeLabel.setFont(font2)
        self.swingTradeLabel.setAlignment(Qt.AlignCenter)
        self.swingTradeLabel.setWordWrap(True)

        self.titleLayout.addWidget(self.swingTradeLabel)

        self.dayTradeLabel = QLabel(self.summaryFrame)
        self.dayTradeLabel.setObjectName(u"dayTradeLabel")
        self.dayTradeLabel.setFont(font2)
        self.dayTradeLabel.setAlignment(Qt.AlignCenter)

        self.titleLayout.addWidget(self.dayTradeLabel)

        self.realEstateFundsLabel = QLabel(self.summaryFrame)
        self.realEstateFundsLabel.setObjectName(u"realEstateFundsLabel")
        self.realEstateFundsLabel.setFont(font2)
        self.realEstateFundsLabel.setAlignment(Qt.AlignCenter)

        self.titleLayout.addWidget(self.realEstateFundsLabel)

        self.titleLayout.setStretch(0, 8)
        self.titleLayout.setStretch(1, 10)
        self.titleLayout.setStretch(2, 10)
        self.titleLayout.setStretch(3, 10)

        self.summaryFrameLayout.addLayout(self.titleLayout)

        self.horizontalLine = QFrame(self.summaryFrame)
        self.horizontalLine.setObjectName(u"horizontalLine")
        self.horizontalLine.setFrameShape(QFrame.HLine)
        self.horizontalLine.setFrameShadow(QFrame.Sunken)

        self.summaryFrameLayout.addWidget(self.horizontalLine)

        self.totalPurchaseLayout = QHBoxLayout()
        self.totalPurchaseLayout.setObjectName(u"totalPurchaseLayout")
        self.totalPurchaseLayout.setContentsMargins(-1, -1, 0, -1)
        self.totalPurchaseLabel = QLabel(self.summaryFrame)
        self.totalPurchaseLabel.setObjectName(u"totalPurchaseLabel")
        self.totalPurchaseLabel.setFont(font2)
        self.totalPurchaseLabel.setAlignment(Qt.AlignCenter)

        self.totalPurchaseLayout.addWidget(self.totalPurchaseLabel)

        self.swingTradeTotalPurchaseLabel = QLabel(self.summaryFrame)
        self.swingTradeTotalPurchaseLabel.setObjectName(u"swingTradeTotalPurchaseLabel")
        self.swingTradeTotalPurchaseLabel.setFont(font2)
        self.swingTradeTotalPurchaseLabel.setAlignment(Qt.AlignCenter)

        self.totalPurchaseLayout.addWidget(self.swingTradeTotalPurchaseLabel)

        self.dayTradeTotalPurchaseLabel = QLabel(self.summaryFrame)
        self.dayTradeTotalPurchaseLabel.setObjectName(u"dayTradeTotalPurchaseLabel")
        self.dayTradeTotalPurchaseLabel.setFont(font2)
        self.dayTradeTotalPurchaseLabel.setAlignment(Qt.AlignCenter)

        self.totalPurchaseLayout.addWidget(self.dayTradeTotalPurchaseLabel)

        self.realEstateFundsTotalPurchaseLabel = QLabel(self.summaryFrame)
        self.realEstateFundsTotalPurchaseLabel.setObjectName(u"realEstateFundsTotalPurchaseLabel")
        self.realEstateFundsTotalPurchaseLabel.setFont(font2)
        self.realEstateFundsTotalPurchaseLabel.setAlignment(Qt.AlignCenter)

        self.totalPurchaseLayout.addWidget(self.realEstateFundsTotalPurchaseLabel)

        self.totalPurchaseLayout.setStretch(0, 8)
        self.totalPurchaseLayout.setStretch(1, 10)
        self.totalPurchaseLayout.setStretch(2, 10)
        self.totalPurchaseLayout.setStretch(3, 10)

        self.summaryFrameLayout.addLayout(self.totalPurchaseLayout)

        self.totalSoldLayout = QHBoxLayout()
        self.totalSoldLayout.setObjectName(u"totalSoldLayout")
        self.totalSoldLayout.setContentsMargins(-1, -1, 0, -1)
        self.totalSoldLabel = QLabel(self.summaryFrame)
        self.totalSoldLabel.setObjectName(u"totalSoldLabel")
        self.totalSoldLabel.setFont(font2)
        self.totalSoldLabel.setAlignment(Qt.AlignCenter)

        self.totalSoldLayout.addWidget(self.totalSoldLabel)

        self.swingTradeTotalSoldLabel = QLabel(self.summaryFrame)
        self.swingTradeTotalSoldLabel.setObjectName(u"swingTradeTotalSoldLabel")
        self.swingTradeTotalSoldLabel.setFont(font2)
        self.swingTradeTotalSoldLabel.setAlignment(Qt.AlignCenter)

        self.totalSoldLayout.addWidget(self.swingTradeTotalSoldLabel)

        self.dayTradeTotalSoldLabel = QLabel(self.summaryFrame)
        self.dayTradeTotalSoldLabel.setObjectName(u"dayTradeTotalSoldLabel")
        self.dayTradeTotalSoldLabel.setFont(font2)
        self.dayTradeTotalSoldLabel.setAlignment(Qt.AlignCenter)

        self.totalSoldLayout.addWidget(self.dayTradeTotalSoldLabel)

        self.realEstateFundsTotalSoldLabel = QLabel(self.summaryFrame)
        self.realEstateFundsTotalSoldLabel.setObjectName(u"realEstateFundsTotalSoldLabel")
        self.realEstateFundsTotalSoldLabel.setFont(font2)
        self.realEstateFundsTotalSoldLabel.setAlignment(Qt.AlignCenter)

        self.totalSoldLayout.addWidget(self.realEstateFundsTotalSoldLabel)

        self.totalSoldLayout.setStretch(0, 8)
        self.totalSoldLayout.setStretch(1, 10)
        self.totalSoldLayout.setStretch(2, 10)
        self.totalSoldLayout.setStretch(3, 10)

        self.summaryFrameLayout.addLayout(self.totalSoldLayout)

        self.totalProfitLayout = QHBoxLayout()
        self.totalProfitLayout.setObjectName(u"totalProfitLayout")
        self.totalProfitLayout.setContentsMargins(-1, -1, 0, -1)
        self.totalProfitLabel = QLabel(self.summaryFrame)
        self.totalProfitLabel.setObjectName(u"totalProfitLabel")
        self.totalProfitLabel.setFont(font2)
        self.totalProfitLabel.setAlignment(Qt.AlignCenter)

        self.totalProfitLayout.addWidget(self.totalProfitLabel)

        self.swingTradeTotalProfitLabel = QLabel(self.summaryFrame)
        self.swingTradeTotalProfitLabel.setObjectName(u"swingTradeTotalProfitLabel")
        self.swingTradeTotalProfitLabel.setFont(font2)
        self.swingTradeTotalProfitLabel.setAlignment(Qt.AlignCenter)

        self.totalProfitLayout.addWidget(self.swingTradeTotalProfitLabel)

        self.dayTradeTotalProfitLabel = QLabel(self.summaryFrame)
        self.dayTradeTotalProfitLabel.setObjectName(u"dayTradeTotalProfitLabel")
        self.dayTradeTotalProfitLabel.setFont(font2)
        self.dayTradeTotalProfitLabel.setAlignment(Qt.AlignCenter)

        self.totalProfitLayout.addWidget(self.dayTradeTotalProfitLabel)

        self.realEstateFundsTotalProfitLabel = QLabel(self.summaryFrame)
        self.realEstateFundsTotalProfitLabel.setObjectName(u"realEstateFundsTotalProfitLabel")
        self.realEstateFundsTotalProfitLabel.setFont(font2)
        self.realEstateFundsTotalProfitLabel.setAlignment(Qt.AlignCenter)

        self.totalProfitLayout.addWidget(self.realEstateFundsTotalProfitLabel)

        self.totalProfitLayout.setStretch(0, 8)
        self.totalProfitLayout.setStretch(1, 10)
        self.totalProfitLayout.setStretch(2, 10)
        self.totalProfitLayout.setStretch(3, 10)

        self.summaryFrameLayout.addLayout(self.totalProfitLayout)

        self.accumulatedLossLayout = QHBoxLayout()
        self.accumulatedLossLayout.setObjectName(u"accumulatedLossLayout")
        self.accumulatedLossLayout.setContentsMargins(-1, -1, 0, -1)
        self.accumulatedLossLabel = QLabel(self.summaryFrame)
        self.accumulatedLossLabel.setObjectName(u"accumulatedLossLabel")
        self.accumulatedLossLabel.setFont(font2)
        self.accumulatedLossLabel.setAlignment(Qt.AlignCenter)

        self.accumulatedLossLayout.addWidget(self.accumulatedLossLabel)

        self.swingTradeAccumulatedLossLabel = QLabel(self.summaryFrame)
        self.swingTradeAccumulatedLossLabel.setObjectName(u"swingTradeAccumulatedLossLabel")
        self.swingTradeAccumulatedLossLabel.setFont(font2)
        self.swingTradeAccumulatedLossLabel.setAlignment(Qt.AlignCenter)

        self.accumulatedLossLayout.addWidget(self.swingTradeAccumulatedLossLabel)

        self.dayTradeAccumulatedLossLabel = QLabel(self.summaryFrame)
        self.dayTradeAccumulatedLossLabel.setObjectName(u"dayTradeAccumulatedLossLabel")
        self.dayTradeAccumulatedLossLabel.setFont(font2)
        self.dayTradeAccumulatedLossLabel.setAlignment(Qt.AlignCenter)

        self.accumulatedLossLayout.addWidget(self.dayTradeAccumulatedLossLabel)

        self.realEstateFundsAccumulatedLossLabel = QLabel(self.summaryFrame)
        self.realEstateFundsAccumulatedLossLabel.setObjectName(u"realEstateFundsAccumulatedLossLabel")
        self.realEstateFundsAccumulatedLossLabel.setFont(font2)
        self.realEstateFundsAccumulatedLossLabel.setAlignment(Qt.AlignCenter)

        self.accumulatedLossLayout.addWidget(self.realEstateFundsAccumulatedLossLabel)

        self.accumulatedLossLayout.setStretch(0, 8)
        self.accumulatedLossLayout.setStretch(1, 10)
        self.accumulatedLossLayout.setStretch(2, 10)
        self.accumulatedLossLayout.setStretch(3, 10)

        self.summaryFrameLayout.addLayout(self.accumulatedLossLayout)

        self.dueTaxLayout = QHBoxLayout()
        self.dueTaxLayout.setObjectName(u"dueTaxLayout")
        self.dueTaxLayout.setContentsMargins(-1, -1, 0, -1)
        self.dueTaxLabel = QLabel(self.summaryFrame)
        self.dueTaxLabel.setObjectName(u"dueTaxLabel")
        self.dueTaxLabel.setFont(font2)
        self.dueTaxLabel.setAlignment(Qt.AlignCenter)

        self.dueTaxLayout.addWidget(self.dueTaxLabel)

        self.swingTradeDueTaxLabel = QLabel(self.summaryFrame)
        self.swingTradeDueTaxLabel.setObjectName(u"swingTradeDueTaxLabel")
        self.swingTradeDueTaxLabel.setFont(font2)
        self.swingTradeDueTaxLabel.setAlignment(Qt.AlignCenter)

        self.dueTaxLayout.addWidget(self.swingTradeDueTaxLabel)

        self.dayTradeDueTaxLabel = QLabel(self.summaryFrame)
        self.dayTradeDueTaxLabel.setObjectName(u"dayTradeDueTaxLabel")
        self.dayTradeDueTaxLabel.setFont(font2)
        self.dayTradeDueTaxLabel.setAlignment(Qt.AlignCenter)

        self.dueTaxLayout.addWidget(self.dayTradeDueTaxLabel)

        self.realEstateFundsDueTaxLabel = QLabel(self.summaryFrame)
        self.realEstateFundsDueTaxLabel.setObjectName(u"realEstateFundsDueTaxLabel")
        self.realEstateFundsDueTaxLabel.setFont(font2)
        self.realEstateFundsDueTaxLabel.setAlignment(Qt.AlignCenter)

        self.dueTaxLayout.addWidget(self.realEstateFundsDueTaxLabel)

        self.dueTaxLayout.setStretch(0, 8)
        self.dueTaxLayout.setStretch(1, 10)
        self.dueTaxLayout.setStretch(2, 10)
        self.dueTaxLayout.setStretch(3, 10)

        self.summaryFrameLayout.addLayout(self.dueTaxLayout)


        self.guiLayout.addWidget(self.summaryFrame)

        self.darfGenerationFrame = QFrame(Gui)
        self.darfGenerationFrame.setObjectName(u"darfGenerationFrame")
        self.darfGenerationFrame.setFrameShape(QFrame.NoFrame)
        self.darfGenerationFrame.setFrameShadow(QFrame.Raised)
        self.darfGenerationFrameLayout = QHBoxLayout(self.darfGenerationFrame)
        self.darfGenerationFrameLayout.setObjectName(u"darfGenerationFrameLayout")
        self.darfGenerationFrameLayout.setContentsMargins(-1, 9, -1, -1)
        self.darfValueLayout = QVBoxLayout()
        self.darfValueLayout.setObjectName(u"darfValueLayout")
        self.darfValueTitleLabel = QLabel(self.darfGenerationFrame)
        self.darfValueTitleLabel.setObjectName(u"darfValueTitleLabel")
        self.darfValueTitleLabel.setFont(font)
        self.darfValueTitleLabel.setStyleSheet(u"")
        self.darfValueTitleLabel.setAlignment(Qt.AlignCenter)

        self.darfValueLayout.addWidget(self.darfValueTitleLabel)

        self.darfValueOutputLabel = QLabel(self.darfGenerationFrame)
        self.darfValueOutputLabel.setObjectName(u"darfValueOutputLabel")
        font5 = QFont()
        font5.setPointSize(20)
        font5.setBold(True)
        font5.setWeight(75)
        self.darfValueOutputLabel.setFont(font5)
        self.darfValueOutputLabel.setAlignment(Qt.AlignCenter)

        self.darfValueLayout.addWidget(self.darfValueOutputLabel)


        self.darfGenerationFrameLayout.addLayout(self.darfValueLayout)

        self.darfGenerationSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.darfGenerationFrameLayout.addItem(self.darfGenerationSpacer)

        self.darfGenerationButton = QPushButton(self.darfGenerationFrame)
        self.darfGenerationButton.setObjectName(u"darfGenerationButton")
        self.darfGenerationButton.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.darfGenerationButton.sizePolicy().hasHeightForWidth())
        self.darfGenerationButton.setSizePolicy(sizePolicy1)
        self.darfGenerationButton.setFont(font5)

        self.darfGenerationFrameLayout.addWidget(self.darfGenerationButton)

        self.darfGenerationFrameLayout.setStretch(0, 3)
        self.darfGenerationFrameLayout.setStretch(1, 1)
        self.darfGenerationFrameLayout.setStretch(2, 3)

        self.guiLayout.addWidget(self.darfGenerationFrame)

        self.guiLayout.setStretch(0, 5)
        self.guiLayout.setStretch(1, 2)
        self.guiLayout.setStretch(2, 10)
        self.guiLayout.setStretch(3, 3)
        QWidget.setTabOrder(self.ceiCpfInput, self.ceiPasswordInput)
        QWidget.setTabOrder(self.ceiPasswordInput, self.ceiImportStocksButton)
        QWidget.setTabOrder(self.ceiImportStocksButton, self.ceiImportTransactionsButton)
        QWidget.setTabOrder(self.ceiImportTransactionsButton, self.ceiLoginButton)
        QWidget.setTabOrder(self.ceiLoginButton, self.addStockButton)
        QWidget.setTabOrder(self.addStockButton, self.consultStockButton)
        QWidget.setTabOrder(self.consultStockButton, self.addTransactionButton)
        QWidget.setTabOrder(self.addTransactionButton, self.consultTransactionButton)
        QWidget.setTabOrder(self.consultTransactionButton, self.darfGenerationButton)

        self.retranslateUi(Gui)

        QMetaObject.connectSlotsByName(Gui)
    # setupUi

    def retranslateUi(self, Gui):
        Gui.setWindowTitle(QCoreApplication.translate("Gui", u"Gerador de Darf", None))
        self.ceiLabel.setText(QCoreApplication.translate("Gui", u"CEI - B3", None))
        self.ceiCpfInput.setPlaceholderText(QCoreApplication.translate("Gui", u"CPF", None))
        self.ceiPasswordInput.setText("")
        self.ceiPasswordInput.setPlaceholderText(QCoreApplication.translate("Gui", u"Senha", None))
        self.ceiMonthsList.setCurrentText("")
        self.ceiImportStocksButton.setText(QCoreApplication.translate("Gui", u"Importar A\u00e7\u00f5es", None))
        self.ceiImportTransactionsButton.setText(QCoreApplication.translate("Gui", u"Importar Transa\u00e7\u00f5es", None))
        self.ceiLoginButton.setText(QCoreApplication.translate("Gui", u"Entrar", None))
        self.ceiErrorMessage.setText(QCoreApplication.translate("Gui", u"Mensagem de erro aqui", None))
        self.addStockButton.setText(QCoreApplication.translate("Gui", u"Adicionar A\u00e7\u00e3o", None))
        self.addTransactionButton.setText(QCoreApplication.translate("Gui", u"Adicionar Transa\u00e7\u00e3o", None))
        self.consultStockButton.setText(QCoreApplication.translate("Gui", u"Consultar A\u00e7\u00f5es", None))
        self.consultTransactionButton.setText(QCoreApplication.translate("Gui", u"Consultar Transa\u00e7\u00f5es", None))
        self.titleLabel.setText(QCoreApplication.translate("Gui", u"A\u00e7\u00f5es", None))
        self.swingTradeLabel.setText(QCoreApplication.translate("Gui", u"Swing\n"
" Trade", None))
        self.dayTradeLabel.setText(QCoreApplication.translate("Gui", u"Day\n"
" Trade", None))
        self.realEstateFundsLabel.setText(QCoreApplication.translate("Gui", u"Fundos\n"
" Imobili\u00e1rios", None))
        self.totalPurchaseLabel.setText(QCoreApplication.translate("Gui", u"Comprado", None))
        self.swingTradeTotalPurchaseLabel.setText(QCoreApplication.translate("Gui", u"R$ 0,00", None))
        self.dayTradeTotalPurchaseLabel.setText(QCoreApplication.translate("Gui", u"R$ 0,00", None))
        self.realEstateFundsTotalPurchaseLabel.setText(QCoreApplication.translate("Gui", u"R$ 0,00", None))
        self.totalSoldLabel.setText(QCoreApplication.translate("Gui", u"Vendido", None))
        self.swingTradeTotalSoldLabel.setText(QCoreApplication.translate("Gui", u"R$ 0,00", None))
        self.dayTradeTotalSoldLabel.setText(QCoreApplication.translate("Gui", u"R$ 0,00", None))
        self.realEstateFundsTotalSoldLabel.setText(QCoreApplication.translate("Gui", u"R$ 0,00", None))
        self.totalProfitLabel.setText(QCoreApplication.translate("Gui", u"Lucro", None))
        self.swingTradeTotalProfitLabel.setText(QCoreApplication.translate("Gui", u"R$ 0,00", None))
        self.dayTradeTotalProfitLabel.setText(QCoreApplication.translate("Gui", u"R$ 0,00", None))
        self.realEstateFundsTotalProfitLabel.setText(QCoreApplication.translate("Gui", u"R$ 0,00", None))
        self.accumulatedLossLabel.setText(QCoreApplication.translate("Gui", u"Preju\u00edzo\n"
" Acumulado", None))
        self.swingTradeAccumulatedLossLabel.setText(QCoreApplication.translate("Gui", u"R$ 0,00", None))
        self.dayTradeAccumulatedLossLabel.setText(QCoreApplication.translate("Gui", u"R$ 0,00", None))
        self.realEstateFundsAccumulatedLossLabel.setText(QCoreApplication.translate("Gui", u"R$ 0,00", None))
        self.dueTaxLabel.setText(QCoreApplication.translate("Gui", u"Imposto", None))
        self.swingTradeDueTaxLabel.setText(QCoreApplication.translate("Gui", u"R$ 0,00", None))
        self.dayTradeDueTaxLabel.setText(QCoreApplication.translate("Gui", u"R$ 0,00", None))
        self.realEstateFundsDueTaxLabel.setText(QCoreApplication.translate("Gui", u"R$ 0,00", None))
        self.darfValueTitleLabel.setText(QCoreApplication.translate("Gui", u"VALOR DARF", None))
        self.darfValueOutputLabel.setText(QCoreApplication.translate("Gui", u"R$ 0,00", None))
        self.darfGenerationButton.setText(QCoreApplication.translate("Gui", u"Gerar\n"
" Boleto", None))
    # retranslateUi

