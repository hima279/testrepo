from selenium import webdriver
from selenium.webdriver.common.by import By
#launching the driver
driver=webdriver.Chrome("C:\Drivers\chromedriver.exe")

#launching the application
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

#is_displayed(), is_enabled()
searchbox=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")

#checking if searchbox is displayed or not
print(searchbox.is_displayed())

#checking if searchbox is enabled or not
print(searchbox.is_enabled())

#is_selected()
rbmale=driver.find_element(By.XPATH,"//input[@id='gender-male']")
rbfemale=driver.find_element(By.XPATH,"//input[@id='gender-female']")
print(rbmale.is_selected())
print(rbfemale.is_selected())
#clicking the male radio button
rbmale.click()
#checking if the male radio button is selected or not
print(rbmale.is_selected())

