#!/usr/bin/python3

import logging
from datetime import date
import enum

class StockTypes(enum.Enum):
    NORMAL = 1
    FI = 2
    DAY_TRADE = 3
    
class Stock:

# Initialize the class with its properties
#----------------------------------------------------------------------------------------------------------------------
    def __init__(self, debug=False):
        self.__name = "Acao sem nome"
        self.__buy_date = None
        self.__buy_price = 0.0
        self.__ammount_sold = 0
        self.__sell_price = 0.0
        self.__sell_date = None
        self.__type = StockTypes.NORMAL
        self.__paid_fares = 0.0
        self.__debug = debug

# Get class member "name"
#----------------------------------------------------------------------------------------------------------------------
    @property
    def name(self):
        logging.debug('Returning the stock name: %s!', self.__name)
        return self.__name

# Set class member "name"
#----------------------------------------------------------------------------------------------------------------------
    @name.setter
    def name(self, new_name):
        logging.debug('Setting the stock name: %s!', new_name)
        self.__name = new_name

# Get class member "buy_price"
#----------------------------------------------------------------------------------------------------------------------
    @property
    def buy_price(self):
        logging.debug('Returning the stock buy_price: %f!', self.__buy_price)
        return self.__buy_price

# Set class member "buy_price"
#----------------------------------------------------------------------------------------------------------------------
    @buy_price.setter
    def buy_price(self, new_buy_price):
        logging.debug('Setting the stock buy_price: %f!', new_buy_price)
        self.__buy_price = new_buy_price

# Get class member "ammount_sold"
#----------------------------------------------------------------------------------------------------------------------
    @property
    def ammount_sold(self):
        logging.debug('Returning the stock ammount_sold: %d!', self.__ammount_sold)
        return self.__ammount_sold

# Set class member "ammount_sold"
#----------------------------------------------------------------------------------------------------------------------
    @ammount_sold.setter
    def ammount_sold(self, new_ammount_sold):
        logging.debug('Setting the stock ammount_sold: %d!', new_ammount_sold)
        self.__ammount_sold = new_ammount_sold

# Get class member "sell_price"
#----------------------------------------------------------------------------------------------------------------------
    @property
    def sell_price(self):
        logging.debug('Returning the stock sell_price: %f!', self.__sell_price)
        return self.__sell_price

# Set class member "sell_price"
#----------------------------------------------------------------------------------------------------------------------
    @sell_price.setter
    def sell_price(self, new_sell_price):
        logging.debug('Setting the stock sell_price: %f!', new_sell_price)
        self.__sell_price = new_sell_price

# Get class member "buy_date"
#----------------------------------------------------------------------------------------------------------------------
    @property
    def buy_date(self):
        logging.debug('Returning the stock buy_date...')
        return self.__buy_date

# Set class member "buy_date"
#----------------------------------------------------------------------------------------------------------------------
    def set_buy_date(self, year, month, day):
        logging.debug('Setting the stock buy_date: %d-%d-%d!', day, month, year)
        self.__buy_date = date(year, month, day)

# Get class member "sell_date"
#----------------------------------------------------------------------------------------------------------------------
    @property
    def sell_date(self):
        logging.debug('Returning the stock sell_date...')
        return self.__sell_date

# Set class member "sell_date"
#----------------------------------------------------------------------------------------------------------------------
    def set_sell_date(self, year, month, day):
        logging.debug('Setting the stock sell_date: %d-%d-%d!', day, month, year)
        self.__sell_date = date(year, month, day)

# Get class member "type"
#----------------------------------------------------------------------------------------------------------------------
    @property
    def type(self):
        logging.debug('Setting the stock type: %d!', self.__type)
        return self.__type

# Set class member "type"
#----------------------------------------------------------------------------------------------------------------------
    @type.setter
    def type(self, new_type):
        logging.debug('Setting the stock type: %d!', new_type.value)
        self.__type = new_type
        if self.__type == StockTypes.NORMAL:
            if self.is_day_trade():
                logging.debbug('Day trade detected!')
                self.__type = StockTypes.DAY_TRADE

# Get class member "paid_fares"
#----------------------------------------------------------------------------------------------------------------------
    @property
    def paid_fares(self):
        logging.debug('Returning the stock paid_fares: %f!', self.__paid_fares)
        return self.__paid_fares

# Set class member "paid_fares"
#----------------------------------------------------------------------------------------------------------------------
    @paid_fares.setter
    def paid_fares(self, new_paid_fares):
        logging.debug('Setting the stock paid fares: %d!', new_paid_fares)
        self.__paid_fares = new_paid_fares

# Return total sold value
#----------------------------------------------------------------------------------------------------------------------
    @property
    def total_sold(self):
        logging.debug('Return the total sold value...')
        total = self.__ammount_sold * self.__sell_price
        return total
    
# Return total bought value
#----------------------------------------------------------------------------------------------------------------------
    @property
    def total_bought(self):
        logging.debug('Return the total bought value...')
        total = self.__ammount_sold * self.__buy_price
        return total

# Verify if it is day trade
#----------------------------------------------------------------------------------------------------------------------
    def is_day_trade(self):
        logging.debug('Checking if the stock is day trade...')
        days = (self.__sell_date - self.__buy_date).days
        if days >= 1:
            return False
        else:
            return True

# Calculate due taxes or loss and return the value
#----------------------------------------------------------------------------------------------------------------------
    def calculate_due_taxes_or_loss(self):
        logging.debug('Calculating due taxes or loss and return the value..')
        profit = self.total_sold - self.total_bought
        if profit > 0:
            if self.__type == StockTypes.NORMAL:
                value = profit * 0.15 - self.__paid_fares
            else:
                value = profit * 0.20 - self.__paid_fares
        else:
            value = profit
        return value

#----------------------------------------------------------------------------------------------------------------------
