from time import sleep
from poium import PageWait, PageSelect
from page.crm_student_management_page import GfyCrmStudentCourseManagement, GfyCrmStudentInClassManagement
from page.crm_menu_page import GfyMenu


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
    page.select_a_classes_search.clear()
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
    in_class_page = GfyCrmStudentInClassManagement(driver)
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
    # 点击"自动化测试学生"进行请假
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
    makeup_page.make_up_student_name_input.send_keys(student_name)
    sleep(1)
    makeup_page.query_makeup_student.click()
    sleep(2)
    makeup_page.plan_student_makeup.click()
    sleep(1)
    makeup_page.makeup_select_class.click()