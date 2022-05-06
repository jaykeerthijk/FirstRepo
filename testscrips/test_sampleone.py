from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome("/drivers/chromedriver.exe")
driver.maximize_window()
driver.get("http://demowebshop.tricentis.com/")
sleep(3)
driver.find_element(by=By.ID, value="small-searchterms").send_keys("jk")
driver.find_element(by=By.XPATH, value="//input[@value='Search']").click()
sleep(5)
driver.close()