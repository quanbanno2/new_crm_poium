import sys
import pytest
from time import sleep
from poium import PageWait, PageSelect

from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))

from page.crm_cust_manger_page import GfyCrmCustomerManagement, GfyCustomerAddOrder
from page.crm_home_page import GfyHomePage
from page.crm_menu_page import GfyMenu
from page.crm_finance_page import GfyRefundInfo
from page.crm_login_page import GfyLogin
from test_func.db_func import eliminate_account_by_sql, new_customer_name_by_sql
from test_func.customer_management_func import operate_delete_customer, login, add_customer, split_customer, \
    convert_student, create_account, add_new_order, customer_recovery, pay_new_order, refund_apply


class TestLogin:

    def test_login(self, crm_url, browser1, pass_word, supervisor_account):
        """
        测试登录
        @param crm_url:
        @param browser1:
        @param pass_word:
        @param supervisor_account:
        @return:
        """
        page = GfyLogin(browser1)
        login(crm_url, browser1, supervisor_account, pass_word)
        PageWait(page.account_name)
        assert page.account_name.text == "高分云指导督导1"


class TestCustomerManagement:
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
        student_name = new_customer_name_by_sql()
        add_customer(browser1, student_name, phone_number)
        page = GfyCrmCustomerManagement(browser1)
        PageSelect(page.customer_list_school_list, text=school_name)
        sleep(2)
        assert page.customer_name.text == student_name
        # 数据清除
        operate_delete_customer(browser1)

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
        add_customer(browser1, new_customer_name_by_sql(), phone_number)
        sleep(1)
        split_customer(browser1, adviser_account)
        sleep(2)
        page.checkbox_split_count.click()
        sleep(1)
        # 断言分单次数
        # 断言分单跟进人
        assert page.split_count.text == "1"
        assert page.split_customer.text == adviser_name
        operate_delete_customer(browser1)

    def test_convert_student(self, crm_url, browser1, counseling_supervision_account, pass_word, school_name,
                             phone_number):
        """
        测试单个客户转为学员
        :param crm_url:
        :param browser1:
        :param counseling_supervision_account:
        :param pass_word:
        :param school_name:
        :param phone_number:
        :return:
        """
        page = GfyCrmCustomerManagement(browser1)
        login(crm_url, browser1, counseling_supervision_account, pass_word)
        add_customer(browser1, new_customer_name_by_sql(), phone_number)
        sleep(1)
        split_customer(browser1, counseling_supervision_account)
        sleep(1)
        convert_student(browser1, school_name)
        sleep(1)
        assert page.convert_success_text.text == "成功转为学员"
        page.customer_ok_button.click()
        sleep(1)
        operate_delete_customer(browser1)

    def test_create_account(self, browser1, pass_word, school_name, crm_url, counseling_supervision_account,
                            phone_number):
        """
        测试学员创建账号
        :param browser1:
        :param pass_word:
        :param school_name:
        :param crm_url:
        :param counseling_supervision_account:
        :param phone_number:
        :return:
        """
        page = GfyCrmCustomerManagement(browser1)
        account_name = new_customer_name_by_sql()
        login(crm_url, browser1, counseling_supervision_account, pass_word)
        add_customer(browser1, account_name, phone_number)
        sleep(1)
        split_customer(browser1, counseling_supervision_account)
        sleep(1)
        convert_student(browser1, school_name)
        sleep(1)
        page.customer_ok_button.click()
        sleep(1)
        create_account(browser1, pass_word, school_name)
        sleep(1)
        page.customer_ok_button.click()
        sleep(1)
        assert page.customer_create_account_save_status.text == account_name
        sleep(0.5)
        page.customer_list.click()
        sleep(1)
        # 我的客户-删除客户
        operate_delete_customer(browser1)
        # 清理账号
        eliminate_account_by_sql(account_name)
        sleep(2)

    def test_customer_recovery(self, crm_url, browser1, counseling_supervision_account, pass_word, phone_number,
                               school_name, adviser_account2, adviser_name2, adviser_name):
        """
        测试二手单回收再分单
        数据清理：客户信息、
        :param crm_url:
        :param browser1:
        :param counseling_supervision_account:
        :param pass_word:
        :param phone_number:
        :param school_name:
        :param adviser_account2:
        :param adviser_name2:
        :return:
        """
        page = GfyCrmCustomerManagement(browser1)
        login(crm_url, browser1, counseling_supervision_account, pass_word)
        add_customer(browser1, new_customer_name_by_sql(), phone_number)
        sleep(1)
        # 分单
        split_customer(browser1, counseling_supervision_account)
        sleep(1)
        first_customer_teacher_name = customer_recovery(browser1)
        # 等待"保存成功"提示
        PageWait(page.customer_recovery_status)
        # 断言是否回收成功
        assert page.customer_recovery_status.text == "保存成功"
        sleep(1)
        page.customer_recovery_date_button.click()
        sleep(1)
        page.customer_recovery_teacher_button.click()
        sleep(1)
        # 断言是否有回收时间
        assert page.customer_recovery_date.text != "--"
        sleep(1)
        # 断言回收人是否正确
        assert page.customer_recovery_teacher.text == first_customer_teacher_name
        sleep(1)
        # 二手单分单
        split_customer(browser1, adviser_account2)
        sleep(2)
        page.checkbox_split_count.click()
        sleep(1)
        # 二手单分单次数为2
        # 断言主跟进人
        assert page.customer_teacher[3].text == adviser_name2
        sleep(1)
        assert page.split_count.text == "2"
        operate_delete_customer(browser1)


class TestCustomerAddOrder:
    """
    客户新建订单和支付订单、未上课退费
    """

    def test_add_new_order(self, crm_url, browser1, course, pass_word, counseling_supervision_account,
                           school_name, phone_number, counseling_supervision_name):
        """
        测试创建订单-新单招生
        @param crm_url:
        @param browser1:
        @param course:
        @param pass_word:
        @param counseling_supervision_account:
        @param school_name:
        @param phone_number:
        @param counseling_supervision_name:
        @return:
        """
        order_page = GfyCustomerAddOrder(browser1)
        login(crm_url, browser1, counseling_supervision_account, pass_word)
        sleep(1)
        add_customer(browser1, new_customer_name_by_sql(), phone_number)
        sleep(1)
        split_customer(browser1, counseling_supervision_account)
        sleep(1)
        convert_student(browser1, school_name)
        sleep(1)
        order_page.ok_button.click()
        sleep(1)
        add_new_order(browser1, counseling_supervision_name, course, school_name)
        sleep(1)
        order_page.order_status_confirm.click()
        sleep(1)
        order_page.order_info_loadStuOrderList.click()
        sleep(1)
        # 订单数量断言
        assert order_page.order_info_totalNum[3].text == "1"

    def test_pay_new_order(self, crm_url, browser1, school_name, pass_word, phone_number, course,
                           counseling_supervision_name, counseling_supervision_account):
        """
        测试支付订单：添加优惠-添加支付-添加其他费用-添加分成对象
        @param crm_url:
        @param browser1:
        @param school_name:
        @param pass_word:
        @param phone_number:
        @param course:
        @param counseling_supervision_name:
        @param counseling_supervision_account:
        @return:
        """
        order_page = GfyCustomerAddOrder(browser1)
        login(crm_url, browser1, counseling_supervision_account, pass_word)
        add_customer(browser1, new_customer_name_by_sql(), phone_number)
        sleep(1)
        split_customer(browser1, counseling_supervision_account)
        sleep(1)
        convert_student(browser1, school_name)
        sleep(1)
        order_page.ok_button.click()
        sleep(1)
        add_new_order(browser1, counseling_supervision_name, course, school_name)
        sleep(1)
        order_page.order_status_confirm.click()
        sleep(1)
        pay_new_order(browser1)
        # 断言是否支付成功
        sleep(3)
        assert order_page.pay_order_status.text == "成功"
        assert order_page.pay_order_calculation_status.text == "成功"

    def test_student_refund(self, browser1, crm_url, supervisor_account, pass_word, remarks,
                            phone_number, course, school_name, educational_effect_time, educational_account,
                            counseling_supervision_account, counseling_supervision_name):
        """
        测试客户退费
        活动：新招生
        @param browser1:
        @param crm_url:
        @param supervisor_account:
        @param pass_word:
        @param remarks:
        @param phone_number:
        @param course:
        @param school_name:
        @param educational_effect_time:
        @param educational_account:
        @param counseling_supervision_account:
        @param counseling_supervision_name:
        @return:
        """
        menu_page = GfyMenu(browser1)
        order_page = GfyCustomerAddOrder(browser1)
        other_page = GfyCrmCustomerManagement(browser1)
        login(crm_url, browser1, counseling_supervision_account, pass_word)
        add_customer(browser1, new_customer_name_by_sql(), phone_number)
        sleep(1)
        split_customer(browser1, counseling_supervision_account)
        sleep(1)
        convert_student(browser1, school_name)
        sleep(1)
        order_page.ok_button.click()
        sleep(1)
        add_new_order(browser1, counseling_supervision_name, course, school_name)
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
    # pytest.main(["-v", "-s", "test_crm_cust_manger.py"])
    # pytest.main(["-v", "-s", "test_crm_cust_manger.py::TestCustInfo::test_cust_invite"])
    # pytest.main(["-v", "-s", "test_crm_cust_manger.py::TestCustomerAdd::test_customer_recovery"])
    # pytest.main(["-v", "-s", "test_crm_cust_manger.py::TestCustomerAdd::test_login",
    #              "test_crm_cust_manger.py::TestCustomerAdd::test_add_customer"])
    # pytest.main(["-v", "-s", "test_crm_cust_manger.py::TestLogin::test_login"])
    pytest.main(["-v", "-s", "test_crm_cust_manger.py::TestCustomerAddOrder::test_pay_new_order"])
    # pytest.main(["-v", "-s", "test_crm_cust_manger.py::TestCustomerAddOrder"])
    # pytest.main(["-v", "-s", "test_crm_cust_manger.py::TestCustomerManagement::test_create_account"])
    #              "-v", "-s", "test_crm_cust_manger.py::TestCustomerAdd::test_convert_student"])
