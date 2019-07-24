import pytest
import sys
from time import sleep
from page.crm_student_management_page import GfyCrmStudentCourseManagement, GfyCrmStudentInClassManagement
from poium import PageWait, PageSelect
from test_dir.test_crm_cust_manger import login
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))


class TestStuCourseManagement:
    """
    学员课程管理
    """

    def test_student_select_class(self, browser1, crm_url, supervisor_account, pass_word, class_name):
        """
        单个学员分班
        :param browser1:
        :param crm_url:
        :param supervisor_account:
        :param pass_word:
        :param class_name:
        :return:
        """
        page = GfyCrmStudentCourseManagement(browser1)
        login(crm_url, browser1, supervisor_account, pass_word)
        PageWait(page.student_management)
        page.student_management.click()
        PageWait(page.student_course_management)
        page.student_course_management.click()
        PageWait(page.undivided_student)
        page.undivided_student.click()
        PageWait(page.student_select_class)
        # student_select_class默认选择第一个未分班的学
        page.student_select_class.click()
        PageWait(page.sch_course_class_search_classname)
        page.sch_course_class_search_classname.send_keys(class_name)
        page.sch_course_class_search_classname_button.click()
        PageWait(page.sch_course_class_search_classname_confirm)
        page.sch_course_class_search_classname_confirm.click()
        PageWait(page.student_select_class_status)
        assert page.student_select_class_status.text == "保存成功"


class TestStudentClassManagement:
    """
    学员上课管理
    """

    def test_add_in_class_record(self, browser1, crm_url, education_account, pass_word, class_name, school_name):
        """
        新增上课记录
        :return:
        """
        login(crm_url, browser1, education_account, pass_word)
        page = GfyCrmStudentInClassManagement(browser1)
        page2 = GfyCrmStudentCourseManagement(browser1)
        PageWait(page2.student_management)
        page2.student_management.click()
        PageWait(page.student_class_management)
        page.student_class_management.click()
        PageWait(page.add_in_class_record)
        page.add_in_class_record.click()
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
        page.makeup_in_class_date.click()
        sleep(1)
        page.makeup_in_class_date_today.click()
        PageWait(page.makeup_save)
        page.makeup_save.click()
        PageWait(page.makeup_status)
        assert page.makeup_status.text == "保存成功"
        page.makeup_in_class_status.click()

    def test_in_class(self, browser1, class_name, school_name):
        """
        上课点名
        :return:
        """
        page = GfyCrmStudentInClassManagement(browser1)
        sleep(1)
        PageSelect(page.teacher_class_list, text=class_name)
        sleep(1)
        PageSelect(page.in_class_school_list, text=school_name)
        sleep(1)
        PageSelect(page.in_class_status_list, text="未上课")
        PageWait(page.query_in_class_record)
        page.query_in_class_record.click()
        sleep(1)
        page.in_class_sign.click()
        PageWait(page.in_class_sign_save)
        page.in_class_sign_save.click()
        PageWait(page.in_class_sign_confirm)
        page.in_class_sign_confirm.click()
        PageWait(page.in_class_sign_status)
        assert page.in_class_sign_status.text == "保存成功"


class TestStudentOrderManagement:
    """
    学员订单管理
    """

    def test_student_refund(self, browser1, crm_url):
        pass


if __name__ == '__main__':
    # pytest.main()

    pytest.main(["-v", "-s", "test_crm_student_management.py::TestStudentClassManagement"])
