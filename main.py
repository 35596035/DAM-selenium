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
# pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\USER\Documents\Python Scripts\DAM-selenium\python_tesseract\\tesseract.exe"

#packet file
from AutoTestPage.fn_LogIn import LogIn_Page

driver = webdriver.Chrome()
driver.get("https://192.168.15.141:32000/tw/#")

driver.maximize_window()
action = ActionChains(driver)

LogIn = LogIn_Page(driver, action)
LogIn.GoogleSafe_page()
LogIn.DAM_LogInPage()


img_Name = "DAM_captcha.png"
LogIn.get_captcha(img_Name)
# i = LogIn.ImgNum(img_Name)
# print(i)
LogIn.Input_Num(LogIn.ImgNum(img_Name))

LogIn.CheckLogIn(img_Name)

driver.quit()

#test notebook add branch text
#test home add branch txt


print("測試結束")
os._exit(0)