from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_something():
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.get('https://www.leagueofgraphs.com/')
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR, 'div.container input.search_field').click()
    driver.find_element(By.CSS_SELECTOR, 'div.container input.search_field').clear()
    driver.find_element(By.CSS_SELECTOR, 'div.container input.search_field').send_keys('Вовчик Зеленский')
    driver.find_element(By.CSS_SELECTOR, 'div.container button').click()
    time.sleep(10)



