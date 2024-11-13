# selenium 相關套件
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
# 時間,io相關套件使用
import time
import os
import io
# 畫面切割/分割/儲存/開啟
from PIL import Image
# 圖片驗證碼
import pytesseract

driver = webdriver.Chrome()
driver.get("https://192.168.15.141:32000/tw/#")

driver.maximize_window()
action = ActionChains(driver)

#Google 安全驗證
ele = self.driver.find_element(By.XPATH, '//*[@id="details-button"]')
self.action.click(ele).perform()

ele = self.driver.find_element(By.XPATH, '//*[@id="proceed-link"]')
self.action.click(ele).perform()

#登入畫面
ele = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[3]/div[1]/input")
self.action.click(ele).send_keys("aegIS@123").perform()
