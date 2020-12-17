#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import pyquery
from datetime import date
from automatedweb import AutomatedWeb
from locale import atof, setlocale, LC_NUMERIC

class Cei():

#Definition of Class Constants
#----------------------------------------------------------------------------------------------------------------------
    __login_endpoint = "https://ceiapp.b3.com.br/CEI_Responsivo/login.aspx"
    __wallet_endpoint = "https://ceiapp.b3.com.br/CEI_Responsivo/ConsultarCarteiraAtivos.aspx"
    __stocks_extract_endpoint = "https://ceiapp.b3.com.br/CEI_Responsivo/negociacao-de-ativos.aspx"
    __login_data = {"ctl00$ContentPlaceHolder1$smLoad":\
                    "ctl00$ContentPlaceHolder1$UpdatePanel1|ctl00$ContentPlaceHolder1$btnLogar",
                    "__EVENTTARGET": "", "__EVENTARGUMENT": "", "ctl00$ContentPlaceHolder1$txtLogin": "",
                    "ctl00$ContentPlaceHolder1$txtSenha": "", "__VIEWSTATEGENERATOR": "", "_ASYNCPOST": True,
                    "__EVENTVALIDATION": "", "__VIEWSTATE": "", "ctl00$ContentPlaceHolder1$btnLogar": "Entrar"}
    __wallet_data = {"ctl00$ContentPlaceHolder1$ToolkitScriptManager1":\
                    "ctl00$ContentPlaceHolder1$updFiltro|ctl00$ContentPlaceHolder1$ddlAgentes",
		            "ctl00_ContentPlaceHolder1_ToolkitScriptManager1_HiddenField": "", "__ASYNCPOST": True,
		            "__EVENTTARGET": "ctl00$ContentPlaceHolder1$ddlAgentes", "__EVENTARGUMENT": "", "__LASTFOCUS": "",
		            "__VIEWSTATEGENERATOR": "", "__EVENTVALIDATION": "", "__VIEWSTATE": "",
                    "ctl00$ContentPlaceHolder1$txtData": "", "ctl00$ContentPlaceHolder1$ddlContas": "0",
                    "ctl00$ContentPlaceHolder1$ddlAgentes": ""}
    __extract_data = {"ctl00$ContentPlaceHolder1$ToolkitScriptManager1":\
                    "ctl00$ContentPlaceHolder1$updFiltro|ctl00$ContentPlaceHolder1$ddlAgentes",
		            "ctl00_ContentPlaceHolder1_ToolkitScriptManager1_HiddenField": "", "__ASYNCPOST": True,
		            "__EVENTTARGET": "ctl00$ContentPlaceHolder1$ddlAgentes", "__EVENTARGUMENT": "", "__LASTFOCUS": "",
		            "ctl00$ContentPlaceHolder1$hdnPDF_EXCEL": "", "__VIEWSTATEGENERATOR": "", "__EVENTVALIDATION": "",
		            "__VIEWSTATE": "", "ctl00$ContentPlaceHolder1$txtDataDeBolsa": "",
		            "ctl00$ContentPlaceHolder1$txtDataAteBolsa": "", "ctl00$ContentPlaceHolder1$ddlContas": "0",
                    "ctl00$ContentPlaceHolder1$ddlAgentes": ""}

# Initialize the class with its properties
#----------------------------------------------------------------------------------------------------------------------
    def __init__(self, debug=False):
        self.__web = AutomatedWeb(debug=debug)
        self.__debug = debug
        self.__logged_in = False
        logging.debug('Cei constructor ended!')

# Evaluate the user login in the cei b3 system
#----------------------------------------------------------------------------------------------------------------------
    def login(self, cpf, password):
        logging.debug('Trying to log in the user %s in Cei...', cpf)

        if self.__logged_in:
            logging.warning('Another user is already logged in!')
            raise RuntimeError('Another user is already logged in!')

        try:
            self.__web.executeGet(self.__login_endpoint)
            self.__login_data["__VIEWSTATE"] = self.__web.getValueFromPage('#__VIEWSTATE')
            self.__login_data["__VIEWSTATEGENERATOR"] = self.__web.getValueFromPage('#__VIEWSTATEGENERATOR')
            self.__login_data["__EVENTVALIDATION"] = self.__web.getValueFromPage('#__EVENTVALIDATION')
            self.__login_data["ctl00$ContentPlaceHolder1$txtLogin"] = cpf
            self.__login_data["ctl00$ContentPlaceHolder1$txtSenha"] = password
            self.__web.executePost(self.__login_endpoint, self.__login_data)

            if self.__web.getValueFromPage('#ctl00_ContentPlaceHolder1_btnLogar') != None:
                raise RuntimeError('')

            self.__logged_in = True
            logging.debug('User %s logged in!', cpf)

        except:
            logging.error('User %s failed to log in!', cpf)
            raise RuntimeError('User %s failed to log in!' %cpf)

# Get the user wallet of purchased stocks and fis
#----------------------------------------------------------------------------------------------------------------------
    def get_wallet(self, search_date):
        wallet_date = ("%02d/%02d/%04d" %(search_date.day, search_date.month, search_date.year))
        logging.debug('Getting the wallet in %s in Cei...', wallet_date)
        stocks = []
        stock = {}

        if not self.__logged_in:
            logging.error('User not logged in!')
            raise RuntimeError('User not logged in!')

        try:
            self.__web.executeGet(self.__wallet_endpoint)
            institutions = self.__web.getOptionsValuesFromSelection('ctl00_ContentPlaceHolder1_ddlAgentes')
            institutions.remove('0')

            for institution in institutions:
                stock['institution'] = institution
                accounts = self.__get_accounts_from_institution_in_wallet_page(institution, wallet_date)

                for account in accounts:
                    stock['account'] = account
                    stock['extract'] = \
                        self.__get_stocks_from_account_and_date_in_wallet_page(institution, account, wallet_date)
                    stocks.append(stock)

            return stocks

        except:
            logging.error('Failed to get the user wallet!')
            raise RuntimeError('Failed to get the user wallet!')

# Get the user extract of purchased and sold stocks and fis
#----------------------------------------------------------------------------------------------------------------------
    def get_extract(self, date_begin, date_end):
        start_date = ("%02d/%02d/%04d" %(date_begin.day, date_begin.month, date_begin.year))
        end_date = ("%02d/%02d/%04d" %(date_end.day, date_end.month, date_end.year))
        logging.debug('Getting the extract from %s to %s in Cei...', start_date, end_date)
        transactions = []
        transaction = {}

        if not self.__logged_in:
            logging.error('User not logged in!')
            raise RuntimeError('User not logged in!')

        try:
            self.__web.executeGet(self.__stocks_extract_endpoint)
            institutions = self.__web.getOptionsValuesFromSelection('ctl00_ContentPlaceHolder1_ddlAgentes')
            institutions.remove('-1')

            for institution in institutions:
                transaction['institution'] = institution
                accounts = self.__get_accounts_from_institution_in_extract_page(institution, start_date, end_date)

                for account in accounts:
                    transaction['account'] = account
                    transaction['extract'] = \
                        self.__get_transactions_from_account_and_period_in_extract_page(institution, account,
                            start_date, end_date)
                    transactions.append(transaction)

            return transactions

        except:
            logging.error('Failed to get the user extract!')
            raise RuntimeError('Failed to get the user extract!')

# Get the accounts of an user registered institution in the wallet page
#----------------------------------------------------------------------------------------------------------------------
    def __get_accounts_from_institution_in_wallet_page(self, institution, wallet_date):
        logging.debug('Getting the account from institution %s...', institution)
        self.__wallet_data["__VIEWSTATE"] = self.__web.getValueFromPage('#__VIEWSTATE')
        self.__wallet_data["__VIEWSTATEGENERATOR"] = self.__web.getValueFromPage('#__VIEWSTATEGENERATOR')
        self.__wallet_data["__EVENTVALIDATION"] = self.__web.getValueFromPage('#__EVENTVALIDATION')
        self.__wallet_data["ctl00$ContentPlaceHolder1$ddlContas"] = "0"
        self.__wallet_data["ctl00$ContentPlaceHolder1$txtData"] = wallet_date
        self.__wallet_data["ctl00$ContentPlaceHolder1$ddlAgentes"] = institution
        self.__wallet_data["ctl00$ContentPlaceHolder1$ToolkitScriptManager1"] = \
            "ctl00$ContentPlaceHolder1$updFiltro|ctl00$ContentPlaceHolder1$ddlAgentes"
        self.__web.executePost(self.__wallet_endpoint, self.__wallet_data)
        return self.__web.getOptionsValuesFromSelection('ctl00_ContentPlaceHolder1_ddlContas')

# Get the purchased stocks from an account and a date in the wallet page
#----------------------------------------------------------------------------------------------------------------------
    def __get_stocks_from_account_and_date_in_wallet_page(self, institution, account, wallet_date):
        logging.debug('Getting the stocks from account %s...', account)
        self.__wallet_data["__VIEWSTATE"] = self.__web.getValueFromPage('#__VIEWSTATE')
        self.__wallet_data["__VIEWSTATEGENERATOR"] = self.__web.getValueFromPage('#__VIEWSTATEGENERATOR')
        self.__wallet_data["__EVENTVALIDATION"] = self.__web.getValueFromPage('#__EVENTVALIDATION')
        self.__wallet_data["ctl00$ContentPlaceHolder1$ddlAgentes"] = institution
        self.__wallet_data["ctl00$ContentPlaceHolder1$ddlContas"] = account
        self.__wallet_data["ctl00$ContentPlaceHolder1$txtData"] = wallet_date
        self.__wallet_data["ctl00$ContentPlaceHolder1$btnConsultar"] = "Consultar"
        self.__wallet_data["ctl00$ContentPlaceHolder1$ToolkitScriptManager1"] = \
            "ctl00$ContentPlaceHolder1$updFiltro|ctl00$ContentPlaceHolder1$btnConsultar"
        self.__web.executePost(self.__wallet_endpoint, self.__wallet_data)
        extract = self.__read_stocks_in_wallet_page()
        del self.__wallet_data["ctl00$ContentPlaceHolder1$btnConsultar"]
        return extract

# Read the stocks information from wallet page
#----------------------------------------------------------------------------------------------------------------------
    def __read_stocks_in_wallet_page(self):
        logging.debug('Reading the stocks information from wallet page...')
        result = []
        table_id = \
            "ctl00_ContentPlaceHolder1_rptAgenteContaMercado_ctl00_rptContaMercado_ctl00_rprCarteira_ctl00_grdCarteira"
        raw_stocks = self.__web.getTextFromEachElementOfTable(table_id, 1)

        for item in raw_stocks:
            operation = {}
            operation['company'] = item[0]
            operation['type'] = item[1]
            operation['code'] = item[2]
            operation['fullcode'] = item[3]
            operation['price'] = self.__brl_string_to_float(item[4])
            operation['quantity'] = int(item[5])
            operation['factor'] = self.__brl_string_to_float(item[6])
            operation['total'] = self.__brl_string_to_float(item[7])
            result.append(operation)

        return result

# Get the accounts of an user registered institution in the extract page
#----------------------------------------------------------------------------------------------------------------------
    def __get_accounts_from_institution_in_extract_page(self, institution, start_date, end_date):
        logging.debug('Getting the account from institution %s...', institution)
        self.__extract_data["__VIEWSTATE"] = self.__web.getValueFromPage('#__VIEWSTATE')
        self.__extract_data["__VIEWSTATEGENERATOR"] = self.__web.getValueFromPage('#__VIEWSTATEGENERATOR')
        self.__extract_data["__EVENTVALIDATION"] = self.__web.getValueFromPage('#__EVENTVALIDATION')
        self.__extract_data["ctl00$ContentPlaceHolder1$ddlContas"] = "0"
        self.__extract_data["ctl00$ContentPlaceHolder1$txtDataDeBolsa"] = start_date
        self.__extract_data["ctl00$ContentPlaceHolder1$txtDataAteBolsa"] = end_date
        self.__extract_data["ctl00$ContentPlaceHolder1$ddlAgentes"] = institution
        self.__web.executePost(self.__stocks_extract_endpoint, self.__extract_data)
        return self.__web.getOptionsValuesFromSelection('ctl00_ContentPlaceHolder1_ddlContas')

# Get the stocks transactions from an account and a period in the extract page
#----------------------------------------------------------------------------------------------------------------------
    def __get_transactions_from_account_and_period_in_extract_page(self, institution, account, start_date, end_date):
        logging.debug('Getting the transactions from account %s...', account)
        self.__extract_data["__VIEWSTATE"] = self.__web.getValueFromPage('#__VIEWSTATE')
        self.__extract_data["__VIEWSTATEGENERATOR"] = self.__web.getValueFromPage('#__VIEWSTATEGENERATOR')
        self.__extract_data["__EVENTVALIDATION"] = self.__web.getValueFromPage('#__EVENTVALIDATION')
        self.__extract_data["ctl00$ContentPlaceHolder1$ddlAgentes"] = institution
        self.__extract_data["ctl00$ContentPlaceHolder1$ddlContas"] = account
        self.__extract_data["ctl00$ContentPlaceHolder1$txtDataDeBolsa"] = start_date
        self.__extract_data["ctl00$ContentPlaceHolder1$txtDataAteBolsa"] = end_date
        self.__extract_data["ctl00$ContentPlaceHolder1$btnConsultar"] = "Consultar"
        self.__web.executePost(self.__stocks_extract_endpoint, self.__extract_data)
        extract = self.__read_transactions_in_extract_page()
        self.__reload_transactions_in_extract_page(institution, account, start_date, end_date)
        del self.__extract_data["ctl00$ContentPlaceHolder1$btnConsultar"]
        return extract

# Reload the extract page
#----------------------------------------------------------------------------------------------------------------------
    def __reload_transactions_in_extract_page(self, institution, account, start_date, end_date):
        logging.debug('Reloading the extract page...')
        self.__extract_data["__VIEWSTATE"] = self.__web.getValueFromPage('#__VIEWSTATE')
        self.__extract_data["__VIEWSTATEGENERATOR"] = self.__web.getValueFromPage('#__VIEWSTATEGENERATOR')
        self.__extract_data["__EVENTVALIDATION"] = self.__web.getValueFromPage('#__EVENTVALIDATION')
        self.__extract_data["ctl00$ContentPlaceHolder1$ddlAgentes"] = institution
        self.__extract_data["ctl00$ContentPlaceHolder1$ddlContas"] = account
        self.__extract_data["ctl00$ContentPlaceHolder1$txtDataDeBolsa"] = start_date
        self.__extract_data["ctl00$ContentPlaceHolder1$txtDataAteBolsa"] = end_date
        self.__extract_data["ctl00$ContentPlaceHolder1$btnConsultar"] = "Nova Consulta"
        self.__web.executePost(self.__stocks_extract_endpoint, self.__extract_data)

# Read the transactions information from extract page
#----------------------------------------------------------------------------------------------------------------------
    def __read_transactions_in_extract_page(self):
        logging.debug('Reading the transactions information in the extract page...')
        result = []
        table_id = "ctl00_ContentPlaceHolder1_rptAgenteBolsa_ctl00_rptContaBolsa_ctl00_pnAtivosNegociados"
        raw_extract = self.__web.getTextFromEachElementOfTable(table_id, 0)

        for item in raw_extract:
            operation = {}
            operation['date'] = item[0].replace('\\n','').replace(' ','')
            operation['operation'] = item[1].replace('\\n','').replace(' ','')
            operation['market'] = item[2].replace('\\n','').replace(' ','')
            operation['expiration'] = item[3].replace('\\n','').replace(' ','')
            operation['code'] = item[4].replace('\\n','').replace(' ','')
            operation['name'] = item[5].replace('\\n','').replace(' ','')
            operation['quantity'] = int(item[6].replace('\\n','').replace(' ',''))
            operation['price'] = self.__brl_string_to_float(item[7].replace('\\n','').replace(' ',''))
            operation['total'] = self.__brl_string_to_float(item[8].replace('\\n','').replace(' ',''))
            operation['cotation'] = self.__brl_string_to_float(item[9].replace('\\n','').replace(' ',''))
            result.append(operation)

        return result

# Convert brazilian money string to float
#----------------------------------------------------------------------------------------------------------------------
    def __brl_string_to_float(self, brl_string):
        setlocale(LC_NUMERIC, 'pt_BR.UTF-8')
        return atof(brl_string)
#----------------------------------------------------------------------------------------------------------------------
