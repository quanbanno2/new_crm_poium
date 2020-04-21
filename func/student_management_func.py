from time import sleep
from poium import PageWait, PageSelect
from page.crm_student_management_page import GfyCrmStudentCourseManagement, GfyCrmStudentInClassManagement, \
    GfyStudentOrderManagement
from page.crm_cust_manger_page import GfyCrmCustomerManagement
from page.crm_menu_page import GfyMenu
from func.db_func import DB


def add_new_order(driver, school_name, course_name, case, subject_group_type, subject_group, responsible_name,
                  teacher_name):
    """
    学员创建订单
    @param driver:
    @param school_name:
    @param course_name:
    @param case:
    @param subject_group_type:
    @param subject_group:
    @param responsible_name:
    @param teacher_name:
    @return:
    """
    order_page = GfyStudentOrderManagement(driver)
    order_page.customer_order_info.click()
    sleep(1)
    order_page.customer_order_add.click()
    sleep(1)
    # 顾问老师非空，执行新招生流程
    if case == "新招生":
        # 选择分成对象
        PageSelect(order_page.order_sharing_object_select[0], text=DB(
        ).get_account_info(responsible_name))
        sleep(1)
        order_page.order_sharing_object_select_btn.click()
    if case == "辅导续费":
        # 选择分成对象
        PageSelect(order_page.order_sharing_object_select[0], text=DB(
        ).get_account_info(teacher_name))
        PageSelect(order_page.order_sharing_object_select[1], text=DB(
        ).get_account_info(responsible_name))
        PageSelect(order_page.order_subject_group, text=subject_group_type)
        sleep(1)
        PageSelect(
            order_page.order_sharing_object_select[3], text=subject_group)
        while order_page.order_sharing_object_select_btn:
            order_page.order_sharing_object_select_btn.click()
    if case == "顾问转介绍":
        PageSelect(order_page.order_sharing_object_select[0], text=DB(
        ).get_account_info(responsible_name))
        PageSelect(order_page.order_sharing_object_select[1], text=DB(
        ).get_account_info(responsible_name))
        PageSelect(order_page.order_sharing_object_select[2], text=DB(
        ).get_account_info(teacher_name))
        while order_page.order_sharing_object_select_btn:
            order_page.order_sharing_object_select_btn.click()
    sleep(1)
    order_page.order_select_course.click()
    sleep(1)
    PageSelect(order_page.order_school_list, text=school_name)
    order_page.order_select_course_name.send_keys(course_name)
    sleep(1)
    order_page.order_select_course_name_query.click()
    sleep(1)
    order_page.order_select_course_btn.click()
    sleep(1)
    order_page.order_save_stu_order.click()


def pay_new_order(driver, case, status, order_id, discount, other_fee):
    """
    未缴费、已缴部分订单的支付
    @param order_id:
    @param driver:
    @param case:
    @param status:
    @param discount:
    @param other_fee:
    @return:
    """
    unpaid = ""
    paid = ""
    order_page = GfyStudentOrderManagement(driver)
    other_page = GfyCrmCustomerManagement(driver)
    # 进入订单详情支付
    order_page.student_order_pay_btn.click()
    if case == "未缴费支付":
        # 增加优惠
        PageWait(order_page.add_order_discount_btn)
        order_page.add_order_discount_btn.click()
        order_page.add_order_discount_fee.send_keys(discount)
        order_page.add_order_discount_save.click()
        # 增加支付项
        order_page.add_order_pay_btn.click()
        unpaid = order_page.order_unpaid.text
        order_page.add_order_pay_fee.send_keys(unpaid)
        order_page.add_order_pay_save_btn.click()
        # 增加其他费用
        order_page.add_order_other_btn.click()
        order_page.add_order_other_fee.send_keys(other_fee)
        order_page.add_order_other_save.click()
    elif case == "已缴部分支付":
        PageWait(order_page.add_order_pay_btn)
        sleep(1)
        driver.execute_script("arguments[0].click();", order_page.add_order_pay_btn)
        unpaid = order_page.order_unpaid.text
        paid = order_page.order_paid.text
        order_page.add_order_pay_fee.send_keys(unpaid)
        order_page.add_order_pay_save_btn.click()
    # 支付
    driver.execute_script("arguments[0].click();", order_page.pay_stu_order)
    sleep(1)
    other_page.confirm_btn.click()
    # 返回未交金额
    return unpaid, paid

# def refund_apply(driver, remarks):
#     """
#      订单退费
#     :param driver:
#     :param remarks:
#     :return: customer_name 客户名称、order_id_text 订单编号、refund_fee_text 应退费值
#     """
#     order_page = GfyCustomerAddOrder(driver)
#     sleep(1)
#     order_page.order_detail.click()
#     sleep(1)
#     driver.execute_script("arguments[0].click();", order_page.order_info_refund)
#     sleep(1)
#     # 获取预收款、订购数量、消耗数量、学员名称、订单编号
#     refund_pre_fee_text = order_page.refund_pre_fee.text
#     refund_course_count_text = order_page.refund_course_count.text
#     refund_course_consume_text = order_page.refund_course_consume.text
#     # 获取客户名称
#     customer_name = order_page.order_customer_name.text
#     # 获取订单编号
#     order_id_text = order_page.order_id.text
#     sleep(1)
#     order_page.refund_remark.send_keys(remarks)
#     sleep(1)
#     order_page.save_order_refund.click()
#     PageWait(order_page.approval_matter_setting)
#     PageSelect(order_page.approval_matter_setting, text="辅导督导1-->通知发起人")
#     sleep(1)
#     order_page.save_approval_matter.click()
#     sleep(1)
#     # 计算退费结算金额
#     refund_fee_text = cal_refund_fee(refund_pre_fee_text, refund_course_count_text, refund_course_consume_text)
#     return customer_name, order_id_text, refund_fee_text
#
#
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
#
#
# def set_content_by_id(driver, content_id, text):
#     """
#     文本框输入
#     :param driver:
#     :param content_id:
#     :param text:
#     :return:
#     """
#     js = 'document.getElementById("%s").innerHTML = "%s" ' % (content_id, text)
#     driver.execute_script(js)
#
#
# def set_content_by_name(driver, content_name, text):
#     """
#     文本框输入
#     :param driver:
#     :param content_name:
#     :param text:
#     :return:
#     """
#     js = 'document.getElementsByName("%s").innerHTML = "%s" ' % (content_name, text)
#     driver.execute_script(js)
#
#
# def student_select_class(driver, class_name):
#     """
#     学员分班
#     :param driver:
#     :param class_name:
#     :return:
#     """
#     menu_page = GfyMenu(driver)
#     page = GfyCrmStudentCourseManagement(driver)
#     sleep(1)
#     menu_page.student_course_management.click()
#     PageWait(page.undivided_student)
#     page.undivided_student.click()
#     sleep(1)
#     page.student_select_class[0].click()
#     sleep(1)
#     page.sch_course_class_search_class_name.send_keys(class_name)
#     sleep(1)
#     page.sch_course_class_search_class_name_button[0].click()
#     sleep(1)
#     page.sch_order_course_class_save.click()
#
#
# def add_in_class_record(driver, school_name, class_name, in_class_time):
#     """
#     指导老师新增上课记录
#     :param driver:驱动
#     :param school_name:学校名称
#     :param class_name:班级名称
#     :param in_class_time:上课时间
#     :return:
#     """
#     menu_page = GfyMenu(driver)
#     page = GfyCrmStudentInClassManagement(driver)
#     menu_page.student_management.click()
#     sleep(1)
#     menu_page.student_class_management.click()
#     sleep(1)
#     page.add_in_class_record.click()
#     sleep(1)
#     # 清除readonly属性
#     js = 'document.getElementsByName("inclassDate")[0].removeAttribute("readonly");'
#     driver.execute_script(js)
#     # 将input清空
#     js_clean = 'document.getElementsByName("inclassDate")[0].value=""'
#     driver.execute_script(js_clean)
#     sleep(1)
#     # 输入格式化时间
#     page.makeup_in_class_date.send_keys(in_class_time)
#     sleep(1)
#     PageSelect(page.makeup_school_list, text=school_name)
#     sleep(1)
#     page.makeup_class_name.click()
#     sleep(1)
#     page.select_a_classes_search.clear()
#     sleep(1)
#     page.select_a_classes_search.send_keys(class_name)
#     sleep(1)
#     page.select_a_classes.click()
#     sleep(1)
#     PageSelect(page.makeup_time_cycle, text="单次")
#     sleep(1)
#     page.makeup_save.click()
#
#
# def in_class(driver, class_name, school_name):
#     """
#     学生上课点名
#     :param driver:
#     :param class_name:
#     :param school_name:
#     :return:
#     """
#     in_class_page = GfyCrmStudentInClassManagement(driver)
#     sleep(1)
#     PageSelect(in_class_page.teacher_class_list, text=class_name)
#     sleep(1)
#     PageSelect(in_class_page.in_class_school_list, text=school_name)
#     sleep(1)
#     PageSelect(in_class_page.in_class_status_list, text="未上课")
#     sleep(1)
#     in_class_page.query_in_class_record.click()
#     sleep(1)
#     in_class_page.in_class_sign.click()
#     sleep(1)
#     in_class_page.in_class_sign_save.click()
#     PageWait(in_class_page.in_class_sign_confirm)
#     in_class_page.in_class_sign_confirm.click()
#
#
# def leave(driver):
#     """
#     学员请假
#     :param driver:
#     :return:
#     """
#     leave_page = GfyCrmStudentInClassManagement(driver)
#     leave_page.in_class_leave.click()
#     sleep(1)
#     # 点击"自动化测试学生"进行请假
#     leave_page.in_class_leave_student.click()
#     sleep(1)
#     PageSelect(leave_page.in_class_leave_type, text="公校原因")
#     sleep(1)
#     leave_page.in_class_leave_save.click()
#     sleep(1)
#
#
# def make_up(driver, student_name):
#     """
#     补课安排
#     :param driver:
#     :param student_name:补课学生
#     :return:
#     """
#     makeup_page = GfyCrmStudentInClassManagement(driver)
#     sleep(1)
#     makeup_page.make_up_student_name_input.send_keys(student_name)
#     sleep(1)
#     makeup_page.query_makeup_student.click()
#     sleep(2)
#     makeup_page.plan_student_makeup.click()
#     sleep(1)
#     makeup_page.makeup_select_class.click()
