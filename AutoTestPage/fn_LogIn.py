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
    
    def DAM_LogInPage(self):
        #count
        ele = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/form/div/div[1]/div/div/input")
        self.action.click(ele).send_keys("william.chiu@dataisec.com").perform()
        time.sleep(2)
        #password
        ele = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/form/div/div[2]/div/div/input")
        self.action.click(ele).send_keys("Admin@123@D").perform()
        time.sleep(2)

    def get_captcha(self, path):
        element = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/form/div/div[3]/img")
        self.driver.save_screenshot(path)  # 先將目前的 screen 存起來
        location = element.location  # 取得圖片 element 的位置
        size = element.size  # 取得圖片 element 的大小
        left = location['x'] + 130  # 決定上下左右邊界
        top = location['y'] + 95
        right = location['x'] + size['width'] + 230
        bottom = location['y'] + size['height'] + 120
        image = Image.open(path)  # 將 screen load 至 memory
        image = image.crop((left, top, right, bottom))  # 根據位置剪裁圖片
        image.save(path, 'png')  # 重新儲存圖片為 png 格式
        time.sleep(3)

    # 圖片辨識
    def ImgNum(self, path):
        img = Image.open(path)
        result = pytesseract.image_to_string(img)
        print("驗證碼:{:}".format(result))
        return result

    # 驗證碼輸入框
    def Input_Num(self, ImgNum):
        ele = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/form/div/div[3]/div/div/div/input")
        self.action.click(ele).send_keys(ImgNum).perform()
        time.sleep(2)