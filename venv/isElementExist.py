def is_element_exist(css):
    s = driver.find_elements_by_css_selector(css_selector=css)
    if len(s) == 0:
        print("元素未找到：%s" % css + ",请检查页面！")
        return False
    elif len(s) == 1:
        return True
    else:
        print("找到%s个元素：%s" % (len(s), css) + "，页面显示正常。")
        return False


 # 判断页面上有无div标签
if is_element_exist("div"):
            driver.find_element_by_tag_name("div").send_keys("163")
 # 判断页面上是否有calss为video-list的元素
# if is_element_exist("video-list"):
#      driver.find_element_by_class_name("video-list").send_keys("163")
 # 判断页面是否有无标签为h3的元素
if is_element_exist("h3"):
            driver.find_element_by_tag_name("h3").send_keys("163")
 # 判断页面上是否有img
if is_element_exist("img"):
            driver.find_element_by_tag_name("img").send_keys("163")

if status == 200:
             print(status, "Success")
else:
             print(status, "False")

    # 捕获异常
def isElementExit(css):
    try:
        driver.find_elements_by_css_selector(css)
        return True
    except:
        return False
