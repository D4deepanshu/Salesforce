from datetime import time
import timer
from selenium import webdriver
from selenium.webdriver.common.by import By

"""driver = webdriver.Chrome()
driver.get("https://abm--cpq.sandbox.my.salesforce.com/")
driver.maximize_window()
#driver.find_element(By.XPATH,'//input[@id="Login "]').click()
driver.find_element(*(By.XPATH,"//input[@id='Login']")).click()
driver.find_element(*(By.XPATH,"//input[@id='username']")).send_keys("deepanshu.arora@abm.com.cpq")
driver.find_element(*(By.XPATH,"//input[@id='password']")).send_keys("D4deepanshu@123")
driver.find_element(*(By.XPATH,"//input[@id='Login']")).click()

print(driver.title)"""


driver = webdriver.Firefox()
driver.get("https://abm--cpq.sandbox.my.salesforce.com/")
driver.maximize_window()
#driver.find_element(By.XPATH,'//input[@id="Login "]').click()
driver.find_element(*(By.XPATH,"//input[@id='Login']")).click()
driver.find_element(*(By.XPATH,"//input[@id='username']")).send_keys("deepanshu.arora@abm.com.cpq")
driver.find_element(*(By.XPATH,"//input[@id='password']")).send_keys("D4deepanshu@123")
driver.find_element(*(By.XPATH,"//input[@id='Login']")).click()

print(driver.title)

timer.sleep(20)


