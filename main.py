from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys("standard_user")
driver.find_element(By.XPATH,"//*[@id='password']").send_keys("secret_sauce")
driver.find_element(By.XPATH, "//*[@id='login-button']").click()

text_msg = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div').text
print(text_msg)

