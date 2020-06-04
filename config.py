import datetime

from conftest import BASE_DIR

# 配置请求url
CRM_REQ_URL = "http://gaofenyun.com:8073/crm-web/customer/"
# 测试数据目录
DATA_DIR = BASE_DIR + "/test_case/data/"
# 当前日期
todayDate = (datetime.datetime.now() + datetime.timedelta(hours=0)).strftime("%Y/%m/%d")
# 当前时间
nowTime = (datetime.datetime.now() + datetime.timedelta(hours=0)).strftime("%Y/%m/%d %H:%M:%S")
# 当前时间+1天
nextDay = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y/%m/%d %H:%M:%S")
# 当前时间+1小时
nextTime = (datetime.datetime.now() + datetime.timedelta(hours=1)).strftime("%Y/%m/%d %H:%M:%S")


class mail_config:
    """
    配置登录和服务器信息、发送人、接收人
    """
    mail_host = "smtp.quanlangedu.com"
    mail_user = "fengjiahui@quanlangedu.com"
    mail_pass = "FJh011310"
    sender = "fengjiahui@quanlangedu.com"
    receivers = "fengjiahui@quanlangedu.com"
