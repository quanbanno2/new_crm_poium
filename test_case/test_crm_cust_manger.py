import sys
import pytest
# import logging
from time import sleep
from poium import PageWait, PageSelect
# 定义搜索模块顺序，优先搜索new_crm_poium文件夹
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))

from page.crm_customer_management_page import GfyCrmCustomerManagement
from page.crm_menu_page import GfyMenu

from func.api_request import crmRequest
from func.db_func import DB
from func.xpath_element import by_xpath_contains
from func.customer_management_func import login, split_customer, convert_student, create_account, add_customer, \
    customer_recovery, customerManagementFunc
from func.get_data import get_json_data
from conftest import DATA_DIR
from config import nextTime


# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)


class TestCustomerManagement:
    """
    客户管理模块测试
    """

    @pytest.mark.parametrize(
        "case,schoolName,businessType,loginAccount,password,activityName,phoneNumber,msg",
        get_json_data(DATA_DIR + "customer_management/" + "add_customer_success.json")
    )
    def test_add_customer_success(self, crm_url, browser1, case, schoolName, businessType, loginAccount,
                                  password, activityName, phoneNumber, msg):
        """
        测试新增客户成功情况
        @param crm_url:
        @param browser1:
        @param case:
        @param schoolName:
        @param businessType:
        @param loginAccount:
        @param password:
        @param activityName:
        @param phoneNumber:
        @param msg:
        @return:
        """
        page = GfyCrmCustomerManagement(browser1)
        # 客户名称自动生成
        customer_name = DB().new_customer_name_by_sql()
        login(crm_url, browser1, loginAccount, password)
        add_customer(browser1, customer_name, businessType, activityName, phoneNumber, schoolName)
        PageWait(page.save_status)
        save_text = page.save_status.text
        assert save_text == msg

    # @pytest.mark.parametrize(
    #     "case,businessType,loginAccount,password,activityName,phoneNumber,msg",
    #     get_json_data(DATA_DIR + "add_customer_fail.json")
    # )
    # 失败情况待施工
    # def test_add_customer_fail(self, crm_url, browser1, phone_number, case, businessType, loginAccount, password,
    #                            activityName, phoneNumber, msg):
    #     """
    #     新增客户失败的情况
    #     @param crm_url:
    #     @param browser1:
    #     @param phone_number:
    #     @param case:
    #     @param businessType:
    #     @param loginAccount:
    #     @param password:
    #     @param activityName:
    #     @param phoneNumber:
    #     @param msg:
    #     @return:
    #     """
    @pytest.mark.parametrize(
        "case,schoolName,studentNum,businessType,activityName,phoneNumber,teacherName,loginAccount,password,msg",
        get_json_data(DATA_DIR + "customer_management/" + "split_customer_success.json")
    )
    def test_split_customer_success(self, crm_url, browser1, case, schoolName, studentNum, businessType, activityName,
                                    phoneNumber, teacherName, loginAccount, password, msg, i=0):
        """
        测试学员分单成功情况
        @param crm_url:
        @param browser1:
        @param case:
        @param schoolName:
        @param studentNum:
        @param businessType:
        @param activityName:
        @param phoneNumber:
        @param teacherName:
        @param loginAccount:
        @param password:
        @param msg:
        @return:
        """
        page = GfyCrmCustomerManagement(browser1)
        menu_page = GfyMenu(browser1)
        login(crm_url, browser1, loginAccount, password)
        while i < studentNum:
            crmRequest.save_customer_info(DB().new_customer_name_by_sql())
            i += 1
        menu_page.customer_management.click()
        menu_page.my_customer.click()
        split_customer(browser1, teacherName, studentNum)
        # 是否保存分单成功
        PageWait(page.save_status)
        assert page.save_status.text == msg

    @pytest.mark.parametrize(
        "case,loginAccount,password,customerName,liablePersonAccount,communicationInfo,communicationResult,isVisit,"
        "parent,admitResult,meetingResult,msg",
        get_json_data(DATA_DIR + "customer_management/" + "customer_communication.json")
    )
    def test_customer_communication(self, crm_url, browser1, case, loginAccount, password, customerName,
                                    liablePersonAccount, communicationInfo, communicationResult, isVisit, parent,
                                    admitResult, meetingResult, msg):
        menu_page = GfyMenu(browser1)
        customer_page = GfyCrmCustomerManagement(browser1)
        cmf = customerManagementFunc(browser1)
        login(crm_url, browser1, loginAccount, password)
        # 初始化测试客户信息（删除客户、新建客户、分单）
        DB().delete_customer_info(cust_name=customerName)
        crmRequest.save_customer_info(customerName)
        customer_id = DB().get_customer_id(customerName)
        crmRequest.allot_order(customer_id)
        teacher_id = DB().get_teacher_id(liablePersonAccount)
        DB().update_admin_status(teacher_id)
        if menu_page.menu_loading:
            menu_page.customer_management.click()
            if menu_page.menu_active:
                menu_page.my_customer.click()
                if customer_page.customer_loading:
                    customer_page.customer_name_input.send_keys(customerName)
                    customer_page.customer_list_load_button.click()
                    if customer_page.customer_loading:
                        # 点击客户名称进入客户综合信息
                        by_xpath_contains(browser1, "a", customerName).click()
                        # 邀约
                        com_dict = cmf.customer_communication(communicationInfo, communicationResult, isVisit,
                                                              nextTime)
                        try:
                            assert com_dict["save_status"] == msg
                        finally:
                            try:
                                assert com_dict["communication_result"] == communicationResult
                            finally:
                                try:
                                    assert com_dict["is_visit"] == isVisit
                                finally:
                                    # 到会确认
                                    meet_dict = cmf.customer_meeting(isVisit, parent)
                        try:
                            assert meet_dict["save_status"] == msg
                        finally:
                            try:
                                assert meet_dict["meetingResult"] == meetingResult
                            finally:
                                # 接待
                                admit_dict = cmf.customer_admit()
                        try:
                            assert admit_dict["save_status"] == msg
                        finally:
                            try:
                                assert admit_dict["admit_result"] == admitResult
                            finally:
                                DB().delete_customer_info(cust_id=customer_id)

    @pytest.mark.parametrize(
        "case,studentNum,teacherName,schoolName,loginAccount,password,msg",
        get_json_data(DATA_DIR + "customer_management/" + "convert_student_success.json")
    )
    def test_convert_student_success(self, crm_url, browser1, case, studentNum, teacherName, schoolName, loginAccount,
                                     password, msg, i=0):
        """
        测试单个客户转为学员
        @param crm_url:
        @param browser1:
        @param case: 用例名称
        @param studentNum:
        @param teacherName:
        @param schoolName:
        @param loginAccount:
        @param password:
        @param msg: 断言信息
        @return:
        """
        page = GfyCrmCustomerManagement(browser1)
        menu_page = GfyMenu(browser1)
        studentNum = int(studentNum)
        login(crm_url, browser1, loginAccount, password)
        while i < studentNum:
            customer_name = DB().new_customer_name_by_sql()
            crmRequest.save_customer_info(customer_name)
            i += 1
        menu_page.customer_management.click()
        menu_page.my_customer.click()
        split_customer(browser1, teacherName, studentNum)
        login(crm_url, browser1, teacherName, password)
        menu_page.customer_management.click()
        menu_page.my_customer.click()
        sleep(2)
        convert_student(browser1, schoolName, studentNum)
        sleep(1)
        if case == "单个客户转学员-成功" or case == "客户批量学员-全部成功":
            # 断言提示框标题和提示内容
            assert page.convert_success_text.text == msg and page.convert_success_tips is None
        elif case == "客户批量学员-部分成功":
            # 部分成功即存在已转学员的
            assert page.convert_success_text.text == msg and page.convert_success_tips.text is not None

    @pytest.mark.parametrize(
        "case,accountExist,teacherName,schoolName,loginAccount,password,existAccountName",
        get_json_data(DATA_DIR + "customer_management/" + "create_account.json")
    )
    def test_create_account(self, crm_url, browser1, case, accountExist, teacherName, schoolName, loginAccount,
                            password, existAccountName):
        """
        测试客户绑定和创建账号
        @param crm_url:
        @param browser1:
        @param case:
        @param accountExist:
        @param teacherName:
        @param schoolName:
        @param loginAccount:
        @param password:
        @param existAccountName:
        @return:
        """
        page = GfyCrmCustomerManagement(browser1)
        menu_page = GfyMenu(browser1)
        customer_name = DB().new_customer_name_by_sql()
        # 清除已存在账号的绑定信息
        DB().update_account(existAccountName)
        login(crm_url, browser1, loginAccount, password)
        crmRequest.save_customer_info(customer_name)
        # 分单
        menu_page.customer_management.click()
        menu_page.my_customer.click()
        split_customer(browser1, teacherName)
        sleep(1)
        login(crm_url, browser1, teacherName, password)
        menu_page.customer_management.click()
        menu_page.my_customer.click()
        sleep(2)
        # 转学员
        convert_student(browser1, schoolName)
        sleep(1)
        page.customer_ok_button.click()
        sleep(1)
        create_account(browser1, schoolName, accountExist, existAccountName, customer_name, password)
        sleep(2)
        if case == "已存在的账号名称":
            assert page.customer_create_account_save_status.text == existAccountName
            sleep(1)
            # 清理账号绑定
            DB().update_account(existAccountName)
        if case == "新建的账号名称":
            assert page.customer_create_account_save_status.text == customer_name

    @pytest.mark.parametrize(
        "case,studentNum,teacherName,loginAccount,password,msg",
        get_json_data(DATA_DIR + "customer_management/" + "customer_recovery.json")
    )
    def test_customer_recovery(self, crm_url, browser1, case, studentNum, teacherName, loginAccount, password, msg,
                               i=0):
        """
        测试二手单回收再分单
        数据清理：客户信息
        @param crm_url:
        @param browser1:
        @param case:
        @param studentNum:
        @param teacherName:
        @param loginAccount:
        @param password:
        @param msg:
        @param i:
        @return:
        """
        page = GfyCrmCustomerManagement(browser1)
        menu_page = GfyMenu(browser1)
        login(crm_url, browser1, loginAccount, password)
        # 新增客户
        while i < studentNum:
            crmRequest.save_customer_info(DB().new_customer_name_by_sql())
            i += 1
        menu_page.customer_management.click()
        menu_page.my_customer.click()
        # 分单
        split_customer(browser1, teacherName, studentNum)
        sleep(2)
        # 回收客户
        customer_recovery(browser1, studentNum)
        # 等待"保存成功"提示
        PageWait(page.customer_recovery_status)
        # 多个断言使用try-finally，断言失败不跳出
        # 断言是否回收成功
        try:
            assert page.customer_recovery_status.text == msg
        finally:
            sleep(1)
            PageSelect(page.customer_is_order, text="否")
            # 回收时间显示
            page.customer_recovery_date_button.click()
            # 显示回收跟进人
            page.customer_recovery_teacher_button.click()
            page.customer_list_load_button.click()
            if page.customer_loading:
                # if case == "单个客户回收":
                # 断言是否有回收时间&回收跟进人
                try:
                    assert page.customer_recovery_date[0].text != "--"
                finally:
                    assert page.customer_recovery_teacher[0].text == DB().get_account_name(teacherName)
            # elif case == "客户批量回收":
            # 问题：循环会在第二次失败断言后跳出，无法进入第二次循环进行断言
            #     try:
            #         while j < studentNum:
            #             try:
            #                 print("hello%s" % j)
            #                 assert page.customer_recovery_date[j].text == "--"
            #             finally:
            #                 try:
            #                     assert page.customer_recovery_teacher[j].text != DB().get_account_info(teacherName)
            #                 finally:
            #                     j += 1
            #     finally:
            #         while j < studentNum:
            #             try:
            #                 print("hello%s" % j)
            #                 assert page.customer_recovery_date[j].text == "--"
            #             finally:
            #                 try:
            #                     assert page.customer_recovery_teacher[j].text != DB().get_account_info(teacherName)
            #                 finally:
            #                     j += 1


if __name__ == '__main__':
    # pytest.main()
    pytest.main(["-v", "-s", "test_crm_cust_manger.py"])
    # pytest.main(["-v", "-s", "test_crm_cust_manger.py::TestCustomerManagement::test_convert_student_success"])
    # pytest.main(["-v", "-s", "test_crm_cust_manger.py::TestCustomerManagement::test_customer_communication"])
    # pytest.main(["-v", "-s", "test_crm_cust_manger.py::TestLogin::test_login_success"])

    # pytest.main(["-v", "-s", "test_crm_cust_manger.py::TestCustomerAdd::test_login",
    #              "test_crm_cust_manger.py::TestCustomerAdd::test_add_customer"])
    # pytest.main(["-v", "-s", "test_crm_cust_manger.py::TestLogin::test_login_success"])
    # pytest.main(["-v", "-s", "test_crm_cust_manger.py::TestCustomerAddOrder::test_student_refund"])
    # pytest.main(["-v", "-s", "test_crm_cust_manger.py::TestCustomerAddOrder"])
    # pytest.main(["-v", "-s", "test_crm_cust_manger.py::TestCustomerManagement::test_create_account"])
    #              "-v", "-s", "test_crm_cust_manger.py::TestCustomerAdd::test_convert_student"])
