'''
Created on May 30, 2018
@author: venkateshwara.d
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

class AutoComplete():

    def test(self):
        baseUrl = "http://www.southwest.com"
        chrome_driver_path = os.path.abspath('..')  + "\\Drivers\\chromedriver.exe"
 
        driver=webdriver.Chrome(chrome_driver_path)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # Send Partial Data
        cityField = driver.find_element_by_id("air-city-departure")
        cityField.send_keys("New York")
        time.sleep(3)
        # Find the item and click
        itemToSelect = driver.find_element_by_xpath("//ul[@id='air-city-departure-menu']//li[contains(text(),'NJ - EWR')]")
        itemToSelect.click()

        # time.sleep(3)
        # driver.quit()

ff = AutoComplete()
ff.test()
