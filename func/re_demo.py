import re


def re_demo(context):
    """
    提取数字（小数）
    @param context:
    @return:
    """
    result = re.search("\d+(\.\d+)?", context)
    return result.group()
