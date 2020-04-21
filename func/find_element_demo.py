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


def find_order_pay_info(driver, context):
    """
    订单详情-缴费信息（缴费编号、应收、预收、已缴、未交等）
    @param driver:
    @param context:
    @return:
    """
    return driver.find_element_by_xpath("//th[text()='%s']/following-sibling::td/span" % context)
