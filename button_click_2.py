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


url = "https://rezerwacja.gdansk.uw.gov.pl:8445/qmaticwebbooking/#/"
driver.get(url)
time.sleep(1)
# print(driver.page_source)

# clicking the button
click_1 = driver.find_element(By.ID, '1cf1e3e60eeb96dae2bb572487249bd48cc5bed0024960eaee0c893ce4918569')
click_1.click()


# clicking the button
click_2 = driver.find_element(By.TAG_NAME, 'radio-72')
click_2.click()

# closing the popup
time.sleep(1)

driver.execute_script('el = document.elementFromPoint(47, 457); el.click();')
# driver.switch_to.alert.dismiss()
ActionChains(driver).move_to_element_with_offset(driver.find_element_by_xpath("//button[contains(text(),'Przejdź dalej')]"), 200, 0).click().perform()

time.sleep(3)
driver.quit()



