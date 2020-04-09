import pytest
import sys
from time import sleep
from poium import PageWait, PageSelect
# 定义搜索模块顺序，优先搜索new_crm_poium文件夹
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.crm_student_management_page import GfyCrmStudentCourseManagement, GfyCrmStudentInClassManagement, \
    GfyStudentOrderManagement
from page.crm_cust_manger_page import GfyCrmCustomerManagement
from page.crm_menu_page import GfyMenu
from func.db_func import DB
from func.get_data import get_json_data
from func.customer_management_func import login, add_customer_new, split_customer, convert_student, create_account, \
    add_customer_intent
from func.student_management_func import student_select_class, add_in_class_record, in_class, leave, make_up, \
    add_new_order
from conftest import DATA_DIR


class TestCustomerAddOrder:
    """
    学员新建订单和支付订单、未上课退费
    """

    @pytest.mark.parametrize(
        "case,loginAccount,password,activityType,schoolName,activityName,responsibleName,responsibleDepartment,"
        "teacherName,teacherDepartment,courseName,studentName,subjectGroupType,subjectGroup,msg",
        get_json_data(DATA_DIR + "student_management" + "/add_student_order.json")
    )
    def test_add_new_order(self, crm_url, browser1, case, loginAccount, password, activityType, schoolName,
                           activityName, responsibleName, responsibleDepartment, teacherName, teacherDepartment,
                           courseName, studentName, subjectGroupType, subjectGroup, msg):
        """
        测试学员创建订单
        """
        order_page = GfyStudentOrderManagement(browser1)
        menu_page = GfyMenu(browser1)
        customer_page = GfyCrmCustomerManagement(browser1)
        # 登录
        login(crm_url, browser1, loginAccount, password)
        sleep(1)
        # 进入客户管理-我的客户
        menu_page.customer_management.click()
        menu_page.my_customer.click()
        # 找到指定测试学员
        PageSelect(customer_page.customer_list_school_list, text=schoolName)
        customer_page.customer_name_input.send_keys(studentName)
        customer_page.customer_list_load_button.click()
        # 进入综合信息管理
        sleep(1)
        # customer_page.customer_name.click()
        browser1.find_element_by_xpath("//a[contains(.,'%s')]" % studentName).click()
        sleep(1)
        # 添加跟进人和业务意向
        add_customer_intent(browser1, schoolName, activityType, activityName, responsibleDepartment, responsibleName,
                            case, teacherName, teacherDepartment)
        sleep(2)
        # 新增订单
        add_new_order(browser1, schoolName, courseName, case, subjectGroupType, subjectGroup)
        PageWait(order_page.order_status)
        assert order_page.order_status.text == msg

    #
    #     def test_pay_new_order(self, crm_url, browser1, jigou_school_name, pass_word, phone_number, course,
    #                            counseling_supervision_name, counseling_supervision_account):
    #         """
    #         测试支付订单：添加优惠-添加支付-添加其他费用-添加分成对象
    #         @param crm_url:
    #         @param browser1:
    #         @param jigou_school_name:
    #         @param pass_word:
    #         @param phone_number:
    #         @param course:
    #         @param counseling_supervision_name:
    #         @param counseling_supervision_account:
    #         @return:
    #         """
    #         order_page = GfyCustomerAddOrder(browser1)
    #         login(crm_url, browser1, counseling_supervision_account, pass_word)
    #         add_customer(browser1, DB().new_customer_name_by_sql(), phone_number)
    #         sleep(1)
    #         split_customer(browser1, counseling_supervision_account)
    #         sleep(1)
    #         convert_student(browser1, jigou_school_name)
    #         sleep(1)
    #         order_page.ok_button.click()
    #         sleep(1)
    #         add_new_order(browser1, counseling_supervision_name, course, jigou_school_name)
    #         sleep(1)
    #         order_page.order_status_confirm.click()
    #         sleep(1)
    #         pay_new_order(browser1)
    #         # 断言是否支付成功
    #         sleep(3)
    #         assert order_page.pay_order_status.text == "成功"
    #         assert order_page.pay_order_calculation_status.text == "成功"
    #
    #     def test_student_refund(self, browser1, crm_url, supervisor_account, pass_word, remarks,
    #                             phone_number, course, jigou_school_name, today_date, educational_account,
    #                             counseling_supervision_account, counseling_supervision_name):
    #         """
    #         测试客户退费
    #         活动：新招生
    #         @param browser1:
    #         @param crm_url:
    #         @param supervisor_account:
    #         @param pass_word:
    #         @param remarks:
    #         @param phone_number:
    #         @param course:
    #         @param jigou_school_name:
    #         @param today_date:
    #         @param educational_account:
    #         @param counseling_supervision_account:
    #         @param counseling_supervision_name:
    #         @return:
    #         """
    #         order_page = GfyCustomerAddOrder(browser1)
    #         login(crm_url, browser1, counseling_supervision_account, pass_word)
    #         add_customer(browser1, DB().new_customer_name_by_sql(), phone_number)
    #         sleep(1)
    #         split_customer(browser1, counseling_supervision_account)
    #         sleep(1)
    #         convert_student(browser1, jigou_school_name)
    #         sleep(1)
    #         order_page.ok_button.click()
    #         sleep(1)
    #         add_new_order(browser1, counseling_supervision_name, course, jigou_school_name)
    #         sleep(1)
    #         order_page.order_status_confirm.click()
    #         sleep(1)
    #         pay_new_order(browser1)
    #         sleep(1)
    #         order_page.OK_button.click()
    #         sleep(1)
    #         refund_apply_list = refund_apply(browser1, remarks)
    #         refund_fee_text = refund_apply_list[2]
    #         order_id_text = refund_apply_list[1]
    #         customer_name = refund_apply_list[0]
    #         assert refund_fee_text == order_page.application_for_refund.get_attribute("value")
    #         assert order_page.approval_matter_status.text == "审批保存成功"
    #         sleep(1)
    #         order_page.order_status_confirm.click()
    #         sleep(1)
    #         # 首页审批退费
    #         home_page = GfyHomePage(browser1)
    #         menu_page = GfyMenu(browser1)
    #         menu_page.dashboard.click()
    #         sleep(1)
    #         home_page.more_home_remind.click()
    #         sleep(1)
    #         home_page.search_object_name_input.send_keys("退费申请:待审批")
    #         sleep(1)
    #         home_page.remind_content_search_input.send_keys(customer_name)
    #         sleep(1)
    #         home_page.remind_center_approve_btn.click()
    #         sleep(1)
    #         PageSelect(home_page.approval_matter_type, value="A05")
    #         sleep(1)
    #         home_page.approval_matter_approval_detail.click()
    #         sleep(1)
    #         home_page.approval_result_input.click()
    #         sleep(1)
    #         home_page.save_approval_result.click()
    #         sleep(1)
    #         assert home_page.status.text == "保存成功"
    #         # 财务管理进行确认退费
    #         home_page.ok_button.click()
    #         sleep(1)
    #         menu_page = GfyMenu(browser1)
    #         refund_page = GfyRefundInfo(browser1)
    #         menu_page.finance_menu.click()
    #         sleep(1)
    #         menu_page.finance_fee_info.click()
    #         sleep(1)
    #         menu_page.finance_refund_info.click()
    #         sleep(1)
    #         refund_page.refund_order_id_input.send_keys(order_id_text)
    #         sleep(1)
    #         refund_page.query_refund_info_btn.click()
    #         sleep(1)
    #         refund_page.refund_check_confirm_btn.click()
    #         sleep(1)
    #         refund_page.refund_confirm_btn.click()
    #         sleep(2)
    #         assert refund_page.refund_status.text == "已退费"

    #
    #
    # class TestStuCourseManagement:
    #     """
    #     学员课程管理
    #     """
    #
    #     def test_student_select_class(self, browser1, crm_url, counseling_supervision_account, pass_word, class_name,
    #                                   course, phone_number, jigou_school_name, counseling_supervision_name):
    #         """
    #         测试单个学员分班
    #         @param browser1:
    #         @param crm_url:
    #         @param counseling_supervision_account:
    #         @param pass_word:
    #         @param class_name:
    #         @param course:
    #         @param phone_number:
    #         @param jigou_school_name:
    #         @param counseling_supervision_name:
    #         @return:
    #         """
    #         customer_page = GfyCrmCustomerManagement(browser1)
    #         order_page = GfyCustomerAddOrder(browser1)
    #         student_page = GfyCrmStudentCourseManagement(browser1)
    #         login(crm_url, browser1, counseling_supervision_account, pass_word)
    #         add_customer(browser1, DB().new_customer_name_by_sql(), phone_number)
    #         sleep(1)
    #         split_customer(browser1, counseling_supervision_account)
    #         sleep(1)
    #         convert_student(browser1, jigou_school_name)
    #         sleep(1)
    #         customer_page.customer_ok_button.click()
    #         sleep(1)
    #         create_account(browser1, pass_word, jigou_school_name)
    #         sleep(1)
    #         customer_page.customer_ok_button.click()
    #         sleep(1)
    #         customer_page.customer_list.click()
    #         sleep(1)
    #         add_new_order(browser1, counseling_supervision_name, course, jigou_school_name)
    #         sleep(1)
    #         order_page.order_status_confirm.click()
    #         sleep(1)
    #         pay_new_order(browser1)
    #         PageWait(customer_page.cancel_btn)
    #         customer_page.cancel_btn.click()
    #         sleep(1)
    #         student_select_class(browser1, class_name)
    #         PageWait(student_page.student_select_class_status)
    #         assert student_page.student_select_class_status.text == "保存成功"
    #
    #
    # class TestStudentClassManagement:
    #     """
    #     学员上课管理
    #     """
    #
    #     def test_add_in_class_record(self, browser1, crm_url, education_account, pass_word, class_name, jigou_school_name,
    #                                  in_class_time):
    #         """
    #         测试指导老师新增上课记录
    #         :param browser1:
    #         :param crm_url:
    #         :param education_account:
    #         :param pass_word:
    #         :param class_name:
    #         :param jigou_school_name:
    #         :param in_class_time:
    #         :return:
    #         """
    #         page = GfyCrmStudentInClassManagement(browser1)
    #         login(crm_url, browser1, education_account, pass_word)
    #         add_in_class_record(browser1, jigou_school_name, class_name, in_class_time)
    #         # 保存成功状态，由于成功状态元素显示时间很短
    #         PageWait(page.status)
    #         assert page.status.text == "保存成功"
    #         # 断言完成后删除新增的上课记录
    #         page.ok_button.click()
    #         sleep(1)
    #         PageSelect(page.teacher_class_list, text=class_name)
    #         sleep(1)
    #         page.query_in_class_record.click()
    #         sleep(1)
    #         # 断言班级名称
    #         assert page.in_class_record.text == class_name
    #         PageWait(page.delete_button)
    #         page.delete_button.click()
    #
    #     def test_in_class(self, crm_url, counseling_supervision_account, pass_word, phone_number,
    #                       counseling_supervision_name, course, browser1, class_name, jigou_school_name,
    #                       education_account, in_class_time):
    #         """
    #         测试上课点名
    #         流程：新增客户-分单-转学员-创订单-支付-绑定账号-分班-新增上课记录-上课
    #         @param crm_url:
    #         @param counseling_supervision_account:
    #         @param pass_word:
    #         @param phone_number:
    #         @param counseling_supervision_name:
    #         @param course:
    #         @param browser1:
    #         @param class_name:
    #         @param jigou_school_name:
    #         @param education_account:
    #         @param in_class_time:
    #         @return:
    #         """
    #         customer_page = GfyCrmCustomerManagement(browser1)
    #         order_page = GfyCustomerAddOrder(browser1)
    #         in_class_page = GfyCrmStudentInClassManagement(browser1)
    #         login(crm_url, browser1, counseling_supervision_account, pass_word)
    #         add_customer(browser1, DB().new_customer_name_by_sql(), phone_number)
    #         sleep(1)
    #         split_customer(browser1, counseling_supervision_account)
    #         sleep(1)
    #         convert_student(browser1, jigou_school_name)
    #         sleep(1)
    #         customer_page.customer_ok_button.click()
    #         sleep(1)
    #         create_account(browser1, pass_word, jigou_school_name)
    #         sleep(1)
    #         customer_page.customer_ok_button.click()
    #         sleep(1)
    #         customer_page.customer_list.click()
    #         sleep(1)
    #         add_new_order(browser1, counseling_supervision_name, course, jigou_school_name)
    #         sleep(1)
    #         order_page.order_status_confirm.click()
    #         sleep(1)
    #         pay_new_order(browser1)
    #         # 支付完成留在当前页面
    #         PageWait(customer_page.cancel_btn)
    #         customer_page.cancel_btn.click()
    #         sleep(1)
    #         student_select_class(browser1, class_name)
    #         sleep(1)
    #         # 切换到"高分云指导1"登录
    #         login(crm_url, browser1, education_account, pass_word)
    #         # 增加上课记录
    #         add_in_class_record(browser1, jigou_school_name, class_name, in_class_time)
    #         sleep(1)
    #         in_class_page.ok_button.click()
    #         sleep(1)
    #         # 上课点名
    #         in_class(browser1, class_name, jigou_school_name)
    #         sleep(1)
    #         # 断言点名保存成功
    #         assert in_class_page.status.text == "保存成功"
    #
    #     def test_leave(self, crm_url, education_account, pass_word, browser1, jigou_school_name, class_name, in_class_time,
    #                    student_name):
    #         """
    #         测试请假
    #         前提：已配置班级和学生已订购分班，所以不使用全流程
    #         :param crm_url:
    #         :param education_account:
    #         :param pass_word:
    #         :param browser1:
    #         :param jigou_school_name:
    #         :param class_name:
    #         :param in_class_time:
    #         :param student_name:
    #         :return:
    #         """
    #         leave_page = GfyCrmStudentInClassManagement(browser1)
    #         menu_page = GfyMenu(browser1)
    #         login(crm_url, browser1, education_account, pass_word)
    #         sleep(1)
    #         # 老师新增上课记录
    #         add_in_class_record(browser1, jigou_school_name, class_name, in_class_time)
    #         sleep(1)
    #         leave_page.ok_button.click()
    #         sleep(1)
    #         PageSelect(leave_page.teacher_class_list, text=class_name)
    #         sleep(1)
    #         leave_page.query_in_class_record.click()
    #         sleep(1)
    #         # 请假操作
    #         leave(browser1)
    #         sleep(1)
    #         assert leave_page.status.text == "请假保存成功"
    #         sleep(1)
    #         leave_page.ok_button.click()
    #         sleep(1)
    #         # 删除上课记录
    #         leave_page.delete_button.click()
    #         PageWait(leave_page.ok_button)
    #         leave_page.ok_button.click()
    #         # 撤销请假记录
    #         sleep(1)
    #         menu_page.student_makeup_management.click()
    #         PageWait(leave_page.make_up_student_name_input)
    #         leave_page.make_up_student_name_input.send_keys(student_name)
    #         sleep(1)
    #         leave_page.query_makeup_student.click()
    #         sleep(1)
    #         leave_page.cancel_makeup.click()
    #         sleep(1)
    #         leave_page.cancel_makeup_confirm.click()
    #         sleep(1)
    #         leave_page.ok_button.click()
    #
    #     def test_make_up(self, browser1, crm_url, education_account, pass_word, jigou_school_name, make_up_class,
    #                      make_up_time, student_name, in_class_time, class_name):
    #         """
    #         测试补课
    #         添加上课记录-学员请假（指定学员）-添加补课记录（时间当前时间+1h）-安排补课-老师上课
    #         :param browser1:
    #         :param crm_url:
    #         :param education_account:
    #         :param pass_word:
    #         :param jigou_school_name:
    #         :param make_up_class:
    #         :param make_up_time:
    #         :param student_name:
    #         :param in_class_time:
    #         :param class_name:
    #         :return:
    #         """
    #         menu_page = GfyMenu(browser1)
    #         make_up_page = GfyCrmStudentInClassManagement(browser1)
    #         login(crm_url, browser1, education_account, pass_word)
    #         # 添加上课记录
    #         add_in_class_record(browser1, jigou_school_name, class_name, in_class_time)
    #         make_up_page.ok_button.click()
    #         sleep(1)
    #         # 请假操作
    #         PageSelect(make_up_page.teacher_class_list, text=class_name)
    #         sleep(1)
    #         make_up_page.query_in_class_record.click()
    #         sleep(1)
    #         leave(browser1)
    #         sleep(1)
    #         make_up_page.ok_button.click()
    #         sleep(1)
    #         # 删除上课记录
    #         make_up_page.delete_button.click()
    #         PageWait(make_up_page.ok_button)
    #         make_up_page.ok_button.click()
    #         sleep(1)
    #         # 添加补课记录
    #         menu_page.student_management.click()
    #         sleep(1)
    #         add_in_class_record(browser1, jigou_school_name, make_up_class, make_up_time)
    #         sleep(1)
    #         make_up_page.ok_button.click()
    #         sleep(1)
    #         # 安排补课
    #         menu_page.student_makeup_management.click()
    #         sleep(1)
    #         make_up(browser1, student_name)
    #         sleep(1)
    #         make_up_page.ok_button.click()
    #         sleep(1)
    #         # 老师上课
    #         menu_page.student_class_management.click()
    #         sleep(1)
    #         in_class(browser1, make_up_class, jigou_school_name)
    #         sleep(1)
    #         # 断言补课上课
    #         assert make_up_page.status.text == "保存成功"
    #         make_up_page.ok_button.click()
    #         sleep(1)
    #         menu_page.student_makeup_management.click()
    #         PageWait(make_up_page.make_up_student_name_input)
    #         make_up_page.make_up_student_name_input.send_keys(student_name)
    #         PageSelect(make_up_page.leave_status_select, text="全部")
    #         sleep(1)
    #         make_up_page.query_makeup_student.click()
    #         sleep(2)
    #         # 断言补课状态
    #         assert make_up_page.make_up_student_name[0].text == "已补课"
    #
    #


if __name__ == '__main__':
    #     pytest.main()
    pytest.main(["-v", "-s", "test_crm_student_management.py::TestCustomerAddOrder::test_add_new_order"])
#     # pytest.main(["-v", "-s", "test_crm_student_management.py::TestStuCourseManagement::test_student_select_class"])
#         pytest.main(["-v", "-s", "test_crm_student_management.py::TestCustomerAddOrder::test_add_new_order"])
#     pytest.main(["-v", "-s", "test_crm_student_management.py::TestStudentClassManagement::test_in_class"])
#     # pytest.main(["-v", "-s", "test_crm_student_management.py::TestStudentClassManagement::test_leave",
#     #              "test_crm_student_management.py::TestStudentClassManagement::test_make_up"])
