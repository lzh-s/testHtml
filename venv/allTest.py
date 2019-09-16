#coding=utf-8

import HTMLTestRunner
import unittest
import os,time
from sendEmail import Email
from myUnitTest import myUnitTest


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

#邮件发送报告
email_host = "smtp.163.com"
host_port = 465
from_addr = "bjlizonghao@163.com"
pwd = "lzh123"

#获取最新生成的测试报告
result_dir = r"C:\\Users\\lizonghao\\Documents\\report"
lists = os.listdir(result_dir)
#将目录下的文件排序
lists.sort()
#找到最新生成的文件
file_new = os.path.join(lists[-1])
source_path = result_dir+"\\"+file_new

to_addr_list = ["895041787@qq.com"]
email_content = "这是本次自动化测试报告,请查收！"
email_content_html = "test"
email_subject = "手机网易网自动化测试报告"
email_from = "zonghaoli"
part_name = "test_3g.163.com.html"

email_obj = Email.get_email_obj(email_subject,email_from,to_addr_list)
Email.attach_content(email_obj,email_content)
Email.attach_part(email_obj,source_path,part_name)
Email.send_email(email_obj,email_host,host_port,from_addr,pwd,to_addr_list)

