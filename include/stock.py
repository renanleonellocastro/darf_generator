#!/usr/bin/python3

import enum
import logging

class StockTypes(enum.Enum):
    NORMAL = 1
    FI = 2
    DAY_TRADE = 3

class Stock:

# Initialize the class with its properties
#----------------------------------------------------------------------------------------------------------------------
    def __init__(self, name="NoName", price=0.0, category=StockTypes.NORMAL, ammount=1, paid_fares=0.0, debug=False):
        self.__name = name
        self.__price = price
        self.__category = category
        self.__ammount = ammount
        self.__paid_fares = paid_fares
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

# Get class member "price"
#----------------------------------------------------------------------------------------------------------------------
    @property
    def price(self):
        logging.debug('Returning the stock price: %f!', self.__price)
        return self.__price

# Set class member "price"
#----------------------------------------------------------------------------------------------------------------------
    @price.setter
    def price(self, new_price):
        logging.debug('Setting the stock price: %f!', new_price)
        self.__price = new_price

# Get class member "category"
#----------------------------------------------------------------------------------------------------------------------
    @property
    def category(self):
        logging.debug('Returning the stock category: %d!', self.__category)
        return self.__category

# Set class member "category"
#----------------------------------------------------------------------------------------------------------------------
    @category.setter
    def category(self, new_category):
        logging.debug('Setting the stock category: %d!', new_category)
        self.__category = new_category

# Get class member "ammount"
#----------------------------------------------------------------------------------------------------------------------
    @property
    def ammount(self):
        logging.debug('Returning the stock ammount: %d!', self.__ammount)
        return self.__ammount

# Set class member "ammount"
#----------------------------------------------------------------------------------------------------------------------
    @ammount.setter
    def ammount(self, new_ammount):
        logging.debug('Setting the stock ammount: %d!', new_ammount)
        self.__ammount = new_ammount

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

# Return total price value
#----------------------------------------------------------------------------------------------------------------------
    @property
    def total_price(self):
        logging.debug('Return the total price value...')
        total = self.__ammount * self.__price
        return total

#----------------------------------------------------------------------------------------------------------------------
