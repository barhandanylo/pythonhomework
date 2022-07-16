from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from assertu.assertionsfor import Assertion


def test_something():
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.get('https://guest:welcome2qauto@qauto2.forstudy.space/')
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR, 'div.container button.btn.btn-outline-white').click()
    driver.find_element(By.CSS_SELECTOR, 'div.modal-footer button.btn-link').click()
    driver.find_element(By.CSS_SELECTOR, 'input#signupName').send_keys(Assertion.name)
    driver.find_element(By.CSS_SELECTOR, 'input#signupLastName').send_keys(Assertion.last_name)
    driver.find_element(By.CSS_SELECTOR, 'input#signupEmail').send_keys(Assertion.email)
    driver.find_element(By.CSS_SELECTOR, 'input#signupPassword').send_keys(Assertion.password)
    driver.find_element(By.CSS_SELECTOR, 'input#signupRepeatPassword').send_keys(Assertion.password)
    driver.find_element(By.CSS_SELECTOR, 'div.modal-footer button').click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, 'a.btn.btn-link.text-danger.btn-sidebar').click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'div.container button.btn.btn-outline-white').click()
    driver.find_element(By.CSS_SELECTOR, 'input#signinEmail').send_keys(Assertion.email)
    driver.find_element(By.CSS_SELECTOR, 'input#signinPassword').send_keys(Assertion.password)
    driver.find_element(By.CSS_SELECTOR, 'div.modal-footer.d-flex.justify-content-between > button.btn.btn-primary').click()
    time.sleep(5)

