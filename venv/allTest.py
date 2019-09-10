#coding=utf-8

import HTMLTestRunner
import unittest
import os,time

lista = "C:\\Users\lizonghao\PycharmProjects\\untitled2\\venv"

def createsuite():
    testunit = unittest.TestSuite()#充当一个容器
    #找到指定目录lista下的测试模块
    discover = unittest.defaultTestLoader.discover(lista,pattern="myUnitTest.py",top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit

now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
filename = "C:\\Users\\lizonghao\\Documents\\report\\"+now+"_result.html"
fp = open(filename,"wb")

runner = HTMLTestRunner.HTMLTestRunner(
    stream = fp,
    title = u"页面检查报告",
   )

runner.run(createsuite())

#关闭文件流
fp.close()
