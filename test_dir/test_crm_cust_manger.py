import sys
import pytest
import pymysql
from time import sleep
from os.path import dirname, abspath
from page.crm_cust_manger_page import GfyCrmCustomerManagement, GfyCustomerAddOrder
from page.crm_home_page import GfyHomePage
from page.crm_menu_page import GfyMenu
from page.crm_finance_page import GfyRefundInfo
from page.crm_login_page import GfyLogin
from poium import PageWait, PageSelect
from _pydecimal import Context, ROUND_HALF_UP

sys.path.insert(0, dirname(dirname(abspath(__file__))))


def new_student_name():
    """
    连接集成数据库得出客户***,返回集成数据库最新"客户"***+1的名称
    :return:
    """
    customer_name = []
    db = pymysql.connect('rm-wz9ex1m8zw6c8ui55o.mysql.rds.aliyuncs.com',
                         'edu_test_user',
                         'Quanlang_edu_test')
    cursor = db.cursor()
    sql = 'SELECT cust_name FROM test_customer.cust_info ' \
          'WHERE cust_id = (SELECT MAX(cust_id) ' \
          'FROM test_customer.cust_info WHERE cust_name LIKE "客户%" AND cust_status="S01")'
    cursor.execute(sql)
    result = cursor.fetchall()
    for re in result:
        customer_name = re[0]
    # 读取客户名称后的数字
    a = customer_name[2:]
    client_num = int(a)
    client_num = client_num + 1
    client_name = "客户" + str(client_num)
    db.close()
    return client_name


def login(url, driver, account, password):
    """
    系统登录
    :param url:
    :param driver:
    :param account:
    :param password:
    :return:
    """
    page = GfyLogin(driver)
    page.get(url)
    page.login_input.send_keys(account)
    page.pwd_input.send_keys(password)
    code = page.verification_code.text
    page.code_input.send_keys(code)
    page.enter.click()
    sleep(1)


def add_customer(driver, customer_name, phone_number):
    """
    创建客户：新招生类型
    :param driver:
    :param customer_name:
    :param phone_number:
    :return:
    """
    page = GfyCrmCustomerManagement(driver)
    menu_page = GfyMenu(driver)
    menu_page.customer_management.click()
    menu_page.my_customer.click()
    page.add_customer.click()
    sleep(2)
    page.add_customer_name.send_keys(customer_name)
    page.school_name.click()
    PageWait(page.pub_school_list)
    page.pub_school_list.send_keys("四基初级中学")
    page.pub_school_query.click()
    PageWait(page.pub_school_choice)
    page.pub_school_choice.click()
    PageWait(page.grade)
    PageSelect(page.grade, value='string:G09')
    page.customer_activity.click()
    sleep(1)
    page.activity_name.send_keys('高分云信息单')
    page.activity_query.click()
    sleep(1)
    page.activity_selected.click()
    page.customer_phone.send_keys(phone_number)
    page.add_customer_save.click()


def add_educational(driver, educational_effect_time, educational_account):
    """
    添加教务老师
    :param driver:
    :param educational_effect_time: 教务老师生效时间
    :param educational_account: 教务老师登录账号
    :return:
    """
    page = GfyCrmCustomerManagement(driver)
    menu_page = GfyMenu(driver)
    menu_page.customer_management.click()
    sleep(1)
    menu_page.my_customer.click()
    sleep(1)
    page.first_student_name.click()
    sleep(1)
    page.student_educational.click()
    sleep(1)
    page.student_educational_add.click()
    sleep(1)
    page.educational_account_name.click()
    sleep(1)
    PageSelect(page.teacher_list_school, value="number:24")
    sleep(1)
    PageSelect(page.teacher_attribution_department, text="全部")
    sleep(1)
    page.teacher_list_login_name.send_keys(educational_account)
    sleep(1)
    page.teacher_list_query.click()
    sleep(1)
    page.teacher_select.click()
    sleep(1)
    js = 'document.getElementsByName("effDate")[0].removeAttribute("readonly");'
    driver.execute_script(js)
    sleep(1)
    page.educational_effect_date.send_keys(educational_effect_time)
    sleep(1)
    page.student_educational_save.click()


def split_customer(driver, adviser_account, school_name):
    """
    单个学员分单
    :param driver:
    :param adviser_account:分单目标账号
    :param school_name:校区名称
    :return:
    """
    page = GfyCrmCustomerManagement(driver)
    PageSelect(page.customer_list_school_list, text=school_name)
    sleep(1)
    page.customer_check.click()
    sleep(1)
    page.customer_split.click()
    sleep(1)
    page.teacher_list_login_name.clear()
    sleep(1)
    page.teacher_list_login_name.send_keys(adviser_account)
    sleep(1)
    page.teacher_list_query.click()
    PageWait(page.teacher_select)
    page.teacher_select.click()
    PageWait(page.confirm_split)
    page.confirm_split.click()


def convert_student(driver, school_name):
    """
    单个客户转为学员
    :param driver:
    :param school_name:
    :return:
    """
    page = GfyCrmCustomerManagement(driver)
    PageSelect(page.customer_list_school_list, text=school_name)
    sleep(1)
    page.convert_to_student.click()
    sleep(1)
    page.confirm_btn.click()


def create_account(driver, password, school_name):
    """
    客户详情创建教学帐号绑定
    :param driver:
    :param password:
    :param school_name:
    :return:
    """
    page = GfyCrmCustomerManagement(driver)
    PageSelect(page.customer_list_school_list, text=school_name)
    sleep(1)
    account_name = page.first_student_name.text
    page.first_student_name.click()
    sleep(1)
    page.customer_create_account.click()
    sleep(1)
    page.customer_create_account_btn.click()
    sleep(1)
    page.customer_create_account_name.send_keys(account_name)
    sleep(1)
    page.customer_create_account_password.send_keys(password)
    sleep(1)
    page.customer_create_account_repeat_password.send_keys(password)
    sleep(1)
    page.customer_create_account_birthday.click()
    sleep(1)
    page.customer_create_account_birthday_today.click()
    sleep(1)
    page.customer_create_account_save.click()


def add_new_order(driver, consultant, course_name, school_name):
    """
    客户创建订单
    :param driver:
    :param consultant:分成对象
    :param course_name:
    :param school_name:
    :return:
    """
    customer_page = GfyCrmCustomerManagement(driver)
    order_page = GfyCustomerAddOrder(driver)
    # menu_page = GfyMenu(driver)
    # menu_page.customer_management.click()
    # sleep(1)
    # # menu_page.my_customer.click()
    # sleep(1)
    PageSelect(customer_page.customer_list_school_list, text=school_name)
    sleep(1)
    customer_page.customer_name.click()
    sleep(1)
    order_page.customer_order_info.click()
    sleep(1)
    order_page.customer_order_add.click()
    sleep(1)
    PageSelect(order_page.order_sharing_object_select, text=consultant)
    sleep(1)
    order_page.order_sharing_object_select_btn.click()
    sleep(1)
    order_page.order_select_course.click()
    sleep(1)
    order_page.order_select_course_name.send_keys(course_name)
    sleep(1)
    order_page.order_select_course_name_query.click()
    sleep(1)
    order_page.order_select_course_btn.click()
    sleep(1)
    order_page.order_save_stu_order.click()


def customer_recovery(driver):
    """
    新单招生的客户回收
    :param driver:
    :return: 返回第一位跟进人名称
    """
    # menu_page = GfyMenu(driver)
    # menu_page.customer_management.click()
    # sleep(1)
    # menu_page.my_customer.click()
    customer_page = GfyCrmCustomerManagement(driver)
    sleep(1)
    # 获取第一位跟进人名称
    customer_teacher_name = customer_page.customer_teacher[3].text
    sleep(1)
    # 回收
    customer_page.customer_recovery.click()
    sleep(1)
    customer_page.confirm_btn.click()
    return customer_teacher_name


def pay_new_order(driver):
    """
    新招生单单支付（优惠、支付项、手续费、支付）
    :param driver:
    :return:
    """
    order_page = GfyCustomerAddOrder(driver)
    menu_page = GfyMenu(driver)
    other_page = GfyCrmCustomerManagement(driver)
    sleep(1)
    menu_page.student_management.click()
    sleep(1)
    menu_page.student_order_management.click()
    sleep(1)
    order_page.student_order_pay_btn.click()
    sleep(1)
    # 优惠项
    preferential_amount = cal_preferential_amount(order_page.order_accounts_receivable.text)
    sleep(1)
    order_page.add_order_discount_btn.click()
    sleep(1)
    order_page.add_order_discount_fee.send_keys(preferential_amount)
    sleep(1)
    order_page.add_order_discount_save.click()
    # 支付项
    sleep(1)
    order_page.add_order_pay_btn.click()
    sleep(1)
    order_page.add_order_pay_fee.send_keys(order_page.order_pre_fee.text)
    sleep(1)
    order_page.add_order_pay_save_btn.click()
    # 计算其他费用
    sleep(1)
    service_charge = cal_service_charge(order_page.order_pre_fee.text)
    sleep(1)
    order_page.add_order_other_btn.click()
    sleep(1)
    order_page.add_order_other_fee.send_keys(service_charge)
    sleep(1)
    order_page.add_order_other_save.click()
    sleep(1)
    # 支付
    driver.execute_script("arguments[0].click();", order_page.pay_stu_order)
    sleep(1)
    other_page.confirm_btn.click()


def refund_apply(driver, remarks):
    """
     订单退费
    :param driver:
    :param remarks:
    :return: customer_name 客户名称、order_id_text 订单编号、refund_fee_text 应退费值
    """
    menu_page = GfyMenu(driver)
    order_page = GfyCustomerAddOrder(driver)
    sleep(1)
    menu_page.student_management.click()
    sleep(1)
    menu_page.student_order_management.click()
    sleep(1)
    order_page.order_detail.click()
    sleep(1)
    driver.execute_script("arguments[0].click();", order_page.order_info_refund)
    sleep(1)
    # 获取预收款、订购数量、消耗数量、学员名称、订单编号
    refund_pre_fee_text = order_page.refund_pre_fee.text
    refund_course_count_text = order_page.refund_course_count.text
    refund_course_consume_text = order_page.refund_course_consume.text
    customer_name = order_page.order_customer_name.text
    order_id_text = order_page.order_id.text
    sleep(1)
    order_page.refund_remark.send_keys(remarks)
    sleep(1)
    order_page.save_order_refund.click()
    PageWait(order_page.approval_matter_setting)
    PageSelect(order_page.approval_matter_setting, text="辅导督导1-->通知发起人")
    sleep(1)
    order_page.save_approval_matter.click()
    sleep(1)
    refund_fee_text = cal_refund_fee(refund_pre_fee_text, refund_course_count_text, refund_course_consume_text)
    return customer_name, order_id_text, refund_fee_text


def cal_preferential_amount(charge):
    """
    计算优惠
    :param charge:
    :return:
    """
    preferential_amount = int(int(charge) * 0.1)
    return preferential_amount


def cal_service_charge(charge):
    """
    计算手续费
    :param charge:
    :return:
    """
    service_charge = int(int(charge) * 5 / 1000)
    return service_charge


def cal_refund_fee(pre_fee, course_count, course_consume):
    """
    计算退费结算金额 = 预收 - （预收/课程单价*消耗课程数量）
    :param pre_fee:预收金额
    :param course_count:课程总数量
    :param course_consume:已消耗课程
    :return:
    """
    pre_fee = float(pre_fee)
    course_count = float(course_count)
    course_consume = float(course_consume)
    refund_fee = pre_fee - (pre_fee / course_count * course_consume)
    # 保留两位、四舍五入,以字符串格式返回
    return str(Context(prec=6, rounding=ROUND_HALF_UP).create_decimal(refund_fee))


# def audio_upload(driver, audio_dir):
#     """
#     上传沟通音频
#     :param driver:
#     :param audio_dir:
#     :return:
#     """
#     all_auido = [
#         r'G:\pyautoTest-crm\audio\amr测试.amr',
#         r'G:\pyautoTest-crm\audio\mp3测试.mp3',
#         r'G:\pyautoTest-crm\audio\ogg测试.ogg',
#         r'G:\pyautoTest-crm\audio\wav测试.wav'
#     ]
#     page = CustRecruitStudents(driver)
#     for i in all_auido:
#         sleep(2)
#         page.cust_communicate_select_file.click()
#         sleep(2)
#         cmd = audio_dir + " " + "%s" % i
#         sleep(2)
#         os.system(cmd)


def set_content_by_id(driver, content_id, text):
    """
    文本框输入
    :param driver:
    :param content_id:
    :param text:
    :return:
    """
    js = 'document.getElementById("%s").innerHTML = "%s" ' % (content_id, text)
    driver.execute_script(js)


def set_content_by_name(driver, content_name, text):
    """
    文本框输入
    :param driver:
    :param content_name:
    :param text:
    :return:
    """
    js = 'document.getElementsByName("%s").innerHTML = "%s" ' % (content_name, text)
    driver.execute_script(js)


class TestLogin:

    def test_login(self, crm_url, browser1, pass_word, supervisor_account):
        """
        测试登录
        :param crm_url:
        :param browser1:
        :param pass_word:
        :param supervisor_account:
        :return:
        """
        page = GfyLogin(browser1)
        login(crm_url, browser1, supervisor_account, pass_word)
        PageWait(page.account_name)
        assert page.account_name.text == "高分云指导督导1"


class TestCustomerAdd:
    """
    客户管理模块测试
    """

    def test_add_customer(self, crm_url, browser1, phone_number, pass_word, counseling_supervision_account,
                          school_name):
        """
        测试新增客户：新招生
        :param crm_url:
        :param browser1:
        :param phone_number:
        :param pass_word:
        :param counseling_supervision_account:
        :param school_name:
        :return:
        """
        login(crm_url, browser1, counseling_supervision_account, pass_word)
        student_name = new_student_name()
        add_customer(browser1, student_name, phone_number)
        page = GfyCrmCustomerManagement(browser1)
        PageSelect(page.customer_list_school_list, text=school_name)
        sleep(2)
        assert page.customer_name.text == student_name

    def test_split_customer(self, crm_url, browser1, adviser_account, counseling_supervision_account, school_name,
                            phone_number, pass_word, adviser_name):
        """
        测试单个客户分单
        :param crm_url:
        :param browser1:
        :param adviser_account:
        :param school_name:
        :param phone_number:
        :param pass_word:
        :param adviser_name:
        :return:
        """
        page = GfyCrmCustomerManagement(browser1)
        login(crm_url, browser1, counseling_supervision_account, pass_word)
        add_customer(browser1, new_student_name(), phone_number)
        sleep(1)
        split_customer(browser1, adviser_account, school_name)
        sleep(2)
        page.checkbox_split_count.click()
        sleep(1)
        # 断言分单次数
        # 断言分单跟进人
        assert page.split_count.text == "1"
        assert page.split_customer.text == adviser_name

    def test_convert_student(self, crm_url, browser1, counseling_supervision_account, pass_word, school_name,
                             phone_number, adviser_account):
        """
        测试单个客户转为学员
        :param crm_url:
        :param browser1:
        :param counseling_supervision_account:
        :param pass_word:
        :param school_name:
        :param phone_number:
        :param adviser_account:
        :return:
        """
        page = GfyCrmCustomerManagement(browser1)
        login(crm_url, browser1, counseling_supervision_account, pass_word)
        add_customer(browser1, new_student_name(), phone_number)
        sleep(1)
        split_customer(browser1, adviser_account, school_name)
        sleep(1)
        convert_student(browser1, school_name)
        sleep(1)
        assert page.convert_success_text.text == "成功转为学员"

    def test_create_account(self, browser1, pass_word, school_name, crm_url, adviser_account,
                            counseling_supervision_account, phone_number):
        """
        测试单个客户转为学员
        :param browser1:
        :param pass_word:
        :param school_name:
        :param crm_url:
        :param adviser_account:
        :param counseling_supervision_account:
        :param phone_number:
        :return:
        """
        page = GfyCrmCustomerManagement(browser1)
        account_name = new_student_name()
        login(crm_url, browser1, counseling_supervision_account, pass_word)
        add_customer(browser1, account_name, phone_number)
        sleep(1)
        split_customer(browser1, adviser_account, school_name)
        sleep(1)
        convert_student(browser1, school_name)
        sleep(1)
        page.customer_ok_button.click()
        sleep(1)
        create_account(browser1, pass_word, school_name)
        sleep(1)
        assert page.customer_create_account_save_status.text == account_name

    def test_customer_recovery(self, crm_url, browser1, counseling_supervision_account, pass_word, phone_number,
                               adviser_account, school_name, adviser_account2, adviser_name2):
        """
        测试二手单回收再分单
        :param crm_url:
        :param browser1:
        :param counseling_supervision_account:
        :param pass_word:
        :param phone_number:
        :param adviser_account:
        :param school_name:
        :param adviser_account2:
        :param adviser_name2:
        :return:
        """
        page = GfyCrmCustomerManagement(browser1)
        login(crm_url, browser1, counseling_supervision_account, pass_word)
        add_customer(browser1, new_student_name(), phone_number)
        sleep(1)
        # 第一个跟进人分单
        split_customer(browser1, adviser_account, school_name)
        # 分单完成等待刷新
        sleep(1)
        first_customer_teacher_name = customer_recovery(browser1)
        # 等待"保存成功"提示
        PageWait(page.customer_recovery_status)
        assert page.customer_recovery_status.text == "保存成功"
        sleep(1)
        page.customer_recovery_date_button.click()
        sleep(1)
        page.customer_recovery_teacher_button.click()
        sleep(1)
        assert page.customer_recovery_date[0].text != "--"
        assert page.customer_recovery_teacher[0].text == first_customer_teacher_name
        sleep(1)
        # 二手单分单
        split_customer(browser1, adviser_account2, school_name)
        sleep(1)
        page.checkbox_split_count.click()
        sleep(1)
        # 二手单分单次数为2
        # 断言主跟进人
        assert page.customer_teacher[3].text == adviser_name2
        assert page.split_count.text == "2"


class TestCustomerAddOrder:
    """
    客户新建订单和支付订单、未上课退费
    """
    def test_add_new_order(self, crm_url, browser1, adviser_name, course, pass_word, counseling_supervision_account,
                           school_name, phone_number, adviser_account):
        """
        测试创建订单-新单招生
        :param crm_url:
        :param browser1:
        :param adviser_name:
        :param course:
        :param pass_word:
        :param counseling_supervision_account:
        :param school_name:
        :param phone_number:
        :param adviser_account:
        :return:
        """
        order_page = GfyCustomerAddOrder(browser1)
        menu_page = GfyMenu(browser1)
        login(crm_url, browser1, counseling_supervision_account, pass_word)
        sleep(1)
        add_customer(browser1, new_student_name(), phone_number)
        sleep(1)
        split_customer(browser1, adviser_account, school_name)
        sleep(1)
        convert_student(browser1, school_name)
        sleep(1)
        order_page.ok_button.click()
        # sleep(1)
        # menu_page.customer_management.click()
        sleep(1)
        add_new_order(browser1, adviser_name, course, school_name)
        sleep(1)
        order_page.order_status_confirm.click()
        sleep(1)
        order_page.order_info_loadStuOrderList.click()
        sleep(1)
        # 订单数量断言
        assert order_page.order_info_totalNum[3].text == "1"

    def test_pay_new_order(self, crm_url, browser1, school_name, adviser_account, pass_word, phone_number, adviser_name,
                           course, counseling_supervision_account):
        """
        测试支付订单：添加优惠-添加支付-添加其他费用-添加分成对象
        :param crm_url:
        :param browser1:
        :param school_name:
        :param adviser_account:
        :param pass_word:
        :param phone_number:
        :param adviser_name:
        :param course:
        :param counseling_supervision_account:
        :return:
        """
        menu_page = GfyMenu(browser1)
        order_page = GfyCustomerAddOrder(browser1)
        login(crm_url, browser1, counseling_supervision_account, pass_word)
        add_customer(browser1, new_student_name(), phone_number)
        sleep(1)
        split_customer(browser1, adviser_account, school_name)
        sleep(1)
        convert_student(browser1, school_name)
        sleep(1)
        order_page.ok_button.click()
        sleep(1)
        # menu_page.customer_management.click()
        # sleep(1)
        add_new_order(browser1, adviser_name, course, school_name)
        sleep(1)
        order_page.order_status_confirm.click()
        sleep(1)
        pay_new_order(browser1)
        # 断言是否支付成功
        sleep(1)
        assert order_page.pay_order_status.text == "成功"
        assert order_page.pay_order_calculation_status.text == "成功"

    def test_student_refund(self, browser1, crm_url, supervisor_account, pass_word, remarks,
                            phone_number, adviser_name, adviser_account, course, school_name, educational_effect_time,
                            educational_account, counseling_supervision_account):
        """
        测试客户退费
        :param browser1:
        :param crm_url:
        :param supervisor_account:
        :param pass_word:
        :param remarks:
        :param phone_number:
        :param adviser_name:
        :param adviser_account:
        :param course:
        :param school_name:
        :param educational_effect_time:
        :param educational_account:
        :return:
        """
        menu_page = GfyMenu(browser1)
        order_page = GfyCustomerAddOrder(browser1)
        other_page = GfyCrmCustomerManagement(browser1)
        login(crm_url, browser1, counseling_supervision_account, pass_word)
        add_customer(browser1, new_student_name(), phone_number)
        sleep(1)
        split_customer(browser1, adviser_account, school_name)
        sleep(1)
        convert_student(browser1, school_name)
        sleep(1)
        order_page.ok_button.click()
        sleep(1)
        # menu_page.customer_management.click()
        # sleep(1)
        add_new_order(browser1, adviser_name, course, school_name)
        sleep(1)
        order_page.order_status_confirm.click()
        sleep(1)
        pay_new_order(browser1)
        sleep(1)
        other_page.cancel_btn.click()
        sleep(1)
        menu_page.student_management.click()
        sleep(1)
        refund_apply_list = refund_apply(browser1, remarks)
        refund_fee_text = refund_apply_list[2]
        order_id_text = refund_apply_list[1]
        customer_name = refund_apply_list[0]

        assert refund_fee_text == order_page.application_for_refund.get_attribute("value")
        assert order_page.approval_matter_status.text == "审批保存成功"
        sleep(1)
        order_page.order_status_confirm.click()
        sleep(1)
        # 首页审批退费
        home_page = GfyHomePage(browser1)
        menu_page = GfyMenu(browser1)
        menu_page.dashboard.click()
        sleep(1)
        home_page.more_home_remind.click()
        sleep(1)
        home_page.search_object_name_input.send_keys("退费申请:待审批")
        sleep(1)
        home_page.remind_content_search_input.send_keys(customer_name)
        sleep(1)
        home_page.remind_center_approve_btn.click()
        sleep(1)
        PageSelect(home_page.approval_matter_type, value="A05")
        sleep(1)
        home_page.approval_matter_approval_detail.click()
        sleep(1)
        home_page.approval_result_input.click()
        sleep(1)
        home_page.save_approval_result.click()
        sleep(1)
        assert home_page.status.text == "保存成功"
        # 财务管理进行确认退费
        home_page.ok_button.click()
        sleep(1)
        menu_page = GfyMenu(browser1)
        refund_page = GfyRefundInfo(browser1)
        menu_page.finance_menu.click()
        sleep(1)
        menu_page.finance_fee_info.click()
        sleep(1)
        menu_page.finance_refund_info.click()
        sleep(1)
        refund_page.refund_order_id_input.send_keys(order_id_text)
        sleep(1)
        refund_page.query_refund_info_btn.click()
        sleep(1)
        refund_page.refund_check_confirm_btn.click()
        sleep(1)
        refund_page.refund_confirm_btn.click()
        sleep(1)
        assert refund_page.refund_status.text == "已退费"


if __name__ == '__main__':
    # pytest.main()
    # pytest.main(["-v", "-s", "test_crm_cust_manger.py::TestCustInfo::test_cust_invite"])
    # pytest.main(["-v", "-s", "test_crm_cust_manger.py::TestCustomerAdd::test_customer_recovery"])
    # pytest.main(["-v", "-s", "test_crm_cust_manger.py::TestCustomerAdd::test_login",
    #              "test_crm_cust_manger.py::TestCustomerAdd::test_add_customer"])
    # pytest.main(["-v", "-s", "test_crm_cust_manger.py::TestLogin"])
    pytest.main(["-v", "-s", "test_crm_cust_manger.py::TestCustomerAddOrder::test_add_new_order"])
    # pytest.main(["-v", "-s", "test_crm_cust_manger.py::TestCustomerAddOrder"])
    # pytest.main(["-v", "-s", "test_crm_cust_manger.py::TestCustomerAdd::test_add_customer",
    #              "-v", "-s", "test_crm_cust_manger.py::TestCustomerAdd::test_convert_student"])
