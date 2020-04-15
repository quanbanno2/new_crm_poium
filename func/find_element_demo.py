# from selenium import webdriver
# from time import sleep


def by_xpath_contains(driver, tag, context, context_2=None):
    """
    根据元素包含文字进行定位
    @param tag:
    @param driver:
    @param context:包含的文字
    @param context_2:xpath定位语法辅助定位
    @return:
    """
    if context_2 is None:
        return driver.find_element_by_xpath("//%s[contains(.,'%s')]" % (tag, context))
    else:
        return driver.find_element_by_xpath("//%s[contains(.,'%s') and %s]" % (tag, context, context_2))

#
# wd = webdriver.Chrome()
# wd.get("https://www.baidu.com")
#
# by_xpath_contains(wd, "抗击肺炎", "@id=\"virus-2020\"").click()
# sleep(5)
# wd.close()
