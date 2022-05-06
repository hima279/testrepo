from selenium import webdriver

driver=webdriver.Chrome("C:\Drivers\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.quit()
