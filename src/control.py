#!/usr/bin/python3

from stock import StockTypes
from stock import Stock
import logging

class Control:

# Initialize the class with its properties
#----------------------------------------------------------------------------------------------------------------------
    def __init__(self, debug=False):
        self.__stocks = []
        self.__debug = debug

# Add a new stock to the class
#----------------------------------------------------------------------------------------------------------------------
    def add_stock(self, name, buy_day, buy_month, buy_year, sell_day, sell_month, sell_year, ammount_sold, buy_price,
        sell_price, type, paid_fares):
        logging.debug('Adding new stock: %s', name)
        stock = Stock()
        stock.name = name
        stock.buy_price = buy_price
        stock.ammount_sold = ammount_sold
        stock.sell_price = sell_price
        stock.set_buy_date(buy_year, buy_month, buy_day)
        stock.set_sell_date(sell_year, sell_month, sell_day)
        stock.paid_fares = paid_fares
        stock.type = type
        self.__stocks.append(stock)

# Get stocks
#----------------------------------------------------------------------------------------------------------------------
    @property
    def stocks(self):
        logging.debug('Returning the registered stocks...')
        return self.__stocks

# Set log level
#----------------------------------------------------------------------------------------------------------------------
    def set_log_level(self, debug):
        if (debug):
            logging.basicConfig(level=1)
            logging.debug('Log debug level activated!')
        else:
            logging.basicConfig(level=logging.INFO)

#----------------------------------------------------------------------------------------------------------------------
