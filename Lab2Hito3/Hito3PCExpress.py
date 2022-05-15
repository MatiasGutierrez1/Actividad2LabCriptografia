from lib2to3.pgen2 import driver
import time
from selenium import webdriver
import string
import random

def crearCuenta():
    driver = webdriver.Chrome("D:\Reespaldo\Guias y documentos\Criptografia\chromedriver")
    # base = string.ascii_letters

    driver.get("https://tienda.pc-express.cl/index.php?route=account/register")
    time.sleep(3)
    driver.find_element_by_id("input-rut").send_keys("22483061-0")
    # time.sleep(1)
    driver.find_element_by_id("input-telephone").send_keys("987057173")
    # time.sleep(1)
    driver.find_element_by_id("input-firstname").send_keys("Matias")
    # time.sleep(1)
    driver.find_element_by_id("input-lastname").send_keys("Gutierrez")
    # time.sleep(1)
    driver.find_element_by_id("input-email").send_keys("kenihap293@hbehs.com")
    # time.sleep(1)
    driver.find_element_by_name("email_confirm").send_keys("kenihap293@hbehs.com")
    # time.sleep(1)
    # password = driver.find_element_by_id("input-password")
    # password.clear()
    # passRandom = ''.join(random.choice(base) for i in range(41))
    # password.send_keys(passRandom)
    driver.find_element_by_id("input-password").send_keys("asdf")
    # time.sleep(1)
    driver.find_element_by_id("input-confirm").send_keys("asdf")
    # driver.find_element_by_id("input-confirm").send_keys(passRandom)
    # print("Pass random de 41 caracteres usada: " + str(passRandom))
    time.sleep(1)
    driver.find_element_by_css_selector("input[type=\"submit\" i]").click()
    time.sleep(5)

def iniciarSesion():
    driver = webdriver.Chrome("D:\Reespaldo\Guias y documentos\Criptografia\chromedriver")

    driver.get("https://tienda.pc-express.cl/index.php?route=account/login")
    time.sleep(3)
    driver.find_element_by_id("input-rut").send_keys("20309809-k")
    time.sleep(1)
    driver.find_element_by_id("input-password").send_keys("asdf")
    time.sleep(1)
    driver.find_element_by_css_selector("input[type=\"submit\" i]").click()
    time.sleep(4)
    driver.find_element_by_id("input-rut").send_keys("20309809-k")
    time.sleep(1)
    driver.find_element_by_id("input-password").send_keys("asdf")
    time.sleep(1)
    driver.find_element_by_css_selector("input[type=\"submit\" i]").click()
    time.sleep(5)

def restablecerPass():
    driver = webdriver.Chrome("D:\Reespaldo\Guias y documentos\Criptografia\chromedriver")

    driver.get("https://tienda.pc-express.cl/index.php?route=account/forgotten")
    time.sleep(3)
    driver.find_element_by_id("input-email").send_keys("gijox48921@dmosoft.com")
    time.sleep(1)
    driver.find_element_by_css_selector("input[type=\"submit\" i]").click()
    time.sleep(5)

def restablecerPass2():
    driver = webdriver.Chrome("D:\Reespaldo\Guias y documentos\Criptografia\chromedriver")

    driver.get("https://tienda.pc-express.cl/index.php?route=account/reset&code=AIqqfUhk6TBnXLsnTLVotGy3yakbKWFiJGTMXwYh")
    time.sleep(3)
    driver.find_element_by_id("input-password").send_keys("qwer")
    # time.sleep(1)
    driver.find_element_by_id("input-confirm").send_keys("qwer")
    # time.sleep(1)
    driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(3)

def modificarPass():
    driver = webdriver.Chrome("D:\Reespaldo\Guias y documentos\Criptografia\chromedriver")

    driver.get("https://tienda.pc-express.cl/index.php?route=account/login")
    time.sleep(4)
    driver.find_element_by_id("input-rut").send_keys("20309809-k")
    time.sleep(1)
    driver.find_element_by_id("input-password").send_keys("qwer")
    time.sleep(1)
    driver.find_element_by_css_selector("input[type=\"submit\" i]").click()
    time.sleep(4)
    driver.find_element_by_id("input-rut").send_keys("20309809-k")
    time.sleep(1)
    driver.find_element_by_id("input-password").send_keys("qwer")
    time.sleep(1)
    driver.find_element_by_css_selector("input[type=\"submit\" i]").click()
    time.sleep(5)
    driver.get("https://tienda.pc-express.cl/index.php?route=account/password")
    time.sleep(1)
    driver.find_element_by_id("input-password").send_keys("asdf")
    time.sleep(1)
    driver.find_element_by_id("input-confirm").send_keys("asdf")
    time.sleep(1)
    driver.find_element_by_css_selector("input[type=\"submit\" i]").click()
    time.sleep(5)

crearCuenta()
# iniciarSesion()
# restablecerPass()
# restablecerPass2()
# modificarPass()
