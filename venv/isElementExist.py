class isElementExist(object):
 def __init__(self,css,url):
     self.css = css
     self.url = url

 def get_status(self):
     r = requests.get(self.url, verify=False)  # 将证书关闭
     return r.status_code

 def is_element_exist(self):
    s = driver.find_elements_by_css_selector(css_selector=self.css)
    if len(s) == 0:
        print("元素未找到：%s" % css + ",请检查页面！")
        return False
    elif len(s) == 1:
        return True
    else:
        print("找到%s个元素：%s" % (len(s), css) + "，页面显示正常。")
        return False



     # 捕获异常
 def isElementExit(css):
     try:
        driver.find_elements_by_css_selector(css)
        return True
     except:
        return False
