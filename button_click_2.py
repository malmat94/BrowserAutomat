from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

import time
import os
from pynput import *
from pyautogui import *

options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_argument('--disable-notifications')
options.add_argument('--disable-popup-blocking')
options.add_experimental_option('useAutomationExtension', False)

driver_path = "C:/Users/Maliccy/AppData/Local/Programs/chromedriver.exe"
driver = webdriver.Chrome(driver_path, chrome_options = options)
driver.set_window_size(1000, 1000)


url = "https://rezerwacja.gdansk.uw.gov.pl:8445/qmaticwebbooking/#/"
driver.get(url)

# click_1 = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div/div[1]/div[1]/div/div/div/div[2]/div/div/div/div/div/div/div[3]/div/div')
# click_1.click()

click_1 = click(132, 661) #Lokalizacja urzędu

time.sleep(1)
click_2 = click(126, 565) #Loklaizacja typu wniosku

time.sleep(1)
click_3 = click(267, 689) #Loklaizacja dodania dorosłego

time.sleep(1)
click_4 = click(454, 677) #Lokalizacja dodania dzieci

time.sleep(1)
click_5 = click(454, 677) #Lokalizacja dodania dzieci

time.sleep(1)
click_6 = click(230, 900) #Loklazacja "wybierz termin"
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(1)
driver.get_screenshot_as_file("paszport_1.png")  #screenshot of dates page for 1st month

time.sleep(1)
click_7 = click(848, 625) #Loklazacja "następny miesiąc"
driver.get_screenshot_as_file("paszport_2.png")    #screenshot of dates page for 2nd month

#Waiting for the webpage to load
# try:
#     click_2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, '4fe2df1ac02036b7096beb9b80b8e0e8924c3c282eb992fc83b5a3977ddd20b1')))
#     click_2.click()
#
# except:
#     print("Kurwa no nie ma...")


# clicking the button
# click_2 = driver.find_element(By.TAG_NAME, 'radio-72')
# click_2.click()

# closing the popup
time.sleep(1)

# driver.execute_script('el = document.elementFromPoint(47, 457); el.click();')
# # driver.switch_to.alert.dismiss()
# ActionChains(driver).move_to_element_with_offset(driver.find_element_by_xpath("//button[contains(text(),'Przejdź dalej')]"), 200, 0).click().perform()

time.sleep(3)
# driver.quit()



