#!/usr/bin/python3

from stock import StockTypes
from stock import SoldStock
import logging

class Control:

# Initialize the class with its properties
#----------------------------------------------------------------------------------------------------------------------
    def __init__(self, debug=False):
        self.__stocks = []
        self.__darf_value = 0.0
        self.__accumulated_loss = {'normal': 0.0, 'day_trade': 0.0, 'fi': 0.0}
        self.__accumulated_darf = 0.0
        self.__debug = debug

# Add a new stock to the class
#----------------------------------------------------------------------------------------------------------------------
    def add_stock(self, name, buy_day, buy_month, buy_year, sell_day, sell_month, sell_year, ammount_sold,
        average_price, sell_price, type, paid_fares):
        logging.debug('Adding new stock: %s', name)
        stock = SoldStock()
        stock.name = name
        stock.average_price = average_price
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

# Get darf value
#----------------------------------------------------------------------------------------------------------------------
    @property
    def darf_value(self):
        logging.debug('Returning the darf value %f...', self.__darf_value)
        return self.__darf_value

# Get total sell value of normal stocks
#----------------------------------------------------------------------------------------------------------------------
    def get_total_sell_value_of_normal_stocks(self):
        logging.debug('Returning the total sell value of normal stocks...')
        total = 0.0
        for stock in self.__stocks:
            total += stock.total_sold
        return total

# Calculate darf
#----------------------------------------------------------------------------------------------------------------------
    def calculate_darf(self):
        logging.debug('Calculating the darfs...')
        total_normal = self.__accumulated_loss['normal']
        total_day_trade = self.__accumulated_loss['day_trade']
        total_fi = self.__accumulated_loss['fi']
        normal_free_tax_sell = 20000.00
        minimum_darf_value = 10.0
        self.__darf_value = 0.0

        for stock in self.__stocks:
            if stock.type == StockTypes.DAY_TRADE:
                total_day_trade += stock.calculate_due_taxes_or_loss()
            elif stock.type == StockTypes.FI:
                total_fi += stock.calculate_due_taxes_or_loss()
            elif stock.type == StockTypes.NORMAL:
                total_normal += stock.calculate_due_taxes_or_loss()

        #Day trade operations with positive profit
        if total_day_trade > 0.0:
            self.__darf_value += total_day_trade
            self.__accumulated_loss['day_trade'] = 0.0
        #Day trade operations with negative profit
        else:
            self.__accumulated_loss['day_trade'] = total_day_trade

        #Normal operations with positive profit
        if self.get_total_sell_value_of_normal_stocks() > normal_free_tax_sell:
            if total_normal > 0.0:
                self.__darf_value += total_normal
                self.__accumulated_loss['normal'] = 0.0
        #Normal operations with negative profit
        if total_normal < 0.0:
                self.__accumulated_loss['normal'] = total_normal

        #fi operations with positive profit
        if total_fi > 0.0:
            self.__darf_value += total_fi
            self.__accumulated_loss['fi'] = 0.0
        #fi operations with negative profit
        else:
            self.__accumulated_loss['fi'] = total_fi

        #add accumulated darf and check if darf has to accumulate
        self.__darf_value += self.__accumulated_darf
        if self.__darf_value >= minimum_darf_value:
            self.__accumulated_darf = 0.0
        else:
            logging.debug('Darf %d is not greater than minimum %f...', self.__darf_value, minimum_darf_value)
            self.__accumulated_darf = self.__darf_value
            self.__darf_value = 0.0

# Set log level
#----------------------------------------------------------------------------------------------------------------------
    def set_log_level(self, debug):
        if (debug):
            logging.basicConfig(level=1)
            logging.debug('Log debug level activated!')
        else:
            logging.basicConfig(level=logging.INFO)

#----------------------------------------------------------------------------------------------------------------------
