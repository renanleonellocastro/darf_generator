#!/usr/bin/python3

import logging
from src.control import Control
from include.stock import StockTypes
from include.transaction import TransactionTypes

class Test:

# Initialize the class with its properties
#----------------------------------------------------------------------------------------------------------------------
    def __init__(self, debug=False):
        self.__control = Control(debug)

# Test1
#----------------------------------------------------------------------------------------------------------------------
    def test1(self):
        logging.debug('Executing test 1')
        self.__control.add_stock('teste1-fi', 10.0, StockTypes.FI, 10, 1.20)
        self.__control.add_stock('teste1-normal', 10.0, StockTypes.NORMAL, 10, 2.40)
        self.__control.add_transaction('teste1-fi', 10.0, StockTypes.FI, 10, 1.57, 1, 1, 2020,\
        TransactionTypes.PURCHASE, 1)
        self.__control.add_transaction('teste1-normal', 10.0, StockTypes.NORMAL, 10, 1.75, 2, 1, 2020,\
        TransactionTypes.PURCHASE, 2)
        self.__control.add_transaction('teste1-fi', 20.0, StockTypes.FI, 20, 1.36, 2, 1, 2020,\
        TransactionTypes.SALE, 3)
        self.__control.add_transaction('teste1-normal', 20.0, StockTypes.NORMAL, 20, 1.89, 3, 1, 2020,\
        TransactionTypes.SALE, 4)
        self.__control.calculate_darf()
        logging.info('Total Purchase FI: %f', self.__control.get_total_purchase_of_fi_stocks())
        logging.info('Total Purchase NORMAL: %f', self.__control.get_total_purchase_of_normal_stocks())
        logging.info('Total Purchase DAY_TRADE: %f', self.__control.get_total_purchase_of_day_trade_stocks())
        logging.info('Total Sale FI: %f', self.__control.get_total_sale_of_fi_stocks())
        logging.info('Total Sale NORMAL: %f', self.__control.get_total_sale_of_normal_stocks())
        logging.info('Total Sale DAY_TRADE: %f', self.__control.get_total_sale_of_day_trade_stocks())
        logging.info('Total Profit FI: %f', self.__control.get_total_profit_of_fi_stocks())
        logging.info('Total Profit NORMAL: %f', self.__control.get_total_profit_of_normal_stocks())
        logging.info('Total Profit DAY_TRADE: %f', self.__control.get_total_profit_of_day_trade_stocks())
        logging.info('Total Tax FI: %f', self.__control.get_total_due_tax_of_fi_stocks())
        logging.info('Total Tax NORMAL: %f', self.__control.get_total_due_tax_of_normal_stocks())
        logging.info('Total Tax DAY_TRADE: %f', self.__control.get_total_due_tax_of_day_trade_stocks())
        logging.info('DARF VALUE: %f', self.__control.darf_value)
#----------------------------------------------------------------------------------------------------------------------

test = Test(False)
test.test1()