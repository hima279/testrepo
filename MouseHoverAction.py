from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
driver=webdriver.Chrome("C:\Drivers\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
#Login
driver.find_element(By.XPATH,'//input[@id="txtUsername"]').send_keys("Admin")
driver.find_element(By.XPATH,'//input[@id="txtPassword"]').send_keys("admin123")
driver.find_element(By.XPATH,'//input[@id="btnLogin"]').click()

#Admin-user management-users
admin=driver.find_element(By.XPATH,'//a[@id="menu_admin_viewAdminModule"]')
usermngt=driver.find_element(By.XPATH,'//a[@id="menu_admin_UserManagement"]')
user=driver.find_element(By.XPATH,'//a[@id="menu_admin_viewSystemUsers"]')
#mouse hover

act=ActionChains(driver)
act.move_to_element(admin).move_to_element(usermngt).move_to_element(user).click().perform()

