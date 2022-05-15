# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import codecs

usuarios = ['benjavizaviza@gmail.com', 'carda78@chile.com', 'cl.rodriguez.untechoparachile@gmail.com', 'darlynluque78@gmail.com', 'javiera_bienkoketa@hotmail.com']
passwords = ['BenjaPro34000', 'farola', 'coyote', 'teamo123', "klklkñlklñkñ"]

def probarSepuls(): 
    driver = webdriver.Chrome("D:\Reespaldo\Guias y documentos\Criptografia\chromedriver")
    driver.get("https://sepuls.cl/customer/login")
    time.sleep(3)

    for x in range(5):
        user = driver.find_element_by_id("customer_email")
        user.clear()
        user.send_keys(usuarios[x])
        time.sleep(1)
        passw = driver.find_element_by_id("customer_password")
        passw.clear()
        passw.send_keys(passwords[x].decode('utf-8').strip())
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='submit_login']").click()
        time.sleep(1)

def probarElpais():
    driver = webdriver.Chrome("D:\Reespaldo\Guias y documentos\Criptografia\chromedriver")
    driver.get("https://elpais.com/subscriptions/#/sign-in?prod=REG&o=CABEP&backURL=https%3A%2F%2Felpais.com")
    time.sleep(3)
    driver.find_element_by_id("didomi-notice-agree-button").click()
    time.sleep(2)

    for x in range(5):
        user = driver.find_element_by_id("subsEmail")
        user.clear()
        user.send_keys(usuarios[x])
        time.sleep(1)
        passw = driver.find_element_by_id("subsPassword")
        passw.clear()
        passw.send_keys(passwords[x].decode('utf-8').strip())
        time.sleep(1)
        driver.find_element_by_id("subsSignIn").click()
        time.sleep(3)

probarSepuls()
# probarElpais()
