#!/usr/bin/python3

import os
import time
import logging
import datetime
from shutil import copy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class DarfGenerator:

# Initialize the class with its properties
#----------------------------------------------------------------------------------------------------------------------
    def __init__(self, debug=False):
        self.__endpoint = "http://www31.receita.fazenda.gov.br/SicalcWeb/UF.asp?AP=P&Person=N&TipTributo=1&FormaPagto=1"
        copy(os.path.dirname(__file__) + "/../libs/chromedriver", "/tmp/chromedriver")
        os.chmod("/tmp/chromedriver", 0o775)
        self.__web = webdriver.Chrome("/tmp/chromedriver")
        self.__debug = debug

# Generate the darf using governement`s system
#----------------------------------------------------------------------------------------------------------------------
    def generate(self):
        logging.debug('Generating the darf using governement`s system...')

        #Navigate to the government system
        self.__web.get(self.__endpoint)

        #Select state and confirm
        state = self.__web.find_element_by_tag_name('select')
        for option in state.find_elements_by_tag_name('option'):
            if option.text == 'SP - SAO PAULO':
                option.click()
                break
        self.__web.find_element_by_xpath('//*[@id="botoes"]/input[2]').click()

        #Select city and confirm
        state = self.__web.find_element_by_tag_name('select')
        for option in state.find_elements_by_tag_name('option'):
            if option.text == 'SAO PAULO':
                option.click()
                break
        self.__web.find_element_by_xpath('//*[@id="botoes"]/input[2]').click()

        #Insert darf government code
        self.__web.find_element_by_name('CodReceita').send_keys('6015')
        self.__web.find_element_by_xpath('//*[@id="botoes"]/input[2]').click()
        time.sleep(5)

        #Insert darf period and value
        try:
            self.__web.switch_to.alert.accept()
        except:
            logging.debug("Alerta nao apareceu!")
        date = datetime.date.today().strftime("%m%Y")
        self.__web.find_element_by_name('PA').send_keys(date)
        value = 11.00
        self.__web.find_element_by_name('TxtValRec').send_keys("%.2f" %value)
        self.__web.find_element_by_xpath('//*[@id="botoes"]/input[3]').click()

        #Check information and continue
        self.__web.find_element_by_xpath('//*[@id="botoes"]/input[2]').click()

        #Finish generation
        input()
        self.__web.close()
        self.__web.quit()

#----------------------------------------------------------------------------------------------------------------------

#Testing
#----------------------------------------------------------------------------------------------------------------------
logging.basicConfig(level=1)
darf = DarfGenerator(True)
darf.generate()