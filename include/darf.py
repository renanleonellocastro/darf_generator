#!/usr/bin/python3

import os
import time
import base64
import logging
import datetime
from shutil import copy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class DarfGenerator:

# Initialize the class with its properties
#----------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        self.__endpoint = "http://www31.receita.fazenda.gov.br/SicalcWeb/UF.asp?AP=P&Person"\
            + "=N&TipTributo=1&FormaPagto=1"
        copy(os.path.dirname(__file__) + "/../libs/chromedriver", "/tmp/chromedriver")
        os.chmod("/tmp/chromedriver", 0o775)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.__web = webdriver.Chrome(executable_path="/tmp/chromedriver", options=options)

# Find html option in a list of options
#----------------------------------------------------------------------------------------------------------------------
    def __find_option(self, option):
        logging.debug('Finding the option %s...', option)
        options = self.__web.find_element_by_tag_name('select')
        for possible_option in options.find_elements_by_tag_name('option'):
            if possible_option.text == option:
                possible_option.click()
                return True
        raise ValueError("Option: %s not found!" %option)

# Proceed to next step clicking in continue button
#----------------------------------------------------------------------------------------------------------------------
    def __proceed_next_step(self, button=2):
        logging.debug('Proceeding to next step clicking in continue button...')
        self.__web.find_element_by_xpath('//*[@id="botoes"]/input[%d]'%button).click()

# Insert government code
#----------------------------------------------------------------------------------------------------------------------
    def __insert_government_code(self):
        logging.debug('Inserting government code...')
        self.__web.find_element_by_name('CodReceita').send_keys('6015')
        self.__proceed_next_step()

# Insert darf period and value
#----------------------------------------------------------------------------------------------------------------------
    def __insert_period_and_value(self, period, value):
        logging.debug('Inserting darf period and value...')
        #handle alert if it appears
        try:
            self.__web.switch_to.alert.accept()
        except:
            logging.debug("Alerta nao apareceu!")

        logging.debug('Inserting period...')
        date = period.strftime("%m%Y")
        self.__web.find_element_by_name('PA').send_keys(date)
        logging.debug('Inserting value...')
        self.__web.find_element_by_name('TxtValRec').send_keys("%.2f" %value)
        self.__proceed_next_step(3)

# Select state and city
#----------------------------------------------------------------------------------------------------------------------
    def __select_state_and_city(self, state, city):
        logging.debug('Selecting state and city...')
        self.__find_option(state)
        self.__proceed_next_step()
        self.__find_option(city)
        self.__proceed_next_step()

# Fill CPF number
#----------------------------------------------------------------------------------------------------------------------
    def __fill_cpf(self, cpf):
        logging.debug('Filling the cpf number...')
        self.__web.find_element_by_name('Num_Princ').send_keys(cpf[:9])
        self.__web.find_element_by_name('Num_DV').send_keys(cpf[-2:])

# Download the captcha
#----------------------------------------------------------------------------------------------------------------------
    def __download_captcha(self):
        logging.debug('Downloading the captcha...')
        captcha = self.__web.execute_script("""
            var ele = arguments[0];
            var cnv = document.createElement('canvas');
            cnv.width = ele.width; cnv.height = ele.height;
            cnv.getContext('2d').drawImage(ele, 0, 0);
            return cnv.toDataURL('captcha/jpeg').substring(22);    
            """, self.__web.find_element_by_id("img_captcha_serpro_gov_br"))
        with open(r"../downloads/captcha.jpg", 'wb') as f:
            f.write(base64.b64decode(captcha))

# Solving the captcha
#----------------------------------------------------------------------------------------------------------------------
    def __solve_captcha(self):
        logging.debug('Solving the captcha...')
        solved = False
        while (not solved):
            self.__download_captcha()
            captcha_answer = input("Enter the solved captcha: ")
            self.__web.find_element_by_id("txtTexto_captcha_serpro_gov_br").send_keys(captcha_answer)
            self.__proceed_next_step()
            try:
                time.sleep(2)
                self.__web.find_element_by_id("txtTexto_captcha_serpro_gov_br")
                logging.error('Captcha wrong. Try again!')
            except:
                solved = True

# Save darf bill
#----------------------------------------------------------------------------------------------------------------------
    def __save_bill(self, name):
        logging.debug('Saving the darf bill...')
        self.__proceed_next_step()
        time.sleep(2)
        self.__web.switch_to.window(window_name=self.__web.window_handles[-1])
        time.sleep(2)
        self.__web.save_screenshot(os.path.dirname(__file__) + "/../downloads/%s" %name)

# Generate the darf using governement system
#----------------------------------------------------------------------------------------------------------------------
    def generate(self, cpf, date, value):
        logging.debug('Generating the darf for user %s...', cpf)
        #Navigate to the government system
        self.__web.get(self.__endpoint)
        #Select state and city
        self.__select_state_and_city("SP - SAO PAULO", "SAO PAULO")
        #Insert darf government code
        self.__insert_government_code()
        #time.sleep(5)
        #Insert darf period and value
        self.__insert_period_and_value(date, value)
        #Check information and continue
        self.__proceed_next_step()
        #Fill CPF number
        self.__fill_cpf(cpf)
        #Solve captcha
        self.__solve_captcha()
        #Save darf bill
        self.__save_bill("darf.png")
        #Finish generation
        self.__web.close()
        self.__web.quit()
#----------------------------------------------------------------------------------------------------------------------
