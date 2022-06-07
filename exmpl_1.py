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


url = "https://www.youtube.com/"
driver.get(url)
time.sleep(3)
print(driver.page_source)

# # clicking the button
click_1 = driver.find_element(By.XPATH, "//button[contains(text(),'ZAAKCEPTUJ WSZYSTKO')]")
click_1.click()
print(driver.page_source)

# # clicking the button
# click_1 = driver.find_element(By.XPATH, "//button[contains(text(),'Akceptuj')]")
# click_1.click()
#
# # clicking the button
# # click_5 = driver.find_element(By.XPATH, "//button[contains(text(),'Wyszukaj')]")
# # click_5.click()
#
# # closing the popup
# time.sleep(1)
#
# # ActionChains(driver).move_to_element_with_offset(driver.find_element(By.XPATH, "//button[contains(text(),'Przejdź dalej')]"), 200, 0).click().perform() #Clicking 200px to the right of the popup
#
# # time.sleep(3)
# # driver.quit()