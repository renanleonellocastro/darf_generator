#!/usr/bin/python3

import logging
import pyquery
from datetime import date
from include.automatedweb import AutomatedWeb

class Cei():

#Definition of Class Constants
#----------------------------------------------------------------------------------------------------------------------
    __login_endpoint = "https://cei.b3.com.br/cei_responsivo/login.aspx"
    __home_endpoint = "https://cei.b3.com.br/CEI_Responsivo/home.aspx"
    __stocks_extract_endpoint = "https://cei.b3.com.br/CEI_Responsivo/negociacao-de-ativos.aspx"
    __login_data = {"__EVENTTARGET": "", "__EVENTARGUMENT": "", "ctl00$ContentPlaceHolder1$txtLogin": "",
                "ctl00$ContentPlaceHolder1$txtSenha": "", "__VIEWSTATEGENERATOR": "", "_ASYNCPOST": True,
                "__EVENTVALIDATION": "", "__VIEWSTATE": "", "ctl00$ContentPlaceHolder1$btnLogar": "Entrar"}
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
            print (institutions)
            institutions.remove('-1')
            print ("chegou!")

            for institution in institutions:
                transaction['institution'] = institution
                accounts = self.__get_accounts_from_institution(institution, start_date, end_date)

                for account in accounts:
                    transaction['account'] = account
                    transaction['extract'] = \
                        self.__get_transactions_from_account_and_period(institution, account, start_date, end_date)
                    transactions.append(transaction)

            return transactions

        except:
            logging.error('failed')
            raise RuntimeError('failed')

# Get the accounts of an user registered institution
#----------------------------------------------------------------------------------------------------------------------
    def __get_accounts_from_institution(self, institution, start_date, end_date):
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

# Get the stocks transactions from an account and a period
#----------------------------------------------------------------------------------------------------------------------
    def __get_transactions_from_account_and_period(self, institution, account, start_date, end_date):
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
        extract = self.__read_extract_in_page()
        self.__reload_transactions_page(institution, account, start_date, end_date)
        del self.__extract_data["ctl00$ContentPlaceHolder1$btnConsultar"]
        return extract

# Reload the stock transactions page
#----------------------------------------------------------------------------------------------------------------------
    def __reload_transactions_page(self, institution, account, start_date, end_date):
        logging.debug('Reloading the transactions page...')
        self.__extract_data["__VIEWSTATE"] = self.__web.getValueFromPage('#__VIEWSTATE')
        self.__extract_data["__VIEWSTATEGENERATOR"] = self.__web.getValueFromPage('#__VIEWSTATEGENERATOR')
        self.__extract_data["__EVENTVALIDATION"] = self.__web.getValueFromPage('#__EVENTVALIDATION')
        self.__extract_data["ctl00$ContentPlaceHolder1$ddlAgentes"] = institution
        self.__extract_data["ctl00$ContentPlaceHolder1$ddlContas"] = account
        self.__extract_data["ctl00$ContentPlaceHolder1$txtDataDeBolsa"] = start_date
        self.__extract_data["ctl00$ContentPlaceHolder1$txtDataAteBolsa"] = end_date
        self.__extract_data["ctl00$ContentPlaceHolder1$btnConsultar"] = "Nova Consulta"
        self.__web.executePost(self.__stocks_extract_endpoint, self.__extract_data)

# Read the transactions extract information from transactions page
#----------------------------------------------------------------------------------------------------------------------
    def __read_extract_in_page(self):
        logging.debug('Reading the extract information from transactions page...')
        return []

# [
#     {
#         institution: 'Banco Inter',
#         account: 12345,
#         stockHistory: [
#             {
#                 date: "2019-06-12T03:00:00.000Z",
#                 operation: "C", // C (Compra) ou V (Venda),
#                 market: "Mercado a Vista",
#                 expiration: "",
#                 code: "BTOW3",
#                 name: "B2W DIGITAL ON NM",
#                 quantity: 200,
#                 price: 32.2,
#                 totalValue: 6440,
#                 cotation: 1
#             }
#         ]
#     }
# ]
