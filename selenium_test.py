# -*- coding: utf-8 -*-
import base64

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import win32api
import win32con
import unittest, time, re
import os


class HttpsWwwMetarthunterComModelEmilyBloom(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_https_www_metarthunter_com_model_emily_bloom(self):
        driver = self.driver
        driver.get("https://www.metarthunter.com/model/emily-bloom/")
        print("step 1")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Emily Bloom'])[2]/following::img[1]").click()
        print("step 2")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Silk Stockings'])[1]/following::img[1]").click()
        print("step 3")
        time.sleep(1)


        #以下部分保存单张图片
        xpath = '//html/body/div/div/div/div/div/img'
        obj = driver.find_element_by_xpath(xpath)
        self.picSave(obj,driver)
        #self.printPic(obj.screenshot_as_base64)
        print(driver.find_element_by_xpath(xpath))
        driver.find_element_by_xpath(xpath).click();

        #切换到下一张图片


        #停止关闭浏览器的行为，方便调试
        print("step 4")
        time.sleep(1000)
        #driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Stop'])[1]/following::img[1]").click()

    def printPic(self,str):
        imgdata = base64.b64decode(str)
        file = open('1.jpg', 'wb')
        file.write(imgdata)
        file.close()


    def picSave(self,obj,driver):
        action = ActionChains(driver).move_to_element(obj)
        action.context_click(obj)
        #先把这个右键的动作调出来
        action.perform()

        time.sleep(1)
        # 按下K键,这里用到了win32api,win32con
        win32api.keybd_event(86, win32con.KEYEVENTF_KEYUP, 0)
        os.system('xx.exe E:\PIC\Ptest.jpg')

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
