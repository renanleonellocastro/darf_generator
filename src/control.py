#!/usr/bin/python3

import copy
import logging
from stock import Stock
from stock import StockTypes
from transaction import Transaction
from transaction import TransactionTypes

class Control:

# Initialize the class with its properties
#----------------------------------------------------------------------------------------------------------------------
    def __init__(self, debug=False):
        self.__stocks = []
        self.__evaluated_stocks = self.__stocks
        self.__transactions = []
        self.__darf_value = 0.0
        self.__total_purchase = {'normal': 0.0, 'day_trade': 0.0, 'fi': 0.0}
        self.__total_sale = {'normal': 0.0, 'day_trade': 0.0, 'fi': 0.0}
        self.__total_due_tax = {'normal': 0.0, 'day_trade': 0.0, 'fi': 0.0}
        self.__total_profit = {'normal': 0.0, 'day_trade': 0.0, 'fi': 0.0}
        self.__accumulated_loss = {'normal': 0.0, 'day_trade': 0.0, 'fi': 0.0}
        self.__accumulated_loss_evaluated = self.__accumulated_loss
        self.__accumulated_darf = 0.0
        self.__accumulated_darf_evaluated = self.__accumulated_darf
        self.__normal_no_tax_sale_ammount = 20000.00
        self.__normal_tax = 0.15
        self.__fi_tax = 0.20
        self.__day_trade_tax = 0.20
        self.__minimum_darf_value = 10.0
        self.__debug = debug

# Get class member "month"
#----------------------------------------------------------------------------------------------------------------------
    @property
    def month(self):
        logging.debug('Returning the month: %d!', self.__month)
        return self.__month

# Set class member "month"
#----------------------------------------------------------------------------------------------------------------------
    @month.setter
    def month(self, new_month):
        logging.debug('Setting the month: %d!', new_month)
        if new_month > 12 or new_month < 1:
            logging.error('Month does not exist!')
        else:
            self.__month = new_month

# Add a new stock to the class
#----------------------------------------------------------------------------------------------------------------------
    def add_stock(self, name, price, category, ammount, paid_fares):
        logging.debug('Adding a new stock: %s', name)
        if (self.find_stock(name) == -1):
            stock = Stock(name,price,category,ammount,paid_fares,self.__debug)
            self.__stocks.append(stock)
            return True
        else:
            logging.warning('Stock: %s already exists!', name)
            return False

# Edit a stock in the class
#----------------------------------------------------------------------------------------------------------------------
    def edit_stock(self, name, price, category, ammount, paid_fares):
        logging.debug('Editing the stock: %s', name)
        stock_index = self.find_stock(name)
        if (stock_index != -1):
            self.__stocks[stock_index].price = price
            self.__stocks[stock_index].category = category
            self.__stocks[stock_index].ammount = ammount
            self.__stocks[stock_index].paid_fares = paid_fares
            return True
        else:
            logging.warning('Stock: %s does not exist!', name)
            return False

# Remove a stock in the class
#----------------------------------------------------------------------------------------------------------------------
    def remove_stock(self, name):
        logging.debug('Removing the stock: %s', name)
        stock_index = self.find_stock(name)
        if (stock_index != -1):
            del self.__stocks[stock_index]
            return True
        else:
            logging.warning('Stock: %s does not exist!', name)
            return False

# Find an existing stock by name (return index if exists, else return -1)
#----------------------------------------------------------------------------------------------------------------------
    def find_stock(self, name):
        logging.debug('Finding if stock %s exists in the system', name)
        for i in range (len(self.__stocks)):
            if self.__stocks[i].name == name:
                return i
        return -1

# Remove all stocks that has zero as ammount number in the class
#----------------------------------------------------------------------------------------------------------------------
    def remove_all_zero_ammount_stocks(self, name):
        logging.debug('Removing the zero ammount stocks')
        for i in range(len(self.__stocks)):
            if self.__stocks[i].ammount == 0:
                del self.__stocks[i]

# Get stocks
#----------------------------------------------------------------------------------------------------------------------
    @property
    def stocks(self):
        logging.debug('Returning the registered stocks...')
        return self.__stocks

# Add a new transaction to the class
#----------------------------------------------------------------------------------------------------------------------
    def add_transaction(self, name, price, category, ammount, paid_fares, day, month, year,
        operation_type, operation_id):
        logging.debug('Adding new transaction: %s : id: %d', name, operation_id)
        transaction = Transaction(name,price,category,ammount,paid_fares,day,month,year,
            operation_type,operation_id,self.__debug)
        self.__transactions.append(transaction)

# Edit a transaction in the class
#----------------------------------------------------------------------------------------------------------------------
    def edit_transaction(self, operation_id,name, price, category, ammount, paid_fares,
        day, month, year, operation_type):
        logging.debug('Editing the transaction: %d', operation_id)
        transaction_index = self.find_transaction(operation_id)
        if (transaction_index != -1):
            self.__transactions[transaction_index].name = name
            self.__transactions[transaction_index].price = price
            self.__transactions[transaction_index].category = category
            self.__transactions[transaction_index].ammount = ammount
            self.__transactions[transaction_index].paid_fares = paid_fares
            self.__transactions[transaction_index].set_operation_date(year,month,day)
            self.__transactions[transaction_index].operation_type = operation_type
            return True
        else:
            logging.warning('Transaction: %d does not exist!', operation_id)
            return False

# Remove a transaction in the class
#----------------------------------------------------------------------------------------------------------------------
    def remove_transaction(self, operation_id):
        logging.debug('Removing the transaction: %d', operation_id)
        transaction_index = self.find_transaction(operation_id)
        if (transaction_index != -1):
            del self.__transactions[transaction_index]
            return True
        else:
            logging.warning('Stock: %d does not exist!', operation_id)
            return False

# Find an existing transaction by id (return index if exists, else return -1)
#----------------------------------------------------------------------------------------------------------------------
    def find_transaction(self, operation_id):
        logging.debug('Finding if transaction %d exists in the system', operation_id)
        for i in range (len(self.__transactions)):
            if self.__transactions[i].operation_id == operation_id:
                return i
        return -1

# Get transactions
#----------------------------------------------------------------------------------------------------------------------
    @property
    def transactions(self):
        logging.debug('Returning the registered transactions...')
        return self.__transactions

# Process transactions
#----------------------------------------------------------------------------------------------------------------------
    def process_transactions(self):
        logging.debug('Processing the registered transactions...')
        self.__evaluated_stocks = self.__stocks
        self.__accumulated_darf_evaluated = self.__accumulated_darf
        self.__darf_value = 0.0
        transactions = sorted(self.__transactions, key=lambda x: (x.operation_date, x.operation_type))
        fi_transactions = []
        day_trade_transactions = []
        normal_transactions = []
        for i in range(len(transactions)):
            if transactions[i].category == StockTypes.FI:
                fi_transactions.append(copy.copy(transactions[i]))
            elif transactions[i].category == StockTypes.NORMAL:
                j = i + 1
                while (transactions[j].operation_date == transactions[i].operation_date and
                    transactions[i].ammount != 0):
                    if (transactions[j].name == transactions[i].name):
                        if (transactions[j].operation_type == transactions[i].operation_type):
                            new_ammount = transactions[i].ammount + transactions[j].ammount
                            new_price = (transactions[i].price * transactions[i].ammount +
                                transactions[j].price * transactions[j].ammount) / new_ammount
                            transactions[i].ammount = new_ammount
                            transactions[i].price = new_price
                            transactions[i].paid_fares += transactions[j].paid_fares
                            transactions[j].ammount = 0
                            transactions[j].price = 0.0
                            transactions[j].paid_fares = 0.0
                        else:
                            if (transactions[j].ammount < transactions[i].ammount):
                                Transaction new = copy.copy(transactions[i])
                                new.ammount = transactions[j].ammount
                                new.paid_fares = (transactions[i].paid_fares / transactions[i].ammount) * new.ammount
                                transactions[j].category = StockTypes.DAY_TRADE
                                new.category = StockTypes.DAY_TRADE
                                day_trade_transactions.append(new)
                                day_trade_transactions.append(copy.copy(transactions[j]))
                                transactions[i].paid_fares = transactions[i].paid_fares - new.paid_fares
                                transactions[i].ammount-=new.ammount
                                transactions[j].ammount = 0
                            else:
                                Transaction new = copy.copy(transactions[j])
                                new.ammount = transactions[i].ammount
                                new.paid_fares = (transactions[j].paid_fares / transactions[j].ammount) * new.ammount
                                transactions[i].category = StockTypes.DAY_TRADE
                                new.category = StockTypes.DAY_TRADE
                                day_trade_transactions.append(new)
                                day_trade_transactions.append(copy.copy(transactions[i]))
                                transactions[j].paid_fares = transactions[j].paid_fares - new.paid_fares
                                transactions[j].ammount-=new.ammount
                                transactions[i].ammount = 0
                    j+=1
                if (transactions[i].ammount != 0 and transactions[i].category != StockTypes.DAY_TRADE):
                    normal_transactions.append(copy.copy(transactions[i]))
        self.__process_fi_transactions(fi_transactions)
        self.__process_day_trade_transactions(day_trade_transactions)
        self.__process_normal_transactions(normal_transactions)
        self.__total_due_tax = {'normal': 0.0, 'day_trade': 0.0, 'fi': 0.0}
        self.__darf_value = self.__total_due_tax['normal'] + self.__total_due_tax['day_trade'] + \
            self.__total_due_tax['fi']

# Process fi transactions
#----------------------------------------------------------------------------------------------------------------------
    def __process_fi_transactions(self, transactions):
        logging.debug('Processing fi transactions')
        self.__accumulated_loss_evaluated['fi'] = self.__accumulated_loss['fi']
        self.__total_purchase['fi'] = 0.0
        self.__total_sale['fi'] = 0.0
        self.__total_profit['fi'] = 0.0
        self.__total_due_tax['fi'] = 0.0
        for transaction in transactions:
            stock_index = self.find_stock(transaction.name)
            stock = self.__evaluated_stocks[stock_index]
            if (transaction.operation_type == TransactionTypes.PURCHASE):
                self.__total_purchase['fi'] += transaction.price * transaction.ammount
                if (stock_index != -1):
                    stock_price = stock.price
                    stock_ammount = stock.ammount
                    stock_fares = stock.paid_fares
                    new_ammount = stock_ammount + transaction.ammount
                    stock.price = (stock_price * stock_ammount + transaction.price * transaction.ammount) / new_ammount
                    stock.ammount = new_ammount
                    stock.paid_fares += transaction.paid_fares
                else:
                    stock = Stock(transaction.name, transaction.price, transaction.category, transaction.ammount,
                        transaction.paid_fares)
                    self.__evaluated_stocks.append(stock)
            else:
                if (stock_index != -1):
                    self.__total_sale['fi'] += transaction.price * transaction.ammount
                    fares = (stock.paid_fares / stock.ammount) * transaction.ammount + transaction.paid_fares
                    profit = transaction.price * transaction.ammount - stock.price * transaction.ammount - fares
                    self.__total_profit['fi'] += profit
                    stock.ammount -= transaction.ammount
                    stock.paid_fares -= fares
                    if (stock.ammount < 0):
                        return False
                    elif (self.__evaluated_stocks[stock_index].ammount == 0):
                        del self.__evaluated_stocks[stock_index]
                else:
                    return False
        if (self.__total_profit['fi'] - self.__accumulated_loss_evaluated['fi']) > 0:
            self.__total_due_tax['fi'] = self.__fi_tax * self.__total_profit['fi']
        else:
            self.__accumulated_loss_evaluated['fi'] = self.__accumulated_loss_evaluated['fi'] \
                - self.__total_profit['fi']
        return True

# Process day trade transactions
#----------------------------------------------------------------------------------------------------------------------
    def __process_day_trade_transactions(self, transactions):
        logging.debug('Processing day trade transactions')
        self.__accumulated_loss_evaluated['day_trade'] = self.__accumulated_loss['day_trade']
        self.__total_purchase['day_trade'] = 0.0
        self.__total_sale['day_trade'] = 0.0
        self.__total_profit['day_trade'] = 0.0
        self.__total_due_tax['day_trade'] = 0.0
        for i in range(len(transactions)):
            transaction = transactions[i]
            if (transaction.ammount != 0):
                if (transaction.operation_type == TransactionTypes.PURCHASE):
                    purchase = transaction.price * transaction.ammount
                    sale = transactions[i+1].price * transactions[i+1].ammount
                else:
                    sale = transaction.price * transaction.ammount
                    purchase = transactions[i+1].price * transactions[i+1].ammount

                fares = transaction.paid_fares + transactions[i+1].paid_fares
                profit = sale - purchase - fares
                self.__total_purchase['day_trade'] += purchase
                self.__total_sale['day_trade'] += sale
                self.__total_profit['day_trade'] += profit
                transaction.ammount = 0
                transactions[i+1].ammount = 0

        if (self.__total_profit['day_trade'] - self.__accumulated_loss_evaluated['day_trade']) > 0:
            self.__total_due_tax['day_trade'] = self.__day_trade_tax * self.__total_profit['day_trade']
        else:
            self.__accumulated_loss_evaluated['day_trade'] = self.__accumulated_loss_evaluated['day_trade'] \
                - self.__total_profit['day_trade']
        return True

# Evaluate transactions
#----------------------------------------------------------------------------------------------------------------------
    def evaluate_transactions(self):
        logging.debug('Evaluating the registered transactions...')
        self.__stocks = self.__evaluated_stocks
        self.__accumulated_loss = self.__accumulated_loss_evaluated
        self.__accumulated_darf = self.__accumulated_darf_evaluated

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
