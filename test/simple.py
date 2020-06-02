#!/usr/bin/python3

import math
import logging
from src.control import Control
from include.stock import StockTypes
from include.transaction import TransactionTypes

class Test:

# Initialize the class with its properties
#----------------------------------------------------------------------------------------------------------------------
    def __init__(self, debug=False):
        self.__debug = debug
        self.__control = Control()

# Check Results
#----------------------------------------------------------------------------------------------------------------------
    def checkResults(self, total_purchase_fi, total_purchase_normal, total_purchase_day_trade, total_sale_fi, \
        total_sale_normal, total_sale_day_trade, total_profit_fi, total_profit_normal, total_profit_day_trade, \
        total_due_tax_fi, total_due_tax_normal, total_due_tax_day_trade, darf_value):
        if (not math.isclose(self.__control.get_total_purchase_of_fi_stocks(), total_purchase_fi)):
            return False
        if (not math.isclose(self.__control.get_total_purchase_of_normal_stocks(), total_purchase_normal)):
            return False
        if (not math.isclose(self.__control.get_total_purchase_of_day_trade_stocks(), total_purchase_day_trade)):
            return False
        if (not math.isclose(self.__control.get_total_sale_of_fi_stocks(), total_sale_fi)):
            return False
        if (not math.isclose(self.__control.get_total_sale_of_normal_stocks(), total_sale_normal)):
            return False
        if (not math.isclose(self.__control.get_total_sale_of_day_trade_stocks(), total_sale_day_trade)):
            return False
        if (not math.isclose(self.__control.get_total_profit_of_fi_stocks(), total_profit_fi)):
            return False
        if (not math.isclose(self.__control.get_total_profit_of_normal_stocks(), total_profit_normal)):
            return False
        if (not math.isclose(self.__control.get_total_profit_of_day_trade_stocks(), total_profit_day_trade)):
            return False
        if (not math.isclose(self.__control.get_total_due_tax_of_fi_stocks(), total_due_tax_fi)):
            return False
        if (not math.isclose(self.__control.get_total_due_tax_of_normal_stocks(), total_due_tax_normal)):
            return False
        if (not math.isclose(self.__control.get_total_due_tax_of_day_trade_stocks(), total_due_tax_day_trade)):
            return False
        if (not math.isclose(self.__control.darf_value, darf_value)):
            return False
        return True

# Test1
#----------------------------------------------------------------------------------------------------------------------
    def test1(self):
        logging.debug('Executing test 1')
        self.__control = Control()
        self.__control.add_stock('fi', 10.0, StockTypes.FI, 10, 1.20)
        self.__control.add_transaction('fi', 10.0, StockTypes.FI, 10, 1.57, 1, 1, 2020,\
        TransactionTypes.PURCHASE, 1)
        self.__control.add_transaction('fi', 20.0, StockTypes.FI, 20, 1.36, 2, 1, 2020,\
        TransactionTypes.SALE, 2)
        self.__control.calculate_darf()
        if (self.checkResults(100.0, 0.0, 0.0, 400.0, 0.0, 0.0, 195.87, 0.0, 0.0, 39.174, 0.0, 0.0, 39.174)):
            print ('OK')
        else:
            print ('NOK')

# Test2
#----------------------------------------------------------------------------------------------------------------------
    def test2(self):
        logging.debug('Executing test 2')
        self.__control = Control()
        self.__control.add_stock('normal', 10.0, StockTypes.NORMAL, 10, 2.40)
        self.__control.add_transaction('normal', 10.0, StockTypes.NORMAL, 10, 1.75, 2, 1, 2020,\
        TransactionTypes.PURCHASE, 1)
        self.__control.add_transaction('normal', 20.0, StockTypes.NORMAL, 20, 1.89, 3, 1, 2020,\
        TransactionTypes.SALE, 2)
        self.__control.calculate_darf()
        if (self.checkResults(0.0, 100.0, 0.0, 0.0, 400.0, 0.0, 0.0, 193.96, 0.0, 0.0, 0.0, 0.0, 0.0)):
            print ('OK')
        else:
            print ('NOK')


# Test3
#----------------------------------------------------------------------------------------------------------------------
    def test3(self):
        logging.debug('Executing test 3')
        self.__control = Control()
        self.__control.add_stock('normal', 10.0, StockTypes.NORMAL, 10, 2.40)
        self.__control.add_transaction('normal', 10.0, StockTypes.NORMAL, 1000, 1.75, 2, 1, 2020,\
        TransactionTypes.PURCHASE, 1)
        self.__control.add_transaction('normal', 20.0, StockTypes.NORMAL, 1010, 1.89, 3, 1, 2020,\
        TransactionTypes.SALE, 2)
        self.__control.calculate_darf()
        if (self.checkResults(0.0, 10000.0, 0.0, 0.0, 20200.0, 0.0, 0.0, 10093.96, 0.0, 0.0, 1514.094, 0.0, 1514.094)):
            print ('OK')
        else:
            print ('NOK')

# Test4
#----------------------------------------------------------------------------------------------------------------------
    def test4(self):
        logging.debug('Executing test 4')
        self.__control = Control()
        self.__control.add_stock('day_trade', 10.0, StockTypes.NORMAL, 10, 3.02)
        self.__control.add_transaction('day_trade', 15.0, StockTypes.NORMAL, 10, 2.46, 2, 1, 2020,\
        TransactionTypes.PURCHASE, 1)
        self.__control.add_transaction('day_trade', 20.0, StockTypes.NORMAL, 10, 2.37, 2, 1, 2020,\
        TransactionTypes.SALE, 2)
        self.__control.calculate_darf()
        if (self.checkResults(0.0, 0.0, 150.0, 0.0, 0.0, 200.0, 0.0, 0.0, 45.17, 0.0, 0.0, 9.034, 9.034)):
            print ('OK')
        else:
            print ('NOK')

#----------------------------------------------------------------------------------------------------------------------

test = Test(False)
test.test1()
test.test2()
test.test3()
test.test4()
