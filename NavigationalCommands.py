from selenium import webdriver

driver=webdriver.Chrome("C:\Drivers\chromedriver.exe")
driver.get("https://www.snapdeal.com")
driver.get("https://www.amazon.com")
driver.back()
driver.forward()
driver.refresh()
driver.quit()
