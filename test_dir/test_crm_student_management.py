import pytest
import sys
from time import sleep
from test_dir.test_crm_cust_manger import login, new_student_name, add_customer, split_customer, convert_student, \
    create_account, add_new_order, pay_new_order
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))

from page.crm_student_management_page import GfyCrmStudentCourseManagement, GfyCrmStudentInClassManagement
from page.crm_cust_manger_page import GfyCrmCustomerManagement, GfyCustomerAddOrder
from page.crm_menu_page import GfyMenu
from poium import PageWait, PageSelect


def student_select_class(driver, class_name):
    """
    学员分班
    :param driver:
    :param class_name:
    :return:
    """
    menu_page = GfyMenu(driver)
    page = GfyCrmStudentCourseManagement(driver)
    sleep(1)
    menu_page.student_course_management.click()
    PageWait(page.undivided_student)
    page.undivided_student.click()
    sleep(1)
    page.student_select_class[0].click()
    sleep(1)
    page.sch_course_class_search_class_name.send_keys(class_name)
    sleep(1)
    page.sch_course_class_search_class_name_button[0].click()
    sleep(1)
    page.sch_order_course_class_save.click()


def add_in_class_record(driver, school_name, class_name, in_class_time):
    """
    指导老师新增上课记录
    :param driver:驱动
    :param school_name:学校名称
    :param class_name:班级名称
    :param in_class_time:上课时间
    :return:
    """
    menu_page = GfyMenu(driver)
    page = GfyCrmStudentInClassManagement(driver)
    PageWait(menu_page.student_management)
    menu_page.student_management.click()
    sleep(1)
    menu_page.student_class_management.click()
    sleep(1)
    page.add_in_class_record.click()
    sleep(1)
    # 清除readonly属性
    js = 'document.getElementsByName("inclassDate")[0].removeAttribute("readonly");'
    driver.execute_script(js)
    # 将input清空
    js_clean = 'document.getElementsByName("inclassDate")[0].value=""'
    driver.execute_script(js_clean)
    sleep(1)
    # 输入格式化时间
    page.makeup_in_class_date.send_keys(in_class_time)
    sleep(1)
    PageSelect(page.makeup_school_list, text=school_name)
    sleep(1)
    page.makeup_class_name.click()
    sleep(1)
    page.select_a_classes_search.send_keys(class_name)
    sleep(1)
    page.select_a_classes.click()
    sleep(1)
    PageSelect(page.makeup_time_cycle, text="单次")
    sleep(1)
    page.makeup_save.click()


def in_class(driver, class_name, school_name):
    """
    学生上课点名
    :param driver:
    :param class_name:
    :param school_name:
    :return:
    """
    menu_page = GfyMenu(driver)
    in_class_page = GfyCrmStudentInClassManagement(driver)
    PageWait(menu_page.student_management)
    menu_page.student_management.click()
    sleep(1)
    menu_page.student_class_management.click()
    sleep(1)
    PageSelect(in_class_page.teacher_class_list, text=class_name)
    sleep(1)
    PageSelect(in_class_page.in_class_school_list, text=school_name)
    sleep(1)
    PageSelect(in_class_page.in_class_status_list, text="未上课")
    sleep(1)
    in_class_page.query_in_class_record.click()
    sleep(1)
    in_class_page.in_class_sign.click()
    sleep(1)
    in_class_page.in_class_sign_save.click()
    PageWait(in_class_page.in_class_sign_confirm)
    in_class_page.in_class_sign_confirm.click()


def leave(driver):
    """
    学员请假
    :param driver:
    :return:
    """
    leave_page = GfyCrmStudentInClassManagement(driver)
    leave_page.in_class_leave.click()
    sleep(1)
    leave_page.in_class_leave_student.click()
    sleep(1)
    PageSelect(leave_page.in_class_leave_type, text="公校原因")
    sleep(1)
    leave_page.in_class_leave_save.click()
    sleep(1)


def make_up(driver, student_name):
    """
    补课安排
    :param driver:
    :param student_name:补课学生
    :return:
    """
    makeup_page = GfyCrmStudentInClassManagement(driver)
    sleep(1)
    makeup_page.make_up_student_name.send_keys(student_name)
    sleep(1)
    makeup_page.query_makeup_student.click()
    sleep(1)
    makeup_page.plan_student_makeup.click()
    sleep(1)
    makeup_page.makeup_select_class.click()


class TestStuCourseManagement:
    """
    学员课程管理
    """

    def test_student_select_class(self, browser1, crm_url, counseling_supervision_account, adviser_account, pass_word,
                                  class_name, course, adviser_name,
                                  phone_number, school_name):
        """
        测试单个学员分班
        :param browser1:
        :param crm_url:
        :param counseling_supervision_account:
        :param adviser_account:
        :param pass_word:
        :param class_name:
        :param course:
        :param adviser_name:
        :param phone_number:
        :param school_name:
        :return:
        """
        customer_page = GfyCrmCustomerManagement(browser1)
        order_page = GfyCustomerAddOrder(browser1)
        student_page = GfyCrmStudentCourseManagement(browser1)
        login(crm_url, browser1, counseling_supervision_account, pass_word)
        add_customer(browser1, new_student_name(), phone_number)
        sleep(1)
        split_customer(browser1, adviser_account, school_name)
        sleep(1)
        convert_student(browser1, school_name)
        sleep(1)
        customer_page.customer_ok_button.click()
        sleep(1)
        create_account(browser1, pass_word, school_name)
        sleep(1)
        customer_page.customer_ok_button.click()
        sleep(1)
        customer_page.customer_list.click()
        sleep(1)
        add_new_order(browser1, adviser_name, course, school_name)
        sleep(1)
        order_page.order_status_confirm.click()
        sleep(1)
        pay_new_order(browser1)
        PageWait(customer_page.cancel_btn)
        customer_page.cancel_btn.click()
        sleep(1)
        student_select_class(browser1, class_name)
        PageWait(student_page.student_select_class_status)
        assert student_page.student_select_class_status.text == "保存成功"


class TestStudentClassManagement:
    """
    学员上课管理
    """

    def test_add_in_class_record(self, browser1, crm_url, education_account, pass_word, class_name, school_name,
                                 in_class_time):
        """
        测试指导老师新增上课记录
        :param browser1:
        :param crm_url:
        :param education_account:
        :param pass_word:
        :param class_name:
        :param school_name:
        :param in_class_time:
        :return:
        """
        page = GfyCrmStudentInClassManagement(browser1)
        login(crm_url, browser1, education_account, pass_word)
        add_in_class_record(browser1, school_name, class_name, in_class_time)
        # 保存成功状态，由于成功状态元素显示时间很短
        PageWait(page.status)
        assert page.status.text == "保存成功"
        # 断言完成后删除新增的上课记录
        page.ok_button.click()
        sleep(1)
        PageSelect(page.teacher_class_list, text=class_name)
        sleep(1)
        page.query_in_class_record.click()
        sleep(1)
        # 断言班级名称
        assert page.in_class_record.text == class_name
        PageWait(page.delete_button)
        page.delete_button.click()

    def test_in_class(self, crm_url, counseling_supervision_account, pass_word, phone_number, adviser_account,
                      adviser_name, course, browser1, class_name, school_name, education_account, in_class_time):
        """
        测试上课点名
        流程：新增客户-分单-转学员-创订单-支付-绑定账号-分班-新增上课记录-上课
        :param browser1:
        :param class_name:
        :param school_name:
        :return:
        """
        customer_page = GfyCrmCustomerManagement(browser1)
        order_page = GfyCustomerAddOrder(browser1)
        in_class_page = GfyCrmStudentInClassManagement(browser1)
        menu_page = GfyMenu(browser1)
        login(crm_url, browser1, counseling_supervision_account, pass_word)
        add_customer(browser1, new_student_name(), phone_number)
        sleep(1)
        split_customer(browser1, adviser_account, school_name)
        sleep(1)
        convert_student(browser1, school_name)
        sleep(1)
        customer_page.customer_ok_button.click()
        sleep(1)
        create_account(browser1, pass_word, school_name)
        sleep(1)
        customer_page.customer_ok_button.click()
        sleep(1)
        customer_page.customer_list.click()
        sleep(1)
        add_new_order(browser1, adviser_name, course, school_name)
        sleep(1)
        order_page.order_status_confirm.click()
        sleep(1)
        pay_new_order(browser1)
        # 支付完成留在当前页面
        PageWait(customer_page.cancel_btn)
        customer_page.cancel_btn.click()
        sleep(1)
        student_select_class(browser1, class_name)
        sleep(1)
        # 切换到"高分云指导1"登录
        login(crm_url, browser1, education_account, pass_word)
        # 增加上课记录
        add_in_class_record(browser1, school_name, class_name, in_class_time)
        sleep(1)
        in_class_page.ok_button.click()
        sleep(1)
        menu_page.student_management.click()
        sleep(1)
        # 上课点名
        in_class(browser1, class_name, school_name)
        sleep(1)
        # 断言点名保存成功
        assert in_class_page.status.text == "保存成功"

    def test_leave(self, crm_url, education_account, pass_word, browser1, school_name, class_name, in_class_time,
                   phone_number, adviser_account, adviser_name, course, ):
        """
        测试请假
        流程：创建客户-创建账号-创建订单-支付-分班-请假
        :param crm_url:
        :param education_account:
        :param pass_word:
        :param browser1:
        :param school_name:
        :param class_name:
        :param in_class_time:
        :return:
        """
        leave_page = GfyCrmStudentInClassManagement(browser1)
        customer_page = GfyCrmCustomerManagement(browser1)
        menu_page = GfyMenu(browser1)
        order_page = GfyCustomerAddOrder(browser1)
        login(crm_url, browser1, education_account, pass_word)
        sleep(1)
        add_customer(browser1, new_student_name(), phone_number)
        sleep(1)
        # 分单
        split_customer(browser1, adviser_account, school_name)
        sleep(1)
        # 转学员
        convert_student(browser1, school_name)
        sleep(1)
        customer_page.customer_ok_button.click()
        sleep(1)
        # 创建账号
        create_account(browser1, pass_word, school_name)
        sleep(1)
        customer_page.customer_ok_button.click()
        sleep(1)
        customer_page.customer_list.click()
        sleep(1)
        # 创建订单
        add_new_order(browser1, adviser_name, course, school_name)
        sleep(1)
        order_page.order_status_confirm.click()
        sleep(1)
        # 支付
        pay_new_order(browser1)
        sleep(1)
        menu_page.student_management.click()
        sleep(1)
        menu_page.student_class_management.click()
        sleep(1)
        # 老师新增上课记录
        add_in_class_record(browser1, school_name, class_name, in_class_time)
        sleep(1)
        leave_page.ok_button.click()
        sleep(1)
        PageSelect(leave_page.teacher_class_list, text=class_name)
        sleep(1)
        # 查询新增上课记录
        leave_page.query_in_class_record.click()
        sleep(1)
        leave(browser1)
        sleep(1)
        assert leave_page.status.text == "请假保存成功"
        sleep(1)
        leave_page.ok_button.click()
        sleep(1)
        # 删除上课记录
        leave_page.delete_button.click()

    def test_make_up(self, browser1, crm_url, education_account, pass_word, school_name, make_up_class, make_up_time,
                     student_name):
        """
        测试补课
        :param browser1:
        :param crm_url:
        :param education_account:
        :param pass_word:
        :param school_name:
        :param make_up_class:
        :param make_up_time:
        :param student_name:
        :return:
        """
        login(crm_url, browser1, education_account, pass_word)
        menu_page = GfyMenu(browser1)
        PageWait(menu_page.student_management)
        menu_page.student_management.click()
        PageWait(menu_page.student_class_management)
        menu_page.student_class_management.click()
        sleep(1)
        # 添加补课记录
        add_in_class_record(browser1, school_name, make_up_class, make_up_time)
        sleep(1)
        make_up_page = GfyCrmStudentInClassManagement(browser1)
        make_up_page.ok_button.click()
        sleep(1)
        # 安排补课
        menu_page.student_makeup_management.click()
        sleep(1)
        make_up(browser1, student_name)
        sleep(1)
        assert make_up_page.status.text == "保存成功"
        sleep(1)
        make_up_page.ok_button.click()
        sleep(1)
        menu_page.student_class_management.click()
        sleep(1)
        # 补课老师补课
        in_class(browser1, make_up_class, school_name)
        sleep(1)
        assert make_up_page.status.text == "保存成功"


if __name__ == '__main__':
    # pytest.main()
    # pytest.main(["-v", "-s", "test_crm_student_management.py::TestStuCourseManagement::test_student_select_class"])
    pytest.main(["-v", "-s", "test_crm_student_management.py::TestStudentClassManagement::test_add_in_class_record"])
    # pytest.main(["-v", "-s", "test_crm_student_management.py::TestStudentClassManagement::test_leave",
    #              "test_crm_student_management.py::TestStudentClassManagement::test_make_up"])
