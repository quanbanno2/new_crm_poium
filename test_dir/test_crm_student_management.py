import pytest
import sys
from time import sleep
from page.crm_student_management_page import GfyCrmStudentCourseManagement, GfyCrmStudentInClassManagement
from page.crm_menu_page import GfyMenu
from poium import PageWait, PageSelect
from test_dir.test_crm_cust_manger import login
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))


def student_select_class(driver, url, login_name, password, class_name):
    """
    学员分班
    :param driver:
    :param url:
    :param login_name:
    :param password:
    :param class_name:
    :return:
    """
    login(url, driver, login_name, password)
    page = GfyCrmStudentCourseManagement(driver)
    menu_page = GfyMenu(driver)
    PageWait(menu_page.student_management)
    menu_page.student_management.click()
    PageWait(menu_page.student_course_management)
    menu_page.student_course_management.click()
    PageWait(page.undivided_student)
    page.undivided_student.click()
    PageWait(page.student_select_class)
    page.student_select_class.click()
    PageWait(page.sch_course_class_search_classname)
    page.sch_course_class_search_classname.send_keys(class_name)
    page.sch_course_class_search_classname_button.click()
    PageWait(page.sch_course_class_search_classname_confirm)
    page.sch_course_class_search_classname_confirm.click()


def add_in_class_record(driver, school_name, class_name):
    """
    指导老师新增上课记录
    :param driver:
    :param school_name:
    :param class_name:
    :return:
    """
    page = GfyCrmStudentInClassManagement(driver)
    menu_page = GfyMenu(driver)
    PageWait(menu_page.student_management)
    menu_page.student_management.click()
    PageWait(menu_page.student_class_management)
    menu_page.student_class_management.click()
    sleep(1)
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


def in_class(driver, class_name, school_name):
    """
    学生上课点名
    :param driver:
    :param class_name:
    :param school_name:
    :return:
    """
    in_class_page = GfyCrmStudentInClassManagement(driver)
    sleep(1)
    PageSelect(in_class_page.teacher_class_list, text=class_name)
    sleep(1)
    PageSelect(in_class_page.in_class_school_list, text=school_name)
    sleep(1)
    PageSelect(in_class_page.in_class_status_list, text="未上课")
    PageWait(in_class_page.query_in_class_record)
    in_class_page.query_in_class_record.click()
    sleep(1)
    in_class_page.in_class_sign.click()
    PageWait(in_class_page.in_class_sign_save)
    in_class_page.in_class_sign_save.click()
    PageWait(in_class_page.in_class_sign_confirm)
    in_class_page.in_class_sign_confirm.click()


class TestStuCourseManagement:
    """
    学员课程管理
    """

    def test_student_select_class(self, browser1, crm_url, supervisor_account, pass_word, class_name):
        """
        单个学员分班
        :param browser1:
        :param crm_url:
        :param supervisor_account:高分云指导督导1账号
        :param pass_word:
        :param class_name:
        :return:
        """
        student_select_class(browser1, crm_url, supervisor_account, pass_word, class_name)
        page = GfyCrmStudentCourseManagement(browser1)
        sleep(1)
        assert page.student_select_class_status.text == "保存成功"
        page.student_select_class_ok.click()


class TestStudentClassManagement:
    """
    学员上课管理
    """

    def test_add_in_class_record(self, browser1, crm_url, education_account, pass_word, class_name, school_name):
        """
        测试指导老师新增上课记录
        :param browser1:
        :param crm_url:
        :param education_account: 高分云指导1账号
        :param pass_word:
        :param class_name:
        :param school_name:
        :return:
        """
        login(crm_url, browser1, education_account, pass_word)
        add_in_class_record(browser1, school_name, class_name)
        page = GfyCrmStudentInClassManagement(browser1)
        PageWait(page.status)
        assert page.status.text == "保存成功"
        page.makeup_in_class_status.click()

    def test_in_class(self, browser1, class_name, school_name):
        """
        上课点名
        :return:
        """
        in_class(browser1, class_name, school_name)
        sleep(1)
        page = GfyCrmStudentInClassManagement(browser1)
        PageWait(page.status)
        assert page.status.text == "保存成功"


if __name__ == '__main__':
    # pytest.main()

    # pytest.main(["-v", "-s", "test_crm_student_management.py::TestStuCourseManagement"])
    pytest.main(["-v", "-s", "test_crm_student_management.py::TestStudentClassManagement"])
