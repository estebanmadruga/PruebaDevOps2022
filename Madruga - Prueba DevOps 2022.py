import time
from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:\\Users\\Esteban\\Downloads\\chromedriver_win32\\chromedriver')
driver.get("http://192.168.56.101:8012/")
elemento1 = driver.find_element(By.ID, "user")
elemento1.clear()
elemento1.send_keys("root")

elemento2 = driver.find_element(By.NAME, "pass")
elemento2.clear()
elemento2.send_keys("password")

driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div/form/div[3]/div/input").click()
driver.get("http://192.168.56.101:8012/")

time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[6]/form[2]/div[1]/input").click()

time.sleep(10)
driver.close()