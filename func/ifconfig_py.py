import platform
import os
import re


def ipconfig():
    """
    获取本机内网ip地址
    @return:
    """
    data = []
    if platform.system() == "Windows":
        ip = os.popen("chcp 65001&&ipconfig").read()
        res = re.findall('IPv4 Address.*?: (.*?)\n.*?Subnet Mask.*?: (.*?)\n', ip)
        for i in range(len(res)):
            for j in res[i]:
                data.append(j)
        return data[2]
    else:
        ip = os.popen("ifconfig").read()
        res = re.findall('inet (.*?) netmask (.*?) ', ip)
        for i in range(len(res)):
            for j in res[i]:
                data.append(j)
        return data[2]
