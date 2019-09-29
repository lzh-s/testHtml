import unittest
import requests
from selenium import webdriver
import time,os
#from untitled2.venv.isElementExist import isElementExist

class myUnitTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)#隐形等待时间为5秒

    def check_status(self,url):
        u"""页面状态"""
        r = requests.get(url,verify=False)#关闭证书验证
        if r.status_code == 200:
            print(r.status_code, "Success")
            return True
        else:
            print(r.status_code, "False")
            return False

    def check_html(self,url):
        u"""检查页面"""
        driver = self.driver
        driver.get(url)
        time.sleep(3)
        title = driver.title

        #检查页面div元素
        s = self.driver.find_elements_by_css_selector(css_selector="div")
        #检查页面h3元素
        q = self.driver.find_elements_by_css_selector(css_selector="h3")
        #检查页面img元素
        u = self.driver.find_elements_by_css_selector(css_selector="img")

        #判断页面所有元素是否为空
        if len(s) == 0 or len(q) == 0 or len(u) == 0:
            return False
        #判断页面元素个数为1
        elif len(s) == 1 or len(q) == 1 or len(u) == 1:
            return True
        #判断页面h3元素为空时，是否存在img元素
        elif len(q) == 0 and len(u) != 0:
            return False
        #其他情况
        else:
            return False

    def tearDown(self):
         self.driver.quit()

    @staticmethod
    def getUrlFunc(url):
        def func(self):
            self.check_status(url)
            self.check_html(url)
        return func

def __generateTestCases():
    file_handle = open("urlText.txt", mode="r")

    try:
        urllists = file_handle.readlines()
        for urls in urllists:
           url = urls.strip("\n")
           setattr(myUnitTest,"test_func_%s" % (url),myUnitTest.getUrlFunc(url))
    finally:
        #driver.close()  # 执行结束后关闭页面
         file_handle.close()
__generateTestCases()



if __name__== "__main__":
     unittest.main()

