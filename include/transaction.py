#!/usr/bin/python3

import enum
import logging
from include import stock
from datetime import date

class TransactionTypes(enum.Enum):
    PURCHASE = 1
    SALE = 2

class Transaction(stock.Stock):

# Initialize the class with its properties
#----------------------------------------------------------------------------------------------------------------------
    def __init__(self, name="NoName", price=0.0, category=stock.StockTypes.NORMAL, ammount=1, paid_fares=0.0, 
        day=1, month=1, year=1969, operation_type=TransactionTypes.PURCHASE, operation_id=0, debug=False):
        super().__init__(name, price, category, ammount, paid_fares, debug)
        self.__operation_date = date(year, month, day)
        self.__operation_type = operation_type
        self.__operation_id = operation_id
        self.__debug = debug

# Get class member "operation_date"
#----------------------------------------------------------------------------------------------------------------------
    @property
    def operation_date(self):
        logging.debug('Returning the transaction operation date...')
        return self.__operation_date

# Set class member "operation_date"
#----------------------------------------------------------------------------------------------------------------------
    def set_operation_date(self, year, month, day):
        logging.debug('Setting the transaction operation date: %d-%d-%d!', day, month, year)
        self.__operation_date = date(year, month, day)

# Get class member "operation_type"
#----------------------------------------------------------------------------------------------------------------------
    @property
    def operation_type(self):
        logging.debug('Returning the transaction operation type: %d!', self.__operation_type.value)
        return self.__operation_type

# Set class member "operation_type"
#----------------------------------------------------------------------------------------------------------------------
    @operation_type.setter
    def operation_type(self, new_operation_type):
        logging.debug('Setting the transaction operation type: %d!', new_operation_type.value)
        self.__operation_type = new_operation_type

# Get class member "operation_id"
#----------------------------------------------------------------------------------------------------------------------
    @property
    def operation_id(self):
        logging.debug('Returning the transaction operation id: %d!', self.__operation_id)
        return self.__operation_id

# Set class member "operation_id"
#----------------------------------------------------------------------------------------------------------------------
    @operation_id.setter
    def operation_id(self, new_operation_id):
        logging.debug('Setting the transaction operation id: %d!', new_operation_id)
        self.__operation_id = new_operation_id

# Get total price of transaction
#----------------------------------------------------------------------------------------------------------------------
    def get_total_price(self):
        logging.debug('Returning the transaction total price')
        return self.__ammount * self.__price - self.__paid_fares

#----------------------------------------------------------------------------------------------------------------------
