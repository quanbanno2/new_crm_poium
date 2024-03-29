def by_xpath_contains(driver, tag, context, context_2=None, tag_2="."):
    """
    根据元素包含文字进行定位
    @param tag_2:
    @param tag:
    @param driver:
    @param context:包含的文字
    @param context_2:xpath定位语法辅助定位
    @return:
    """
    if context_2 is None:
        return driver.find_element_by_xpath("//{}[contains({},'{}')]".format(tag, tag_2, context))
    else:
        return driver.find_element_by_xpath("//{}[contains({},'{}') and {}]".format(tag, tag_2, context, context_2))


def find_order_pay_info(driver, context):
    """
    订单详情-缴费信息（缴费编号、应收、预收、已缴、未交等）
    @param driver:
    @param context:
    @return:
    """
    return driver.find_element_by_xpath("//th[text()='{}']/following-sibling::td/span".format(context))


class find_object_element:

    def __init__(self, driver):
        self.driver = driver

    # 根据id查找退费按钮
    def find_confirm_refund_button(self, order_id):
        return self.driver.find_element_by_xpath("//a[text()='{}']/following::td[10]/button[4]".format(order_id))

    # 根据对象内容获取退费业绩
    def find_object_refund_fee(self, objects):
        return self.driver.find_element_by_xpath("//span[text()='{}']/following::td[4]/span".format(objects))

    # 根据订单课程id找到换课按钮
    def find_course_change_class(self, order_course_id):
        return self.driver.find_element_by_xpath(
            "//td[text()='{}']/following::td[14]/button[5]".format(order_course_id))

    # 根据订单id找到当前班级
    def find_course_class(self, order_course_id):
        return self.driver.find_element_by_xpath("//td[text()='{}']/following::td[4]".format(order_course_id))
