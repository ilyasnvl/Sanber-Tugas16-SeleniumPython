from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import time
from pom.loginElem import loginElm
from pom.data import addEmployee

def test_login(self, driver):
    driver = self.driver
    driver.get(self.url)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, loginElm.username).send_keys(addEmployee.usrnameLogin)
    driver.find_element(By.CSS_SELECTOR, loginElm.password).send_keys(addEmployee.passLogin)
    driver.find_element(By.CSS_SELECTOR, loginElm.btnLogin).click()
    time.sleep(2)

    # validasi
    expected_login = (addEmployee.expectedLogin)
    assert expected_login == driver.current_url