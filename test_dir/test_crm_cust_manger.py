import sys
import os
import pytest
from time import sleep
from os.path import dirname, abspath
from page.crm_cust_manger_page import GfyCrmAddCustomer, GfyCustAddOrder
from page.crm_home_page import GfyHomePage
from page.crm_menu_page import GfyMenu
from page.crm_finance_page import GfyRefundInfo
from poium import PageWait, PageSelect
from _pydecimal import Context, ROUND_HALF_UP

sys.path.insert(0, dirname(dirname(abspath(__file__))))


def login(url, driver, account, password):
    """
    系统登录
    :param url:
    :param driver:
    :param account:
    :param password:
    :return:
    """
    page = GfyCrmAddCustomer(driver)
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
    page = GfyCrmAddCustomer(driver)
    menu_page = GfyMenu(driver)
    menu_page.customer_management.click()
    menu_page.my_customer.click()
    page.add_cust.click()
    sleep(2)
    page.add_cust_name.send_keys(customer_name)
    page.school_name.click()
    PageWait(page.pub_school_list)
    page.pub_school_list.send_keys("四基初级中学")
    page.pub_school_query.click()
    PageWait(page.pub_school_choice)
    page.pub_school_choice.click()
    PageWait(page.grade)
    PageSelect(page.grade, value='string:G09')
    page.cust_activity.click()
    PageWait(page.activity_type)
    PageSelect(page.activity_type, value='string:T01')
    page.activity_name.send_keys('高分云信息单')
    page.activity_query.click()
    sleep(1)
    page.activity_selected.click()
    page.customer_phone.send_keys(phone_number)
    page.add_customer_save.click()


def split_customer(driver, adviser_name):
    """
    单个学员分单
    :param driver:
    :param adviser_name:
    :return:
    """
    page = GfyCrmAddCustomer(driver)
    page.cust_check.click()
    page.cust_split.click()
    PageWait(page.teacher_list_login_name)
    page.teacher_list_login_name.send_keys(adviser_name)
    page.teacher_list_query.click()
    PageWait(page.teacher_select)
    page.teacher_select.click()
    PageWait(page.confirm_split)
    page.confirm_split.click()


def convert_student(driver):
    """
    单个客户转为学员
    :param driver:
    :return:
    """
    page = GfyCrmAddCustomer(driver)
    sleep(1)
    page.convert_to_student.click()
    sleep(1)
    page.confirm_btn.click()


def create_account(driver, password):
    """
    客户详情创建教学帐号绑定
    :param driver:
    :param password:
    :return:
    """
    page = GfyCrmAddCustomer(driver)
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
    sleep(1)


def add_new_order(driver, url, login_name, password, consultant, course_name):
    """
    客户创建订单
    :param driver:
    :param url:
    :param login_name: 登录名称
    :param password: 登录密码
    :param consultant: 顾问老师名称
    :param course_name: 课程名称
    :return:
    """
    customer_page = GfyCrmAddCustomer(driver)
    menu_page = GfyMenu(driver)
    login(url, driver, login_name, password)
    sleep(1)
    menu_page.customer_management.click()
    sleep(1)
    menu_page.my_customer.click()
    sleep(1)
    customer_page.cust_name.click()
    order_page = GfyCustAddOrder(driver)
    sleep(1)
    order_page.cust_order_info.click()
    sleep(1)
    order_page.cust_order_add.click()
    sleep(1)
    PageSelect(order_page.order_sharing_object_select, text=consultant)
    sleep(1)
    order_page.order_sharing_object_select_btn.click()
    sleep(1)
    order_page.order_select_course.click()
    sleep(1)
    order_page.order_select_coursename.send_keys(course_name)
    sleep(1)
    order_page.order_select_coursename_query.click()
    sleep(1)
    order_page.order_select_course_btn.click()
    sleep(1)
    order_page.order_save_stu_order.click()


def pay_new_order(driver):
    """
    新招生单单支付（优惠、支付项、手续费、支付）
    :param driver:
    :return:
    """
    order_page = GfyCustAddOrder(driver)
    menu_page = GfyMenu(driver)
    other_page = GfyCrmAddCustomer(driver)
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
    # 其他费用
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
    sleep(1)


def refund_apply(driver, remarks):
    menu_page = GfyMenu(driver)
    order_page = GfyCustAddOrder(driver)
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
    PageWait(order_page.save_approval_matter)
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


class TestCustomerAdd:

    def test_login(self, crm_url, browser1, pass_word, supervisor_account):
        """
        测试登录
        :param crm_url:
        :param browser1:
        :param pass_word:
        :param supervisor_account:
        :return:
        """
        page = GfyCrmAddCustomer(browser1)
        login(crm_url, browser1, supervisor_account, pass_word)
        PageWait(page.account_name)
        assert page.account_name.text == "高分云指导督导1"

    def test_add_customer(self, crm_url, browser1, connect_db, phone_number, pass_word, supervisor_account):
        """
        测试新增客户：新招生
        :param crm_url:
        :param browser1:
        :param connect_db:
        :param phone_number:
        :param pass_word:
        :param supervisor_account:
        :return:
        """
        add_customer(browser1, connect_db, phone_number)
        page = GfyCrmAddCustomer(browser1)
        sleep(2)
        # 判断新增客户是否成功
        assert page.cust_name.text == connect_db

    # def test_import_customer(self, browser1, crm_url, pass_word, template_dir, supervisor_account):
    #     """
    #     我的客户-导入客户：新招生
    #     :param browser1:
    #     :param crm_url:
    #     :param pass_word:
    #     :param template_dir:
    #     :param supervisor_account:
    #     :return:
    #     """
    #     page = GfyCrmAddCustomer(browser1)
    #     login(crm_url, browser1, supervisor_account, pass_word)
    #     PageWait(page.cust_manger)
    #     page.cust_manger.click()
    #     PageWait(page.my_cust)
    #     page.my_cust.click()
    #     PageWait(page.import_customer_btn)
    #     page.import_customer_btn.click()
    #     PageWait(page.import_customer_school)
    #     PageSelect(page.import_customer_school, text="高分云")
    #     PageWait(page.import_customer_school_name)
    #     page.import_customer_school_name.click()
    #     PageWait(page.pub_school_list)
    #     page.pub_school_list.send_keys("四基初级中学")
    #     page.pub_school_query.click()
    #     PageWait(page.pub_school_choice)
    #     page.pub_school_choice.click()
    #     PageWait(page.import_customer_info_name)
    #     page.import_customer_info_name.click()
    #     PageWait(page.cust_activity_type)
    #     PageSelect(page.cust_activity_type, text="新单招生")
    #     page.cust_activity_name.send_keys("高分云信息单")
    #     page.cust_activity_query.click()
    #     sleep(1)
    #     page.cust_activity_selected.click()
    #     PageWait(page.import_customer_select_files)
    #     page.import_customer_select_files.click()
    #     sleep(2)
    #     # 执行上传文件的程序
    #     # win32api.ShellExecute(0, 'open', template_dir, '', '', 0)
    #     template_path = os.path.abspath("..")
    #     # 拼接上传文件脚本地址
    #     template_dir_path = template_path + template_dir
    #     os.system(template_dir_path)
    #     PageWait(page.import_customer_postfiles)
    #     sleep(10)
    #     page.import_customer_postfiles.click()
    #     # assert 断言

    def test_split_customer(self, browser1, adviser_account):
        """
        测试单个客户分单
        :param browser1:
        :param adviser_account:
        :return:
        """
        split_customer(browser1, adviser_account)
        page = GfyCrmAddCustomer(browser1)
        sleep(2)
        page.checkbox_split_count.click()
        PageWait(page.split_count)
        assert page.split_count.text == "1"

    def test_convert_student(self, browser1):
        """
        测试单个转为学员
        :param browser1:
        :return:
        """
        convert_student(browser1)
        page = GfyCrmAddCustomer(browser1)
        sleep(1)
        assert page.convert_success_text.text == '成功转为学员'
        page.convert_success_button.click()
        sleep(1)

    def test_create_account(self, browser1, pass_word):
        """
        测试创建客户教学账号
        :param browser1:
        :param pass_word:
        :return:
        """
        create_account(browser1, pass_word)
        page = GfyCrmAddCustomer(browser1)
        assert page.customer_create_account_save_status.text == "保存成功"
        sleep(1)
        # 点击确定按钮
        page.convert_success_button.click()


# class TestCustInfo:
#     """
#     辅导招生（邀约、到会、促成、回收）
#     """
#
#     def test_cust_invite(self, crm_url, browser1, connect_db, pass_word, audio_dir,
#     comm_content, Remark, supervisor_account):
#         """
#         邀约-有效沟通、承诺到会
#         :param crm_url:
#         :param browser1:
#         :param connect_db:
#         :param pass_word:
#         :param audio_dir:
#         :param comm_content:
#         :param Remark:
#         :return:
#         """
#         page = GfyCrmAddCustomer(browser1)
#         page_com = CustRecruitStudents(browser1)
#         login(crm_url, browser1, supervisor_account, pass_word)
#         PageWait(page.cust_manger)
#         page.cust_manger.click()
#         PageWait(page.my_cust)
#         page.my_cust.click()
#         PageWait(page.cust_name)
#         page.cust_name.click()
#         PageWait(page_com.cust_communicate_switch_tab)
#         page_com.cust_communicate_switch_tab.click()
#         PageWait(page_com.cust_communicate_add)
#         page_com.cust_communicate_add.click()
#         PageWait(page_com.cust_communicate_responsible_personal_name)
#         page_com.cust_communicate_responsible_personal_name.click()
#         PageWait(page_com.cust_communicate_responsible_personal_department)
#         PageSelect(page_com.cust_communicate_responsible_personal_department, text="高分云顾问部")
#         page_com.cust_communicate_responsible_personal_query.click()
#         sleep(1)
#         page_com.cust_communicate_responsible_personal_selected.click()
#         PageWait(page_com.cust_communicate_content)
#         # 获取动态id
#         content_id = page_com.cust_communicate_content.get_attribute("id")
#         set_content(browser1, content_id, comm_content)
#         sleep(1)
#         audio_upload(browser1, audio_dir)
#         sleep(5)
#         page_com.cust_communicate_visit_date.click()
#         PageWait(page.customer_create_account_birthday_today)
#         page.customer_create_account_birthday_today.click()
#         PageWait(page_com.cust_communicate_remark)
#         page_com.cust_communicate_remark.send_keys(Remark)
#         page_com.cust_communicate_enable.click()
#         PageWait(page_com.cust_communicate_status)
#         assert page_com.cust_communicate_status.text == Remark
#
#     def test_cust_meeting(self, browser1, crm_url, supervisor_account):
#         page = CustRecruitStudents(browser1)
#         PageWait(page.cust_meeting_swtich_tab)
#         page.cust_meeting_swtich_tab.click()
#         PageWait(page.cust_meeting_add)
#         page.cust_meeting_add.click()
#         PageWait(page.cust_meeting_user)
#         page.cust_meeting_user.click()
#         PageWait(page.cust_communicate_responsible_personal_department)
#         PageSelect(page.cust_communicate_responsible_personal_department, text="高分云顾问部")
#         sleep(1)
#         page.cust_communicate_responsible_personal_selected.click()
#         PageWait(page.cust_meeting_parent_list)
#         PageSelect(page.cust_meeting_parent_list, text="父亲")
#         page.cust_meeting_confirm_save.click()
#         PageWait(page.cust_meeting_confirm_person)
#         # 通过确认人断言是否到会
#         assert page.cust_meeting_confirm_person.text == supervisor_account


class TestCustomerAddOrder:
    """
    客户新建订单和支付订单、未上课退费
    """

    def test_add_new_order(self, crm_url, browser1, adviser_name, course, pass_word, supervisor_account):
        """
        创建订单-新单招生
        :param crm_url:
        :param browser1:
        :param adviser_name:
        :param course:
        :param pass_word:
        :param supervisor_account:
        :return:
        """
        order_page = GfyCustAddOrder(browser1)
        add_new_order(browser1, crm_url, supervisor_account, pass_word, adviser_name, course)
        sleep(1)
        order_status_text = order_page.order_status.text
        sleep(1)
        order_page.order_status_confirm.click()
        sleep(1)
        assert order_status_text == "成功"

    def test_pay_new_order(self, browser1):
        """
        支付订单：添加优惠-添加支付-添加其他费用-添加分成对象
        :param browser1:
        :return:
        """
        order_page = GfyCustAddOrder(browser1)
        pay_new_order(browser1)
        # 断言是否支付成功
        PageWait(order_page.pay_order_status)
        assert order_page.pay_order_status.text == "成功"
        assert order_page.pay_order_calculation_status.text == "成功"
        PageWait(order_page.pay_order_leave)
        order_page.pay_order_leave.click()

    def test_student_refund(self, browser1, crm_url, supervisor_account, pass_word, remarks):
        """
        未分班退费
        :param browser1:
        :param crm_url:
        :return:TestCustomerAddOrder
        """
        # 申请退费
        login(crm_url, browser1, supervisor_account, pass_word)
        order_page = GfyCustAddOrder(browser1)
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
    # pytest.main(["-v", "-s", "test_crm_cust_manger.py::TestCustAdd::test_create_account"])
    # pytest.main(["-v", "-s", "test_crm_cust_manger.py::TestCustomerAdd::test_login",
    #              "test_crm_cust_manger.py::TestCustomerAdd::test_add_customer"])
    # pytest.main(["-v", "-s", "test_crm_cust_manger.py::TestCustomerAdd"])
    pytest.main(["-v", "-s", "test_crm_cust_manger.py::TestCustomerAddOrder::test_student_refund"])
    # pytest.main(["-v", "-s", "test_crm_cust_manger.py::TestCustomerAddOrder"])
