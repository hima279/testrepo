from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome("C:\Drivers\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
time.sleep(5)
driver.close()
driver.quit()