import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys   #键盘操作
from webdriver.support.ui import WebDriverWait #等待
from selenium.webdriver.support import expected_conditions #预期条件类
from selenium.webdriver.common.by import By   #为了等待定位元素

class testa(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://101.1.0.30:9443/#/")
        self.driver.find_element_by_xpath('//*[@id="username"]').click()
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys("admin@0525")
        self.driver.find_element_by_xpath('//*[@id="password"]').click()
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456aA")
        self.driver.find_element_by_xpath('//*[@id="smspin"]').click()
        self.driver.find_element_by_xpath('//*[@id="smspin"]').send_keys("100000")
        self.driver.find_element_by_xpath('//*[@id="btnLogin"]').click()
        time.sleep(10)


    def test1(self):

        self.driver.find_element_by_xpath('/html/body/ui-view/div/aside/section/ul/li[1]/a/div').click()

        if self.driver.find_element_by_xpath('/html/body/ui-view/div/div/section[2]/ui-view/div/div/div[2]/div/div[2]/div[1]/div[1]'):
            flag=True
        else:
            flag=False
        self.assertTrue(flag)


    def test2(self):
        self.driver.find_element_by_xpath('/html/body/ui-view/div/aside/section/ul/li[2]/a/div').click()
        if self.driver.find_element_by_xpath('/html/body/ui-view/div/aside/section/ul/li[2]/ul/li[1]/a'):
            flag2=True
        else:
             flag2=False
        self.assertTrue(flag2)
        #self.assertEqual(user,"用户列表")

    def test3(self):
        self.driver.find_element_by_xpath('/html/body/ui-view/div/aside/section/ul/li[7]/a').click()
        self.driver.find_element_by_xpath('/html/body/ui-view/div/aside/section/ul/li[7]/ul/li[5]/a').click()
        self.driver.find_element_by_xpath('/html/body/ui-view/div/div/section[2]/ui-view/div/form/input').click()
        self.driver.find_element_by_xpath('/html/body/ui-view/div/div/section[2]/ui-view/div/form/input').send_keys(Keys.ENTER)
        time.sleep(5)
        if self.driver.find_element_by_xpath('//*[@id="titleBar"]/div/div/div[1]/span[2]'):
            flag3=True
        else:
            flag3=False
        #self.driver.save_screenshot("E:\\A\\B\\C\\ddd.png")#到底能不能加啊！！！！！！！！！
        self.assertTrue(flag3)


    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        print("the end of the testhahahahahahha")

if __name__=="__main__":
    unittest.main()
