import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from conftest import todayDate, mail_host, mail_pass, mail_user, sender, receivers


def send_mail(filename, now_time):
    """
    发送邮件
    @param now_time:
    @param filename:
    @return:
    """
    content = MIMEText("\nhello all："
                       "\n本邮件为系统自动发送，请勿回复。"
                       "\n谢谢！", 'plain', 'utf-8')
    att = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    # 解决文件名乱码
    att.add_header('Content-Disposition', 'attachment', filename=('gbk', '', "%s测试报告.zip" % now_time))
    # 附件实例
    msgRoot = MIMEMultipart()
    msgRoot['From'] = Header(sender, 'utf-8')
    msgRoot['To'] = receivers
    msgRoot['Subject'] = "%s 的UI自动化测试报告！" % todayDate
    # 添加内容
    msgRoot.attach(content)
    # 添加附件
    msgRoot.attach(att)
    smtp = smtplib.SMTP()
    smtp.connect(mail_host)
    smtp.login(mail_user, mail_pass)
    try:
        # 支持多个人接收
        smtp.sendmail(sender, receivers.split(","), msgRoot.as_string())
        print("测试报告发送成功")
    except smtplib.SMTPException:
        print("测试报告发送失败")
    smtp.quit()
