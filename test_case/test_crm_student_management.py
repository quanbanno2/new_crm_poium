import pytest
import sys
# 定义搜索模块顺序，优先搜索new_crm_poium文件夹
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.crm_menu_page import GfyMenu
from page.crm_home_page import GfyHomePage
from page.crm_customer_management_page import GfyCrmCustomerManagement
from page.crm_student_management_page import GfyStudentOrderManagement
from func.student_management_func import studentCourseManagement, add_new_order, pay_new_order, order_refund, \
    approval_matter, cal_refund_fee
from func.customer_management_func import login, add_customer_intent
from func.get_data import get_json_data
from func.xpath_element import by_xpath_contains, find_order_pay_info
from func.re_demo import re_demo
from func.db_func import DB
from func.finance_management_func import finance_management

from time import sleep
from poium import PageWait, PageSelect

# from conftest import DATA_DIR
from config import DATA_DIR


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
        # 我的客户列表loading不执行操作
        if customer_page.customer_loading:
            # 找到指定测试学员
            PageSelect(customer_page.customer_list_school_list,
                       text=schoolName)
            customer_page.customer_name_input.send_keys(studentName)
            customer_page.customer_list_load_button.click()
            # 进入综合信息管理
            sleep(1)
            by_xpath_contains(browser1, "a", studentName).click()
            sleep(1)
            # 添加跟进人和业务意向
            add_customer_intent(browser1, schoolName, activityType, activityName, responsibleDepartment,
                                responsibleName, case, teacherName, teacherDepartment)
            sleep(2)
            # 新增订单
            add_new_order(browser1, schoolName, courseName, case, subjectGroupType, subjectGroup, responsibleName,
                          teacherName)
            PageWait(order_page.order_status)
            assert order_page.order_status.text == msg

    @pytest.mark.parametrize(
        "case,status,loginAccount,password,schoolName,orderId,discount,otherFee,msg",
        get_json_data(DATA_DIR + "student_management" + "/pay_order.json")
    )
    def test_pay_new_order(self, crm_url, browser1, case, status, loginAccount, password, schoolName, orderId, discount,
                           otherFee, msg):
        """
        未缴费订单支付流程：已有订单订编号搜索订单-》添加优惠列表-》添加支付列表-》添加其他费用-》支付
        已缴部分：已有订单订编号搜索订单-》添加支付列表（计算未交部分进行缴费）-》支付
        """
        order_page = GfyStudentOrderManagement(browser1)
        menu_page = GfyMenu(browser1)
        login(crm_url, browser1, loginAccount, password)
        sleep(1)
        menu_page.student_management.click()
        if menu_page.menu_active:
            menu_page.student_order_management.click()
            # 等待订单管理界面loading完成
            if order_page.student_order_loading:
                PageSelect(order_page.student_order_school_id, text=schoolName)
                order_page.student_order_id.send_keys(orderId)
                order_page.order_info_loadStuOrderList.click()
                # 等待订单列表loading完成
                if order_page.student_order_loading:
                    paid_list = pay_new_order(browser1, case, discount, otherFee)
                    PageWait(order_page.pay_order_status)
                    try:
                        # 断言支付状态
                        assert order_page.pay_order_status.text == msg
                    finally:
                        try:
                            # 断言业绩计算状态
                            assert order_page.pay_order_calculation_status.text == msg
                        finally:
                            # 留在订单详情
                            order_page.pay_cancel_button.click()
                            if case == "未缴费支付":
                                try:
                                    # 断言缴费信息
                                    assert find_order_pay_info(browser1, "预收账款").text == paid_list[0]
                                finally:
                                    try:
                                        assert int(re_demo(find_order_pay_info(browser1, "优惠金额").text)) == discount
                                    finally:
                                        try:
                                            assert int(re_demo(find_order_pay_info(browser1, "其他费用").text)) == otherFee
                                        finally:
                                            DB().reset_order_status(status, orderId)
                            if case == "已缴部分支付":
                                try:
                                    # 预收账款是否等于订单已缴+未缴
                                    assert int(re_demo(find_order_pay_info(browser1, "预收账款").text)) == int(
                                        paid_list[0]) + int(paid_list[1])
                                finally:
                                    DB().reset_order_status(status, orderId)

    @pytest.mark.parametrize(
        "case,loginAccount,messageObject,approvalType,remindEventType,password,schoolName,orderId,shareTeacher,"
        "shareDepartment,msg",
        get_json_data(DATA_DIR + "student_management" + "/order_refund.json")
    )
    def test_student_refund(self, browser1, crm_url, case, loginAccount, messageObject, approvalType, remindEventType,
                            password, schoolName, orderId, shareTeacher, shareDepartment, msg):
        """
        测试客户退费
        """
        order_page = GfyStudentOrderManagement(browser1)
        menu_page = GfyMenu(browser1)
        home_page = GfyHomePage(browser1)
        DB().reset_order_class_status(case, orderId)
        login(crm_url, browser1, loginAccount, password)
        if menu_page.menu_loading:
            menu_page.student_management.click()
            # 等待目录展开
            if menu_page.menu_active:
                menu_page.student_order_management.click()
                if order_page.student_order_loading:
                    # 申请退费
                    fee_list = order_refund(browser1, schoolName, orderId, loginAccount)
                    try:
                        # 断言退费结算金额是否正确
                        assert cal_refund_fee(fee_list['refund_pre_fee'], fee_list['refund_course_count'],
                                              fee_list['refund_course_consume']) == float(fee_list['refund_fee'])
                    finally:
                        # 进入首页审批
                        menu_page.dashboard.click()
                        PageWait(home_page.more_remind)
                        # 审批
                        approval_matter(browser1, messageObject, fee_list['refund_name'], approvalType, remindEventType)
                        # 进入财务管理
                        menu_page.finance_menu.click()
                        sleep(1)
                        menu_page.finance_fee_info.click()
                        menu_page.finance_refund_info.click()
                        refund_result = finance_management.refund_info(browser1, orderId, shareDepartment, shareTeacher)
                        try:
                            # 部门业绩断言
                            assert float(fee_list['refund_fee']) == float(refund_result['department_fee'])
                        finally:
                            try:
                                # 个人业绩断言
                                assert float(fee_list['refund_fee']) == float(refund_result['personal_fee'])
                            finally:
                                try:
                                    # 退费结果断言
                                    assert refund_result['refunds_status'] == msg
                                finally:
                                    # 重置测试数据
                                    DB().reset_order_class_status(case, orderId)


#
class TestStuCourseManagement:
    """
    学员课程管理
    """

    @pytest.mark.parametrize(
        "case,operateAccount,password,studentCount,schoolName,courseParamsStatus,studentName,orderCourseId,"
        "objectClass,originClassId,msg", get_json_data(DATA_DIR + "student_management" + "/change_class.json"))
    def test_student_change_class(self, browser1, crm_url, case, operateAccount, password, studentCount, schoolName,
                                  courseParamsStatus, studentName, orderCourseId, objectClass, originClassId, msg):
        """
        测试学员换班流程
        @param browser1:
        @param crm_url:
        @param case:
        @param operateAccount:
        @param password:
        @param studentCount:
        @param schoolName:
        @param courseParamsStatus:
        @param studentName:
        @param objectClass:
        @param msg:
        @return:
        """
        course_page = GfyStudentOrderManagement(browser1)
        menu_page = GfyMenu(browser1)
        login(crm_url, browser1, operateAccount, password)
        order_course_id = orderCourseId.split(",")
        if menu_page.menu_loading:
            menu_page.student_management.click()
            if menu_page.menu_active:
                menu_page.student_course_management.click()
                # 等待课程查询loading
                if course_page.course_loading:
                    # 执行换班流程
                    assert_dict = studentCourseManagement.student_change_class(browser1, schoolName,
                                                                               courseParamsStatus, studentName,
                                                                               objectClass, studentCount,
                                                                               order_course_id)
                    try:
                        # 断言换班状态
                        assert assert_dict['changeStatus'] == msg
                    finally:
                        try:
                            for re in assert_dict['className']:
                                # 断言换班后状态是否等于目标班级
                                assert re == objectClass
                        finally:
                            DB().reset_order_course_status(order_course_id, originClassId)


# class TestStudentClassManagement:
#     """
#     学员上课管理
#     """
#
#     def test_add_in_class_record(self, browser1, crm_url, education_account, pass_word, class_name,
#     jigou_school_name,in_class_time):
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
    pytest.main(["-v", "-s", "test_crm_student_management.py"])
    # pytest.main(["-v", "-s", "test_crm_student_management.py::TestCustomerAddOrder::test_student_refund"])
    # pytest.main(["-v", "-s", "test_crm_student_management.py::TestStuCourseManagement::test_student_change_class"])
#         pytest.main(["-v", "-s", "test_crm_student_management.py::TestCustomerAddOrder::test_add_new_order"])
#     pytest.main(["-v", "-s", "test_crm_student_management.py::TestStudentClassManagement::test_in_class"])
#     # pytest.main(["-v", "-s", "test_crm_student_management.py::TestStudentClassManagement::test_leave",
#     #              "test_crm_student_management.py::TestStudentClassManagement::test_make_up"])
