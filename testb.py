import unittest
from selenium import webdriver
import time

class testb(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')

    def test4(self):
        self.driver.find_element_by_xpath('//*[@id="kw"]').click()
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys('傻逼')
        self.driver.find_element_by_xpath('//*[@id="su"]').click()
        time.sleep(3)
        if self.driver.find_element_by_xpath('//*[@id="2"]/h3/a'):
            flag4=True
        else:
            flag4=False
        self.assertTrue(flag4)

    def test5(self):
        self.assertEqual(1,1)

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()

