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
import cv2
import numpy as np
import ddddocr

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
        left = location['x']                  # 決定上下左右邊界
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        #left = location['x'] + 130  # 決定上下左右邊界
        #top = location['y'] + 95
        #right = location['x'] + size['width'] + 230
        #bottom = location['y'] + size['height'] + 120
        image = Image.open(path)  # 將 screen load 至 memory
        image = image.crop((left, top, right, bottom))  # 根據位置剪裁圖片
        image.save(path, 'png')  # 重新儲存圖片為 png 格式
        time.sleep(3)

    # 圖片辨識
    def ImgNum(self, path):
        # ddddocr 套件辨識
        ocr = ddddocr.DdddOcr()
        img = Image.open(path)
        # gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
        # _, threshold = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
        # noise = np.random.normal(0, 15, threshold.shape)
        # noise = np.clip(threshold +noise, 0, 255).astype('uint8')
        # guassian = cv2.blur(noise, (3, 3))        
        # img = Image.fromarray(guassian)

        # pytesseract 套件辨識
        # image = cv2.imread(path)
        # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # # 二值化处理 (自适应阈值处理)
        # thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

        # # 可选去噪处理（腐蚀与膨胀）
        # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
        # processed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

        # # 显示处理后的图像（可选，用于调试）
        # processed = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # pil_image = Image.fromarray(processed)
        # pil_image.save("gray.png", 'png')
        # result = pytesseract.image_to_string(pil_image)
        # print("pytess:",result)

        return ocr.classification(img)

    # 驗證碼輸入框
    def Input_Num(self, ImgNum):
        ele = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/form/div/div[3]/div/div/div/input")
        self.action.click(ele).send_keys(ImgNum).perform()
        time.sleep(2)

        ele = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/form/div/button/span")
        self.action.click(ele).perform()
        time.sleep(2)

    
    def Check_User_ele(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div/header/div/button/div/img")
        self.driver.save_screenshot('LogInHomePage.png')

    def CheckLogIn(self, path):
        while True:
            try:
                self.Check_User_ele()
                break
            except:
                ele = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/form/div/button/span")
                self.action.click(ele).perform()
                print("驗證碼判定錯誤")
                time.sleep(2)
                # 帳號密碼輸入
                self.DAM_LogInPage()
                # 取得驗證碼圖片
                self.get_captcha(path)
                # 驗證碼判定&輸入
                self.Input_Num(self.ImgNum(path))