from selenium import webdriver
import time

options = webdriver.ChromeOptions()     # accesing chrome web browser
driver = webdriver.Chrome(executable_path="C:/Users/Maliccy/AppData/Local/Programs/chromedriver.exe", chrome_options = options)     # accesing web driver

first_site = driver.get("https://rezerwacja.gdansk.uw.gov.pl:8445/qmaticwebbooking/#/")     # accesing site from addres via chrome browser
# print(driver.page_source)     # web page code
print(driver.title)
driver.get_screenshot_as_file("paszport.png")     # getting screenshot from a page
time.sleep(3)     # browser is open for 1 sec

number = 1
websites = ["https://github.com/malmat94/BrowserAutomat" , "https://www.udemy.com/course/browser-automation-with-python-selenium/learn/lecture/13325740#overview" , "https://www.youtube.com/"]    # list of pages I want to visit

for website in websites:    # Iterates through the pages from the list above and screenshot them

    driver.get(website)
    print(driver.title)
    driver.get_screenshot_as_file("site" + str(number) + ".png")
    number += number
    time.sleep(1)

driver.quit()     # browser is open for 1 sec