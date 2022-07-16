from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from assertu.assertionsfor import Assertion
driver = webdriver.Chrome('./chromedriver.exe')

class loginio:
    @staticmethod
    def startio():
     driver.find_element(By.CSS_SELECTOR, 'div.container button.btn.btn-outline-white').click()
     driver.find_element(By.CSS_SELECTOR, 'input#signinEmail').send_keys(Assertion.email)
     driver.find_element(By.CSS_SELECTOR, 'input#signinPassword').send_keys(Assertion.password)
     driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary:disabled').click()

