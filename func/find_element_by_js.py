class find_js_element:
    @staticmethod
    def remove_attribute(attribute):
        """
        移除元素的指定属性值
        @param attribute:
        @return:
        """
        js = 'arguments[0].removeAttribute(\"{}\")'.format(attribute)
        return js
