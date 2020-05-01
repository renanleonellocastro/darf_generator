#!/usr/bin/python3

import os
import time
import logging
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
        time.sleep(5)

        #Select state and confirm
        state = self.__web.find_element_by_tag_name('select')
        for option in state.find_elements_by_tag_name('option'):
            if option.text == 'SP - SAO PAULO':
                option.click()
                break
        self.__web.find_element_by_xpath('//*[@id="botoes"]/input[2]').click()
        time.sleep(5)

        #Finish generation
        time.sleep(30)
        self.__web.quit()
        self.__web.close()

#----------------------------------------------------------------------------------------------------------------------

#Testing
#----------------------------------------------------------------------------------------------------------------------
logging.basicConfig(level=1)
darf = DarfGenerator(True)
darf.generate()