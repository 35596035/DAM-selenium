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

class LogIn_Page:
    def __init__(self, driver, action):
        self.driver = driver
        self.action = action
    def GoogleSafe_page(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="details-button"]')
        self.action.click(ele).perform()

        ele = self.driver.find_element(By.XPATH, '//*[@id="proceed-link"]')
        self.action.click(ele).perform()

        time.sleep(3)