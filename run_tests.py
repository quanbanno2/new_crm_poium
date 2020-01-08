# coding=utf-8
import os
import time
import pytest
import click
import smtplib
import zipfile
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from conftest import REPORT_DIR
from conftest import cases_path, rerun, todayDate, mail_host, mail_pass, mail_user, sender, receivers

'''
说明：
1、用例创建原则，测试文件名必须以“test”开头，测试函数必须以“test”开头。
2、运行方式：
  > python3 run_tests.py  (回归模式，生成HTML报告)
  > python3 run_tests.py -m debug  (调试模式)
'''


def init_env(now_time):
    """
    初始化测试报告目录
    """
    os.mkdir(REPORT_DIR + now_time)
    # os.mkdir(REPORT_DIR + now_time + "/image")


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


def zip_file(src_dir):
    """
    压缩文件
    @param src_dir:
    @return:返回压缩文件的路径
    """
    zip_name = src_dir + '.zip'
    z = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    for dir_path, dir_names, file_names in os.walk(src_dir):
        fpath = dir_path.replace(src_dir, '')
        fpath = fpath and fpath + os.sep or ''
        for filename in file_names:
            z.write(os.path.join(dir_path, filename), fpath + filename)
            # print('==压缩成功==')
    z.close()
    return zip_name


@click.command()
@click.option('-m', default=None, help='输入运行模式：run 或 debug.')
def run(m):
    if m is None or m == "run":
        print("回归模式，执行完成生成测试结果")
        now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
        init_env(now_time)
        html_report = os.path.join(REPORT_DIR, now_time, "report.html")
        xml_report = os.path.join(REPORT_DIR, now_time, "junit-xml.xml")
        report_file_dir_path = os.path.join(REPORT_DIR, now_time)
        pytest.main(["-s", "-v", cases_path,
                     "--html=" + html_report,
                     "--junit-xml=" + xml_report,
                     "--self-contained-html",
                     "--reruns", rerun])
        # 压缩生成完的报告
        report_zip = zip_file(report_file_dir_path)
        # 发送压缩后的报告
        send_mail(report_zip, now_time)
    elif m == "debug":
        print("debug模式运行测试用例：")
        pytest.main(["-v", "-s", cases_path])
        print("运行结束！！")


if __name__ == '__main__':
    run()
