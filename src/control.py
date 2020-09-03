#!/usr/bin/python3

import copy
import time
import logging
from PySide2 import QtCore
from include.cei import Cei
from datetime import date
from include.stock import Stock
from include.stock import StockTypes
from include.darf import DarfGenerator
from include.transaction import Transaction
from include.transaction import TransactionTypes
from dateutil.relativedelta import relativedelta

class Control(QtCore.QObject):

# Definition of Qt Signals
#----------------------------------------------------------------------------------------------------------------------
    update_cei_login_signal = QtCore.Signal(list, str)
    update_cei_import_stocks_signal = QtCore.Signal(str)
    update_cei_import_transactions_signal = QtCore.Signal(str)
    update_add_stock_signal = QtCore.Signal(str)
    update_add_transaction_signal = QtCore.Signal(str)
    update_stock_list_signal = QtCore.Signal(Stock)
    update_transaction_list_signal = QtCore.Signal(Transaction)
    update_stock_widget_signal = QtCore.Signal(Stock, bool, str)
    update_transaction_widget_signal = QtCore.Signal(Transaction, bool, str)
    update_purchase_values_signal = QtCore.Signal(float, float, float)
    update_sale_values_signal = QtCore.Signal(float, float, float)
    update_profit_values_signal = QtCore.Signal(float, float, float)
    update_accumulated_loss_values_signal = QtCore.Signal(float, float, float)
    update_due_tax_values_signal = QtCore.Signal(float, float, float, float)
    request_captcha_solution_signal = QtCore.Signal(bool)
    open_darf_file_signal = QtCore.Signal()

# Initialize the class with its properties
#----------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super().__init__()
        self.__cei = Cei()
        self.__stocks = []
        self.__stocks_after_process = []
        self.__transactions = []
        self.darf_generator = DarfGenerator()
        self.__darf_value = 0.0
        self.__total_purchase = {'normal': 0.0, 'day_trade': 0.0, 'fi': 0.0}
        self.__total_sale = {'normal': 0.0, 'day_trade': 0.0, 'fi': 0.0}
        self.__total_due_tax = {'normal': 0.0, 'day_trade': 0.0, 'fi': 0.0}
        self.__total_profit = {'normal': 0.0, 'day_trade': 0.0, 'fi': 0.0}
        self.__accumulated_loss = {'normal': 0.0, 'day_trade': 0.0, 'fi': 0.0}
        self.__accumulated_loss_after_process = {'normal': 0.0, 'day_trade': 0.0, 'fi': 0.0}
        self.__accumulated_darf = 0.0
        self.__accumulated_darf_after_process = 0.0
        self.__normal_no_tax_sale_value = 20000.00
        self.__normal_tax = 0.15
        self.__fi_tax = 0.20
        self.__day_trade_tax = 0.20
        self.__minimum_darf_value = 10.0
        self.__current_month_date = date.today()

# Add a new stock to the class
#----------------------------------------------------------------------------------------------------------------------
    def add_stock(self, name, price, category, ammount, paid_fares, custom_stock_list=None):
        logging.debug('Adding a new stock: %s', name)
        stock_list = custom_stock_list if custom_stock_list else self.__stocks
        if (self.find_stock(name, custom_stock_list) == -1):
            stock = Stock(name,price,category,ammount,paid_fares)
            stock_list.append(stock)
            return True
        else:
            logging.warning('Stock: %s already exists!', name)
            return False

# Edit a stock in the class
#----------------------------------------------------------------------------------------------------------------------
    def edit_stock(self, name, price, category, ammount, paid_fares, custom_stock_list=None):
        logging.debug('Editing the stock: %s', name)
        stock_list = custom_stock_list if custom_stock_list else self.__stocks
        stock_index = self.find_stock(name, custom_stock_list)
        if (stock_index != -1):
            stock_list[stock_index].price = price
            stock_list[stock_index].category = category
            stock_list[stock_index].ammount = ammount
            stock_list[stock_index].paid_fares = paid_fares
            return True
        else:
            logging.warning('Stock: %s does not exist!', name)
            return False

# Remove a stock in the class
#----------------------------------------------------------------------------------------------------------------------
    def remove_stock(self, name, custom_stock_list=None):
        logging.debug('Removing the stock: %s', name)
        stock_list = custom_stock_list if custom_stock_list else self.__stocks
        stock_index = self.find_stock(name, custom_stock_list)
        if (stock_index != -1):
            del stock_list[stock_index]
            return True
        else:
            logging.warning('Stock: %s does not exist!', name)
            return False

# Find an existing stock by name (return index if exists, else return -1)
#----------------------------------------------------------------------------------------------------------------------
    def find_stock(self, name, custom_stock_list=None):
        logging.debug('Finding if stock %s exists in the system', name)
        stock_list = custom_stock_list if custom_stock_list else self.__stocks
        for i in range (len(stock_list)):
            if stock_list[i].name == name:
                return i
        return -1

# Get stocks
#----------------------------------------------------------------------------------------------------------------------
    @property
    def stocks(self):
        logging.debug('Returning the registered stocks...')
        return self.__stocks

# Add a new transaction to the class
#----------------------------------------------------------------------------------------------------------------------
    def add_transaction(self, name, price, category, ammount, paid_fares, day, month, year,\
        operation_type, operation_id):
        logging.debug('Adding new transaction: %s : id: %d', name, operation_id)
        if (self.find_transaction(operation_id) == -1):
            transaction = Transaction(name,price,category,ammount,paid_fares,day,month,year,
            operation_type,operation_id)
            self.__transactions.append(transaction)
            return True
        else:
            logging.warning('Transaction: %d already exists!', operation_id)
            return False

# Edit a transaction in the class
#----------------------------------------------------------------------------------------------------------------------
    def edit_transaction(self, operation_id,name, price, category, ammount, paid_fares,\
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

# Get the last five months
#----------------------------------------------------------------------------------------------------------------------
    def __get_last_five_months(self):
        logging.debug('Returning the last five months...')
        last_five_months = []
        if (date.today().day >= 5):
            last_five_months.append(date.today() - relativedelta(day=1, months=1))
        for i in range(2, 6):
            last_five_months.append(date.today() - relativedelta(day=1, months=i))
        return last_five_months

# Calculate and return the second business day of the month in parameter
#----------------------------------------------------------------------------------------------------------------------
    def __second_business_day_date_of_month(self, month_date):
        logging.debug('Returning the second business day date of the month...')
        return_date = month_date
        if ((return_date.weekday() == 4) or (return_date.weekday() == 5)):
            return_date = date(return_date.year, return_date.month, 4)
        elif (return_date.weekday() == 6):
            return_date = date(return_date.year, return_date.month, 3)
        else:
            return_date = date(return_date.year, return_date.month, 2)
        return return_date

# Process transactions
#----------------------------------------------------------------------------------------------------------------------
    def __process_transactions(self):
        logging.debug('Processing the registered transactions...')
        self.__darf_value = 0.0
        self.__stocks_after_process = copy.deepcopy(self.__stocks)
        self.__accumulated_darf_after_process = copy.deepcopy(self.__accumulated_darf)
        self.__accumulated_loss_after_process = copy.deepcopy(self.__accumulated_loss)
        transactions = sorted(copy.deepcopy(self.__transactions), key=lambda x: (x.operation_date, x.operation_type.value))
        fi_transactions = []
        day_trade_transactions = []
        normal_transactions = []
        for i in range(len(transactions)):
            if transactions[i].category == StockTypes.FI:
                fi_transactions.append(copy.deepcopy(transactions[i]))
            elif transactions[i].category == StockTypes.NORMAL:
                j = i + 1
                while (j < len(transactions) and transactions[j].operation_date == transactions[i].operation_date \
                     and transactions[i].ammount != 0):
                    if (transactions[j].name == transactions[i].name):
                        if (transactions[j].operation_type == transactions[i].operation_type):
                            new_ammount = transactions[i].ammount + transactions[j].ammount
                            new_price = (transactions[i].price * transactions[i].ammount + \
                                transactions[j].price * transactions[j].ammount) / new_ammount
                            transactions[i].ammount = new_ammount
                            transactions[i].price = new_price
                            transactions[i].paid_fares += transactions[j].paid_fares
                            transactions[j].ammount = 0
                            transactions[j].price = 0.0
                            transactions[j].paid_fares = 0.0
                        else:
                            if (transactions[j].ammount < transactions[i].ammount):
                                new = copy.deepcopy(transactions[i])
                                new.ammount = transactions[j].ammount
                                new.paid_fares = (transactions[i].paid_fares / transactions[i].ammount) * new.ammount
                                transactions[j].category = StockTypes.DAY_TRADE
                                new.category = StockTypes.DAY_TRADE
                                day_trade_transactions.append(new)
                                day_trade_transactions.append(copy.deepcopy(transactions[j]))
                                transactions[i].paid_fares = transactions[i].paid_fares - new.paid_fares
                                transactions[i].ammount-=new.ammount
                                transactions[j].ammount = 0
                            else:
                                new = copy.deepcopy(transactions[j])
                                new.ammount = transactions[i].ammount
                                new.paid_fares = (transactions[j].paid_fares / transactions[j].ammount) * new.ammount
                                transactions[i].category = StockTypes.DAY_TRADE
                                new.category = StockTypes.DAY_TRADE
                                day_trade_transactions.append(new)
                                day_trade_transactions.append(copy.deepcopy(transactions[i]))
                                transactions[j].paid_fares = transactions[j].paid_fares - new.paid_fares
                                transactions[j].ammount-=new.ammount
                                transactions[i].ammount = 0
                    j+=1
                if (transactions[i].ammount != 0 and transactions[i].category != StockTypes.DAY_TRADE):
                    normal_transactions.append(copy.deepcopy(transactions[i]))
        if (not self.__process_fi_transactions(fi_transactions)):
            return False
        if (not self.__process_day_trade_transactions(day_trade_transactions)):
            return False
        if (not self.__process_normal_transactions(normal_transactions)):
            return False
        self.__darf_value = self.__total_due_tax['normal'] + self.__total_due_tax['day_trade'] + \
            self.__total_due_tax['fi'] + self.__accumulated_darf_after_process
        if (self.__darf_value < self.__minimum_darf_value):
            self.__accumulated_darf_after_process = self.__darf_value
        else:
            self.__accumulated_darf_after_process = 0.0
        return True

# Process fi transactions
#----------------------------------------------------------------------------------------------------------------------
    def __process_fi_transactions(self, transactions):
        logging.debug('Processing fi transactions')
        self.__total_purchase['fi'] = 0.0
        self.__total_sale['fi'] = 0.0
        self.__total_profit['fi'] = 0.0
        self.__total_due_tax['fi'] = 0.0
        for transaction in transactions:
            stock_index = self.find_stock(transaction.name, self.__stocks_after_process)
            if (transaction.operation_type == TransactionTypes.PURCHASE):
                self.__total_purchase['fi'] += transaction.price * transaction.ammount
                if (stock_index != -1):
                    stock = self.__stocks_after_process[stock_index]
                    stock_price = stock.price
                    stock_ammount = stock.ammount
                    new_ammount = stock_ammount + transaction.ammount
                    stock.price = (stock_price * stock_ammount + transaction.price * transaction.ammount) / new_ammount
                    stock.ammount = new_ammount
                    stock.paid_fares += transaction.paid_fares
                else:
                    new_stock = Stock(transaction.name, transaction.price, transaction.category, transaction.ammount,
                        transaction.paid_fares)
                    self.__stocks_after_process.append(new_stock)
            else:
                if (stock_index != -1):
                    stock = self.__stocks_after_process[stock_index]
                    self.__total_sale['fi'] += transaction.price * transaction.ammount
                    fares = (stock.paid_fares / stock.ammount) * transaction.ammount + transaction.paid_fares
                    profit = transaction.price * transaction.ammount - stock.price * transaction.ammount - fares
                    self.__total_profit['fi'] += profit
                    stock.ammount -= transaction.ammount
                    stock.paid_fares -= fares
                    if (stock.ammount < 0):
                        return False
                    elif (self.__stocks_after_process[stock_index].ammount == 0):
                        del self.__stocks_after_process[stock_index]
                else:
                    return False

        self.__total_profit['fi'] -= self.__accumulated_loss_after_process['fi']
        if self.__total_profit['fi'] > 0:
            self.__total_due_tax['fi'] = self.__fi_tax * self.__total_profit['fi']
            self.__accumulated_loss_after_process['fi'] = 0.0
        else:
            self.__accumulated_loss_after_process['fi'] = -1 * self.__total_profit['fi']
        return True

# Process day trade transactions
#----------------------------------------------------------------------------------------------------------------------
    def __process_day_trade_transactions(self, transactions):
        logging.debug('Processing day trade transactions')
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

        self.__total_profit['day_trade'] -= self.__accumulated_loss_after_process['day_trade']
        if self.__total_profit['day_trade'] > 0:
            self.__total_due_tax['day_trade'] = self.__day_trade_tax * self.__total_profit['day_trade']
            self.__accumulated_loss_after_process['day_trade'] = 0.0
        else:
            self.__accumulated_loss_after_process['day_trade'] = -1 * self.__total_profit['day_trade']
        return True

# Process normal transactions
#----------------------------------------------------------------------------------------------------------------------
    def __process_normal_transactions(self, transactions):
        logging.debug('Processing normal transactions')
        self.__total_purchase['normal'] = 0.0
        self.__total_sale['normal'] = 0.0
        self.__total_profit['normal'] = 0.0
        self.__total_due_tax['normal'] = 0.0
        for transaction in transactions:
            stock_index = self.find_stock(transaction.name, self.__stocks_after_process)
            if (transaction.operation_type == TransactionTypes.PURCHASE):
                self.__total_purchase['normal'] += transaction.price * transaction.ammount
                if (stock_index != -1):
                    stock = self.__stocks_after_process[stock_index]
                    stock_price = stock.price
                    stock_ammount = stock.ammount
                    new_ammount = stock_ammount + transaction.ammount
                    stock.price = (stock_price * stock_ammount + transaction.price * transaction.ammount) / new_ammount
                    stock.ammount = new_ammount
                    stock.paid_fares += transaction.paid_fares
                else:
                    new_stock = Stock(transaction.name, transaction.price, transaction.category, transaction.ammount,
                        transaction.paid_fares)
                    self.__stocks_after_process.append(new_stock)
            else:
                if (stock_index != -1):
                    stock = self.__stocks_after_process[stock_index]
                    self.__total_sale['normal'] += transaction.price * transaction.ammount
                    fares = (stock.paid_fares / stock.ammount) * transaction.ammount + transaction.paid_fares
                    profit = transaction.price * transaction.ammount - stock.price * transaction.ammount - fares
                    self.__total_profit['normal'] += profit
                    stock.ammount -= transaction.ammount
                    stock.paid_fares -= fares
                    if (stock.ammount < 0):
                        return False
                    elif (self.__stocks_after_process[stock_index].ammount == 0):
                        del self.__stocks_after_process[stock_index]
                else:
                    return False

        self.__total_profit['normal'] -=  self.__accumulated_loss_after_process['normal']
        if self.__total_profit['normal'] > 0:
            if (self.__total_sale['normal'] > self.__normal_no_tax_sale_value):
                self.__total_due_tax['normal'] = self.__normal_tax * self.__total_profit['normal']
        else:
            self.__accumulated_loss_after_process['normal'] = -1 * self.__total_profit['normal']
        return True

# Save operations
#----------------------------------------------------------------------------------------------------------------------
    def save_operations(self):
        logging.debug('Saving the registered operations...')
        self.__stocks = copy.deepcopy(self.__stocks_after_process)
        self.__accumulated_loss = copy.deepcopy(self.__accumulated_loss_after_process)
        self.__accumulated_darf = copy.deepcopy(self.__accumulated_darf_after_process)
        # save the operations in the database
        # self.__stocks = copy.deepcopy(self.__evaluated_stocks)
        # self.__accumulated_loss = copy.deepcopy(self.__accumulated_loss_evaluated)
        # self.__accumulated_darf = copy.deepcopy(self.__accumulated_darf_evaluated)

# Load operations
#----------------------------------------------------------------------------------------------------------------------
    def load_operations(self):
        logging.debug('Loading the saved operations...')
        # Load the operations from the database
        # self.__stocks = copy.deepcopy(self.__evaluated_stocks)
        # self.__accumulated_loss = copy.deepcopy(self.__accumulated_loss_evaluated)
        # self.__accumulated_darf = copy.deepcopy(self.__accumulated_darf_evaluated)

# Get total purchase of fi stocks
#----------------------------------------------------------------------------------------------------------------------
    def get_total_purchase_of_fi_stocks(self):
        logging.debug('Returning the total purchase of fi stocks...')
        return self.__total_purchase['fi']

# Get total purchase of day trade stocks
#----------------------------------------------------------------------------------------------------------------------
    def get_total_purchase_of_day_trade_stocks(self):
        logging.debug('Returning the total purchase of day trade stocks...')
        return self.__total_purchase['day_trade']

# Get total purchase of normal stocks
#----------------------------------------------------------------------------------------------------------------------
    def get_total_purchase_of_normal_stocks(self):
        logging.debug('Returning the total purchase of normal stocks...')
        return self.__total_purchase['normal']

# Get total sale of fi stocks
#----------------------------------------------------------------------------------------------------------------------
    def get_total_sale_of_fi_stocks(self):
        logging.debug('Returning the total sale of fi stocks...')
        return self.__total_sale['fi']

# Get total sale of day trade stocks
#----------------------------------------------------------------------------------------------------------------------
    def get_total_sale_of_day_trade_stocks(self):
        logging.debug('Returning the total sale of day trade stocks...')
        return self.__total_sale['day_trade']

# Get total sale of normal stocks
#----------------------------------------------------------------------------------------------------------------------
    def get_total_sale_of_normal_stocks(self):
        logging.debug('Returning the total sale of normal stocks...')
        return self.__total_sale['normal']

# Get total profit of fi stocks
#----------------------------------------------------------------------------------------------------------------------
    def get_total_profit_of_fi_stocks(self):
        logging.debug('Returning the total profit of fi stocks...')
        return self.__total_profit['fi']

# Get total profit of day trade stocks
#----------------------------------------------------------------------------------------------------------------------
    def get_total_profit_of_day_trade_stocks(self):
        logging.debug('Returning the total profit of day trade stocks...')
        return self.__total_profit['day_trade']

# Get total profit of normal stocks
#----------------------------------------------------------------------------------------------------------------------
    def get_total_profit_of_normal_stocks(self):
        logging.debug('Returning the total profit of normal stocks...')
        return self.__total_profit['normal']

# Get total due tax of fi stocks
#----------------------------------------------------------------------------------------------------------------------
    def get_total_due_tax_of_fi_stocks(self):
        logging.debug('Returning the total due tax of fi stocks...')
        return self.__total_due_tax['fi']

# Get total due tax of day trade stocks
#----------------------------------------------------------------------------------------------------------------------
    def get_total_due_tax_of_day_trade_stocks(self):
        logging.debug('Returning the total due tax of day trade stocks...')
        return self.__total_due_tax['day_trade']

# Get total due tax of normal stocks
#----------------------------------------------------------------------------------------------------------------------
    def get_total_due_tax_of_normal_stocks(self):
        logging.debug('Returning the total due tax of normal stocks...')
        return self.__total_due_tax['normal']

# Get darf value
#----------------------------------------------------------------------------------------------------------------------
    @property
    def darf_value(self):
        logging.debug('Returning the darf value %f...', self.__darf_value)
        return self.__darf_value

# Calculate darf
#----------------------------------------------------------------------------------------------------------------------
    def calculate_darf(self):
        logging.debug('Calculating the darf')
        if (self.__process_transactions()):
            logging.debug('Darf calculated!')
            return True
        else:
            logging.error('Error calculating the darf!')
            return False

# Update all the calculated values on the gui sending signals to it
#----------------------------------------------------------------------------------------------------------------------
    def update_values_on_gui(self):
        logging.debug('Send signals to update the calculated values on the gui')
        self.update_purchase_values_signal.emit(self.get_total_purchase_of_normal_stocks(),\
            self.get_total_purchase_of_day_trade_stocks(), self.get_total_purchase_of_fi_stocks())
        self.update_sale_values_signal.emit(self.get_total_sale_of_normal_stocks(),\
            self.get_total_sale_of_day_trade_stocks(), self.get_total_sale_of_fi_stocks())
        self.update_profit_values_signal.emit(self.get_total_profit_of_normal_stocks(),\
            self.get_total_profit_of_day_trade_stocks(), self.get_total_profit_of_fi_stocks())
        self.update_accumulated_loss_values_signal.emit(self.__accumulated_loss_after_process['normal'],\
            self.__accumulated_loss_after_process['day_trade'], self.__accumulated_loss_after_process['fi'])
        self.update_due_tax_values_signal.emit(self.get_total_due_tax_of_normal_stocks(),\
            self.get_total_due_tax_of_day_trade_stocks(), self.get_total_due_tax_of_fi_stocks(), self.darf_value)

# SLOT - Fires when receive a cei login signal from the gui
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot(str,str)
    def cei_login_slot(self, cpf, password):
        try:
            self.__cei.login(cpf, password)
            self.update_cei_login_signal.emit(self.__get_last_five_months(), '')
        except:
            self.update_cei_login_signal.emit(self.__get_last_five_months(), 'Falha ao acessar o CEI')

# SLOT - Fires when receive a cei import stocks signal from the gui
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot(date)
    def cei_import_stocks_slot(self, import_date):
        try:
            report = self.__cei.get_wallet(self.__second_business_day_date_of_month(import_date))
            for account in report:
                for stock in account['extract']:
                    category = StockTypes.FI if stock['code'][4:6] == '11' else StockTypes.NORMAL
                    new_stock = Stock(stock['code'][0:4], stock['price'], category, stock['quantity'], 0.0)
                    self.add_stock_slot(new_stock)
            self.__current_month_date = import_date
            self.update_cei_import_stocks_signal.emit('')
        except:
            self.update_cei_import_stocks_signal.emit('Falha ao importar carteira de ativos do CEI')

# SLOT - Fires when receive a cei import transactions signal from the gui
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot(date)
    def cei_import_transactions_slot(self, import_date):
        try:
            date_begin = import_date
            date_end = date_begin + relativedelta(months=1) - relativedelta(day=1, days=1)
            report = self.__cei.get_extract(date_begin, date_end)
            oper_id = 1
            for account in report:
                for transaction in account['extract']:
                    category = StockTypes.FI if transaction['code'][4:6] == '11' else StockTypes.NORMAL
                    oper = TransactionTypes.PURCHASE if transaction['operation'] == 'C' else TransactionTypes.SALE
                    day = int(transaction['date'][0:2])
                    month = int(transaction['date'][3:5])
                    year = int(transaction['date'][6:10])
                    new_transaction = Transaction(transaction['code'][0:4], transaction['price'], category,
                        transaction['quantity'], 0.0, day, month, year, oper, oper_id)
                    self.add_transaction_slot(new_transaction)
                    oper_id = oper_id + 1
            self.__current_month_date = import_date
            self.update_cei_import_transactions_signal.emit('')
        except:
            self.update_cei_import_transactions_signal.emit('Falha ao importar transações do CEI')

# SLOT - Fires when receive an add stock signal from the gui
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot(Stock)
    def add_stock_slot(self, new_stock):
        error_message = ""
        if new_stock.name == "":
            error_message = "Erro! Nome da ação inválido"
        elif new_stock.ammount == 0:
            error_message = "Erro! Quantidade não pode ser 0"
        else:
            if not self.add_stock(new_stock.name, new_stock.price, new_stock.category,\
                new_stock.ammount, new_stock.paid_fares):
                error_message = "Erro! Ação já existe!"
            else:
                self.update_stock_list_signal.emit(new_stock)
        self.update_add_stock_signal.emit(error_message)
        self.calculate_darf()
        self.update_values_on_gui()

# SLOT - Fires when receive an edit stock signal from the gui
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot(Stock)
    def edit_stock_slot(self, new_stock):
        error_message = ""
        remove_widget = False
        if new_stock.name == "":
            error_message = "Erro! Nome da ação inválido"
        elif new_stock.ammount == 0:
            if not self.remove_stock(new_stock.name):
                error_message = "Erro! Ação não existe!"
            else:
                remove_widget = True
        else:
            if not self.edit_stock(new_stock.name, new_stock.price, new_stock.category,\
                new_stock.ammount, new_stock.paid_fares):
                error_message = "Erro! Ação não existe!"
        self.update_stock_widget_signal.emit(new_stock, remove_widget, error_message)
        self.calculate_darf()
        self.update_values_on_gui()

# SLOT - Fires when receive an add transaction signal from the gui
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot(Transaction)
    def add_transaction_slot(self, new_transaction):
        error_message = ""
        if new_transaction.name == "":
            error_message = "Erro! Nome da ação da transação inválido"
        elif new_transaction.ammount == 0:
            error_message = "Erro! Quantidade não pode ser 0"
        else:
            if not self.add_transaction(new_transaction.name, new_transaction.price, new_transaction.category,\
                new_transaction.ammount, new_transaction.paid_fares, new_transaction.operation_date.day,\
                new_transaction.operation_date.month, new_transaction.operation_date.year,\
                new_transaction.operation_type, new_transaction.operation_id):
                error_message = "Erro! Id da transação já existe!"
            else:
                self.update_transaction_list_signal.emit(new_transaction)
        self.update_add_transaction_signal.emit(error_message)
        self.calculate_darf()
        self.update_values_on_gui()

# SLOT - Fires when receive an edit transaction signal from the gui
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot(Transaction)
    def edit_transaction_slot(self, new_transaction):
        error_message = ""
        remove_widget = False
        if new_transaction.name == "":
            error_message = "Erro! Nome da ação da transação inválido"
        elif new_transaction.ammount == 0:
            if not self.remove_transaction(new_transaction.operation_id):
                error_message = "Erro! Transação não existe!"
            else:
                remove_widget = True
        else:
            if not self.edit_transaction(new_transaction.operation_id, new_transaction.name, new_transaction.price,\
                new_transaction.category, new_transaction.ammount, new_transaction.paid_fares,\
                new_transaction.operation_date.day,new_transaction.operation_date.month,\
                new_transaction.operation_date.year, new_transaction.operation_type):
                error_message = "Erro! Transação não existe!"
        self.update_transaction_widget_signal.emit(new_transaction, remove_widget, error_message)
        self.calculate_darf()
        self.update_values_on_gui()

# SLOT - Fires when receive an start darf generation signal from the gui
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot(str,str,str,float)
    def start_darf_generation_slot(self, cpf, state, city, darf_value):
        darf_date = self.__current_month_date
        self.darf_generator.start_darf_generation(cpf, state, city, darf_date, darf_value)
        self.darf_generator.download_captcha()
        self.request_captcha_solution_signal.emit(False)

# SLOT - Fires when receive an captcha solution signal from the gui
#----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot(str)
    def captcha_solution_slot(self, captcha_answer):
        self.darf_generator.solve_captcha(captcha_answer)
        if (not self.darf_generator.captcha_solved()):
            time.sleep(2)
            self.darf_generator.download_captcha()
            self.request_captcha_solution_signal.emit(True)
        else:
            self.darf_generator.save_darf()
            self.darf_generator.finish_generation()
            self.open_darf_file_signal.emit()
#----------------------------------------------------------------------------------------------------------------------
