from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

import time
from pathlib import Path
import os
from pynput import *
from pyautogui import *

import shutil

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

time.sleep(2)
click_1 = click(132, 661) #Lokalizacja urzędu

time.sleep(1)
click_2 = click(126, 565) #Loklaizacja typu wniosku

time.sleep(0.5)
click_3 = click(267, 689) #Loklaizacja dodania dorosłego

time.sleep(0.5)
click_4 = click(454, 677) #Lokalizacja dodania dzieci

time.sleep(0.5)
click_5 = click(454, 677) #Lokalizacja dodania dzieci

time.sleep(1)
click_6 = click(230, 900) #Loklazacja "wybierz termin"
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(1)
screen_1 = "paszport_1.png"
driver.get_screenshot_as_file(screen_1)  #screenshot of dates page for 1st month

time.sleep(1)
click_7 = click(848, 625) #Loklazacja "następny miesiąc"
screen_2 = "paszport_2.png"
driver.get_screenshot_as_file(screen_2)    #screenshot of dates page for 2nd month


folder_path = "D:/Użytkownicy/Maliccy/Dokumenty/Mateusz/PROGRAMOWANIE/Python/Projekty/BrowserAutomat/PassPort/"
s_1_destination = Path(folder_path + screen_1)
s_2_destination = Path(folder_path + screen_2)

if s_1_destination.is_file():
    os.unlink(s_1_destination)
    shutil.move(screen_1, folder_path)
else:
    shutil.move(screen_1, folder_path)


if s_2_destination.is_file():
    os.unlink(s_2_destination)
    shutil.move(screen_2, folder_path)
else:
    shutil.move(screen_2, folder_path)

time.sleep(3)
driver.quit()



