import os
import pytest
import datetime
from py.xml import html
from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as CH_Options
from selenium.webdriver.firefox.options import Options as FF_Options

# 项目目录配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = BASE_DIR + "/test_report/"
DATA_DIR = BASE_DIR + "/test_case/data/"

# conftest配置文件每次启动初始化一次

############################

# 配置浏览器驱动类型(chrome/firefox/chrome-headless/firefox-headless)。
# driver_type = "chrome"
# driver_type = "safari"
driver_type = "grid"

# 失败重跑次数
rerun = "1"

# 运行测试用例的目录或文件
cases_path = "test_case/"

# 配置运行的 URL
crmUrl = "http://gaofenyun.com:8073/crm-web/login.html"

# 配置测试客户问题
question = "测试问题1"

# 测试课程名称
course_name = "自动化专用语文培优次课"

# 辅导老师
adviserName = '辅导1'
adviserAccount = '高分云辅导1'

# 高分云辅导2
adviserName2 = '辅导2'
adviserAccount2 = '高分云辅导2'

# 指导老师
educationName = '指导1'
educationAccount = '高分云指导1'

# 教务老师
educationalAccount = "高分云教务1"
educationalName = "教务1"

# 手机号
phoneNumber = '13437829328'

# 指导督导登录账号
supervisorAccount = "高分云指导督导1"

# 高分云辅导督导1账号
counselingSupervisorAccount = "高分云辅导督导1"
counselingSupervisorName = "辅导督导1"

# 密码
password = '123456'

# 备注内容
remark = "这是备注内容。"

# # 新增订单学员名称
# stu_name = "自动化测试专用学员"

# 测试班级名称（班主任：高分云指导1，初一）
className = "测试自动化专用班级"

# 补课用班级名称（班主任：高分云指导1，初一）
makeUpClass = "自动化测试补课班"

# 高分云校区
xiaoqu_schoolName = "高分云"

# 客户生日
customerBirthday = "1991/10/25"

# 补课时间-当前时间加1小时
makeUpTime = (datetime.datetime.now() + datetime.timedelta(hours=1)).strftime("%Y/%m/%d %H:%M:%S")

# 获取当前时间加一天的时间
nextDate = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y/%m/%d %H:%M:%S")

# 上课时间/请假时间-当前时间
inClassTime = (datetime.datetime.now() + datetime.timedelta(hours=0)).strftime("%Y/%m/%d %H:%M:%S")

# 今天日期
todayDate = (datetime.datetime.now() + datetime.timedelta(hours=0)).strftime("%Y/%m/%d")

# 学员姓名
studentName = "自动化测试学生"

# 人事助理账号&名称
humanResourceAccount = "高分云人事1"
humanResourceName = "人事1"

# 登录和服务器信息、发送人、接收人
mail_host = "smtp.quanlangedu.com"
mail_user = "fengjiahui@quanlangedu.com"
mail_pass = "FJh011310"
sender = "fengjiahui@quanlangedu.com"
receivers = "fengjiahui@quanlangedu.com"


############################

@pytest.fixture(scope='session')
def date_today():
    in_class_time = (datetime.datetime.now() + datetime.timedelta(hours=0)).strftime("%Y/%m/%d %H:%M:%S")
    return in_class_time


# 定义基本测试环境


@pytest.fixture(scope='function')
def crm_url():
    global crmUrl
    return crmUrl


@pytest.fixture(scope='function')
def cases_pathh():
    global cases_path
    return cases_path


@pytest.fixture(scope='function')
def questions():
    global question
    return question


@pytest.fixture(scope='function')
def phone_number():
    global phoneNumber
    return phoneNumber


@pytest.fixture(scope='function')
def course():
    global course_name
    return course_name


# 辅导1老师名称
@pytest.fixture(scope='function')
def adviser_name():
    global adviserName
    return adviserName


# 辅导2老师名称
@pytest.fixture(scope='function')
def adviser_name2():
    global adviserName2
    return adviserName2


# 辅导1老师账号
@pytest.fixture(scope='function')
def adviser_account():
    global adviserAccount
    return adviserAccount


# 辅导2老师账号
@pytest.fixture(scope='function')
def adviser_account2():
    global adviserAccount2
    return adviserAccount2


# 登录密码
@pytest.fixture(scope='function')
def pass_word():
    global password
    return password


# 备注
@pytest.fixture(scope='function')
def remarks():
    global remark
    return remark


# 督导登录账号
@pytest.fixture(scope='function')
def supervisor_account():
    global supervisorAccount
    return supervisorAccount


# # 新增订单专用学员账号
# @pytest.fixture(scope='function')
# def student_name():
#     global stu_name
#     return stu_name


# 测试用班级名称
@pytest.fixture(scope='function')
def class_name():
    global className
    return className


# 指导老师名称
@pytest.fixture(scope='function')
def education_name():
    global educationName
    return educationName


# 指导老师账号
@pytest.fixture(scope='function')
def education_account():
    global educationAccount
    return educationAccount


# 教务老师名称
@pytest.fixture(scope='function')
def educational_name():
    global educationalName
    return educationalName


# 教务老师账号
@pytest.fixture(scope='function')
def educational_account():
    global educationalAccount
    return educationalAccount


# 高分云校区
@pytest.fixture(scope='function')
def jigou_school_name():
    global xiaoqu_schoolName
    return xiaoqu_schoolName


# 客户生日
@pytest.fixture(scope='function')
def customer_birthday():
    global customerBirthday
    return customerBirthday


# 补课时间
@pytest.fixture(scope='function')
def make_up_time():
    global makeUpTime
    return makeUpTime


@pytest.fixture(scope='function')
def next_date():
    global nextDate
    return nextDate


# 上课时间
@pytest.fixture(scope='function')
def in_class_time():
    global inClassTime
    return inClassTime


# 返回今天日期
@pytest.fixture(scope='function')
def today_date():
    global todayDate
    return todayDate


# 学员姓名
@pytest.fixture(scope='function')
def student_name():
    global studentName
    return studentName


# 补课班级名称
@pytest.fixture(scope='function')
def make_up_class():
    global makeUpClass
    return makeUpClass


# 高分云辅导督导1账号
@pytest.fixture(scope='function')
def counseling_supervision_account():
    global counselingSupervisorAccount
    return counselingSupervisorAccount


# 高分云辅导督导1名称
@pytest.fixture(scope='function')
def counseling_supervision_name():
    global counselingSupervisorName
    return counselingSupervisorName


# 高分云人事1账号
@pytest.fixture(scope='function')
def human_resource_account():
    global humanResourceAccount
    return humanResourceAccount


#####################

# 设置用例描述表头
@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.pop()


# 设置用例描述表格
@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.pop()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    用于向测试用例中添加用例的开始时间、内部注释，和失败截图等.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    report.description = description_html(item.function.__doc__)
    # 测试报告的test中的汉字转码
    nodeID = report.nodeid
    report.nodeid = nodeID.encode('utf-8').decode('unicode_escape')
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            case_path = report.nodeid.replace("::", "_") + ".png"
            if "[" in case_path:
                case_name = case_path.split("-")[0] + "].png"
            else:
                case_name = case_path
            capture_screenshot(case_name)
            # img_path = "image/" + case_name.split("/")[-1]
            img_path = case_name.split("/")[-1]
            if img_path:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % img_path
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def description_html(desc):
    """
    将用例中的描述转成HTML对象
    :param desc: 描述
    :return:
    """
    if desc is None:
        return "No case description"
    desc_ = ""
    for i in range(len(desc)):
        if i == 0:
            pass
        elif desc[i] == '\n':
            desc_ = desc_ + ";"
        else:
            desc_ = desc_ + desc[i]

    desc_lines = desc_.split(";")
    desc_html = html.html(
        html.head(
            html.meta(name="Content-Type", value="text/html; charset=latin1")),
        html.body(
            [html.p(line) for line in desc_lines]))
    return desc_html


# def capture_screenshot(case_name):
#     """
#     配置用例失败截图路径
#     :param case_name: 用例名
#     :return:
#     """
#     global driver
#     file_name = case_name.split("/")[-1]
#     new_report_dir = new_report_time()
#     if new_report_dir is None:
#         raise RuntimeError('没有初始化测试目录')
#     image_dir = os.path.join(REPORT_DIR, new_report_dir, "image", file_name)
#     print(image_dir)
#     driver.save_screenshot(image_dir)

def capture_screenshot(case_name):
    """
    配置用例失败截图路径
    :param case_name: 用例名
    :return:
    """
    global driver
    file_name = case_name.split("/")[-1]
    new_report_dir = new_report_time()
    if new_report_dir is None:
        raise RuntimeError('没有初始化测试目录')
    image_dir = os.path.join(REPORT_DIR, new_report_dir, file_name)
    driver.save_screenshot(image_dir)


def new_report_time():
    """
    获取最新报告的目录名（即运行时间，例如：2018_11_21_17_40_44）
    """
    files = os.listdir(REPORT_DIR)
    files.sort()
    try:
        return files[-1]
    except IndexError:
        return None


# 启动浏览器
@pytest.fixture(scope='session', autouse=True)
def browser1():
    """
    全局定义浏览器驱动
    :return:
    """
    global driver
    global driver_type

    if driver_type == "chrome":
        # 本地chrome浏览器
        driver = webdriver.Chrome()
        # driver.set_window_size(1920, 1080)
        driver.maximize_window()

    elif driver_type == "firefox":
        # 本地firefox浏览器
        driver = webdriver.Firefox()
        # driver.set_window_size(1920, 1080)
        driver.maximize_window()

    elif driver_type == "safari":
        driver = webdriver.Safari()
        driver.maximize_window()

    elif driver_type == "chrome-headless":
        # chrome headless模式
        chrome_options = CH_Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(options=chrome_options)

    elif driver_type == "firefox-headless":
        # firefox headless模式
        firefox_options = FF_Options()
        firefox_options.headless = True
        driver = webdriver.Firefox(firefox_options=firefox_options)

    elif driver_type == "grid":
        # 通过远程节点运行  command_executor远程节点地址
        driver = Remote(command_executor='http://192.168.0.51:5555/wd/hub',
                        desired_capabilities={
                            "browserName": "chrome",
                        })
        driver.maximize_window()

    else:
        raise NameError("driver驱动类型定义错误！")

    return driver


# 关闭浏览器
@pytest.fixture(scope="session", autouse=True)
def browser_close():
    yield driver
    driver.quit()
    print("\n\ntest end!")


if __name__ == "__main__":
    capture_screenshot("test_case/test_baidu_search.test_search_python.png")
