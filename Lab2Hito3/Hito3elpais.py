from lib2to3.pgen2 import driver
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import string
import random

def crearCuenta():
    driver = webdriver.Chrome("D:\Reespaldo\Guias y documentos\Criptografia\chromedriver")
    # base = string.ascii_letters

    driver.get("https://elpais.com/subscriptions/#/register?prod=REG&o=CABEP&backURL=https%3A%2F%2Felpais.com")
    time.sleep(3)
    driver.find_element_by_id("didomi-notice-agree-button").click()
    time.sleep(2)
    driver.find_element_by_id("subsEmail").send_keys("xetev89370@hbehs.com")
    # time.sleep(1)
    driver.find_element_by_id("subsPassword").send_keys("asdfghjk")
    # time.sleep(1)
    driver.find_element_by_id("subsConfirmPassword").send_keys("asdfghjk")
    # time.sleep(1)
    driver.find_element_by_id("subsConfirmPassword").send_keys(Keys.TAB, "28")
    # time.sleep(1)
    driver.find_element_by_id("subsConfirmPassword").send_keys(Keys.TAB, Keys.TAB, "e")
    # time.sleep(1) 
    driver.find_element_by_id("subsConfirmPassword").send_keys(Keys.TAB, Keys.TAB, Keys.TAB, "1999")
    # time.sleep(1)
    driver.find_element_by_id("subsConfirmPassword").send_keys(Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.SPACE)
    # driver.find_element_by_id("subsConfirmPassword").send_keys(Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, "Chile")
    # time.sleep(1)
    # driver.find_element_by_id("subsConfirmPassword").send_keys(Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, "r")
    # time.sleep(1)
    # driver.find_element_by_id("subsConfirmPassword").send_keys(Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.SPACE)
    time.sleep(1)
    driver.find_element_by_id("subsSignUp").click()
    time.sleep(6)

def iniciarSesion():
    driver = webdriver.Chrome("D:\Reespaldo\Guias y documentos\Criptografia\chromedriver")

    driver.get("https://elpais.com/subscriptions/#/sign-in?prod=REG&o=CABEP&backURL=https%3A%2F%2Felpais.com")
    time.sleep(3)
    driver.find_element_by_id("didomi-notice-agree-button").click()
    time.sleep(2)
    driver.find_element_by_id("subsEmail").send_keys("xetev89370@hbehs.com")
    time.sleep(1)
    driver.find_element_by_id("subsPassword").send_keys("asdfghjk")
    time.sleep(1)
    driver.find_element_by_id("subsSignIn").click()
    time.sleep(6)

def restablecerPass():
    driver = webdriver.Chrome("D:\Reespaldo\Guias y documentos\Criptografia\chromedriver")

    driver.get("https://elpais.com/subscriptions/#/forgot-password")
    time.sleep(7)
    driver.find_element_by_id("didomi-notice-agree-button").click()
    time.sleep(5)
    driver.find_element_by_id("subsEmail").send_keys("xetev89370@hbehs.com")
    time.sleep(1)
    driver.find_element_by_id("subsForgotPassword").click()
    time.sleep(6)

def restablecerPass2():
    driver = webdriver.Chrome("D:\Reespaldo\Guias y documentos\Criptografia\chromedriver")

    driver.get("https://elpais.com/subscriptions/#/reset-password?nonce=Nrv2K6G-__tfTyGTCIfoXX5ceRBXrsZQVG2Ss9vtueWThp_V")
    time.sleep(3)
    driver.find_element_by_id("didomi-notice-agree-button").click()
    time.sleep(2)
    driver.find_element_by_id("subsPassword").send_keys("qwertyui")
    time.sleep(1)
    driver.find_element_by_id("confirmPass").send_keys("qwertyui")
    time.sleep(1)
    driver.find_element_by_id("subsResetPassword").click()
    time.sleep(6)

def modificarPass():
    driver = webdriver.Chrome("D:\Reespaldo\Guias y documentos\Criptografia\chromedriver")

    driver.get("https://elpais.com/subscriptions/#/sign-in?prod=REG&o=CABEP&backURL=https%3A%2F%2Felpais.com")
    time.sleep(3)
    driver.find_element_by_id("didomi-notice-agree-button").click()
    time.sleep(2)
    driver.find_element_by_id("subsEmail").send_keys("xetev89370@hbehs.com")
    time.sleep(1)
    driver.find_element_by_id("subsPassword").send_keys("qwertyui")
    time.sleep(1)
    driver.find_element_by_id("subsSignIn").click()
    time.sleep(10)
    driver.get("https://elpais.com/subscriptions/#/profile?rel=areausuario")
    time.sleep(3)
    driver.find_element_by_id("oldPassword").send_keys("qwertyui")
    time.sleep(1)
    driver.find_element_by_id("newPassword").send_keys("asdfghjk")
    time.sleep(1)
    driver.find_element_by_id("confirmPassword").send_keys("asdfghjk")
    time.sleep(1)
    driver.find_element_by_id("confirmPassword").send_keys(Keys.TAB, Keys.SPACE)
    time.sleep(10)

crearCuenta()
# iniciarSesion()
# restablecerPass()
# restablecerPass2()
# modificarPass()