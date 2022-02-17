from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import 	By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver=webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
driver.get("https://splitter.ai")
driver.maximize_window()

upload= (By.XPATH,"//body/div[6]/div[1]/div[2]/div[1]/div[2]/div[4]/div[1]")
no= (By.XPATH,"//body/div[2]/button[1]/span[1]/*[1]")
myuploads= (By.XPATH,"//button[contains(text(),'My uploads')]")
stem= (By.XPATH,"//body/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/img[1]")


bass= (By.XPATH,"//body/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/a[1]")
drums= (By.XPATH,"//body/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/a[1]")
piano= (By.XPATH,"//body/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[4]/div[1]/div[2]/a[1]")
vocals= (By.XPATH,"//body/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[5]/div[1]/div[2]/a[1]")


WebDriverWait(driver,20).until(EC.element_to_be_clickable(upload)).click()
WebDriverWait(driver,20).until(EC.element_to_be_clickable(no)).click()
WebDriverWait(driver,60).until(EC.element_to_be_clickable(myuploads)).click()
sleep(30)
WebDriverWait(driver,120).until(EC.element_to_be_clickable(stem)).click()
sleep(2)
WebDriverWait(driver,60).until(EC.element_to_be_clickable(bass)).click()
sleep(2)
WebDriverWait(driver,60).until(EC.element_to_be_clickable(drums)).click()
sleep(2)
WebDriverWait(driver,60).until(EC.element_to_be_clickable(piano)).click()
sleep(2)
WebDriverWait(driver,60).until(EC.element_to_be_clickable(vocals)).click()
sleep(2)


