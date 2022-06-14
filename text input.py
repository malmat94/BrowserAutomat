from selenium import webdriver
import time
import os
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_argument('--disable-notifications')
options.add_argument('--disable-popup-blocking')
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(executable_path="C:/Users/Maliccy/AppData/Local/Programs/chromedriver.exe", chrome_options = options)
driver.set_window_size(1000, 1000)

"""Loading the webpage"""
url = "https://chomikuj.pl/"
driver.get(url)
time.sleep(3)

"""Filling the text boxes"""
field_1 = driver.find_element(By.ID, 'topBarLogin')  #looking for a text field with specific ID
field_1.send_keys("knornudel")    #inserting text into text field
time.sleep(1)

field_1 = driver.find_element(By.ID, 'topBarPassword')
field_1.send_keys("ziom20")
time.sleep(1)

"""Clicking a button"""
click_1 = driver.find_element(By.ID, 'topBar_LoginBtn')   #looking for button with specific ID
click_1.click()   #clicking a button

"""Getting some text"""

time.sleep(3)
driver.quit()