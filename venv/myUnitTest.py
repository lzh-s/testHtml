import unittest
import requests
from selenium import webdriver
import time,os

class myUnitTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)#隐形等待时间为5秒
        self.url = "https://3g.163.com/news"

    def get_status(url):
        r = requests.get(url, verify=False)  # 将证书关闭
        return r.status_code

    def test_html(self):
        u"""检查页面"""
        driver = self.driver
        driver.get(self.url+"/")

        time.sleep(3)
        title = driver.title
        self.get_status()

    def tearDown(self):
         self.driver.quit()

if __name__== "__main__":
     unittest.main()

