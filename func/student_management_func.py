from time import sleep
from poium import PageWait, PageSelect
from func.db_func import DB
from page.crm_student_management_page import GfyCrmStudentInClassManagement, GfyStudentOrderManagement
from page.crm_customer_management_page import GfyCrmCustomerManagement
from page.crm_home_page import GfyHomePage
from func.xpath_element import find_object_element


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
        ).get_account_name(responsible_name))
        sleep(1)
        order_page.order_sharing_object_select_btn.click()
    if case == "辅导续费":
        # 选择分成对象
        PageSelect(order_page.order_sharing_object_select[0], text=DB(
        ).get_account_name(teacher_name))
        PageSelect(order_page.order_sharing_object_select[1], text=DB(
        ).get_account_name(responsible_name))
        PageSelect(order_page.order_subject_group, text=subject_group_type)
        sleep(1)
        PageSelect(
            order_page.order_sharing_object_select[3], text=subject_group)
        while order_page.order_sharing_object_select_btn:
            order_page.order_sharing_object_select_btn.click()
    if case == "顾问转介绍":
        PageSelect(order_page.order_sharing_object_select[0], text=DB(
        ).get_account_name(responsible_name))
        PageSelect(order_page.order_sharing_object_select[1], text=DB(
        ).get_account_name(responsible_name))
        PageSelect(order_page.order_sharing_object_select[2], text=DB(
        ).get_account_name(teacher_name))
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


def pay_new_order(driver, case, discount, other_fee):
    """
    未缴费、已缴部分订单的支付
    @param driver:
    @param case:
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
        if order_page.order_detail_loading != "":
            # 等待订单信息加载完成
            unpaid = order_page.order_unpaid.text
            paid = order_page.order_paid.text
            driver.execute_script("arguments[0].click();", order_page.add_order_pay_btn)
            order_page.add_order_pay_fee.send_keys(unpaid)
            order_page.add_order_pay_save_btn.click()
    # 支付
    driver.execute_script("arguments[0].click();", order_page.pay_stu_order)
    PageWait(other_page.confirm_btn)
    other_page.confirm_btn.click()
    # 返回未交金额
    return unpaid, paid


def order_refund(driver, school_name, order_id, teacher_account):
    """
    课程退费
    @param teacher_account:
    @param order_id:
    @param driver:
    @param school_name:
    @return 退费学员姓名、预收款、课程总数、课程消耗、结算框的退费金额
    """
    order_page = GfyStudentOrderManagement(driver)
    # 选择校区
    PageSelect(order_page.student_order_school_id, text=school_name)
    # 输入订单号
    order_page.student_order_id.send_keys(order_id)
    # 查询
    order_page.order_info_loadStuOrderList.click()
    # 等待订单管理loading完成
    if order_page.student_order_loading:
        order_page.order_detail[0].click()
        # 等待订单详情loading完成
        if order_page.order_detail_loading:
            order_page.order_info_refund.click()
            if order_page.order_refund_application:
                refund_name = order_page.refund_name.text
                refund_pre_fee = order_page.refund_pre_fee.text
                refund_course_count = order_page.refund_course_count.text
                refund_course_consume = order_page.refund_course_consume.text
                refund_fee = order_page.refund_fee.get_attribute("value")
                order_page.save_order_refund.click()
                sleep(3)
                # 等待审批事项确认界面loading完成
                approvalList = "%s-->通知发起人" % DB().get_account_name(teacher_account)
                if order_page.order_confirm_loading != "":
                    # 选择审批流程，只支持一个审批人
                    # approvalList = "%s-->通知发起人" % DB().get_account_name(teacher_account)
                    sleep(1)
                    PageSelect(order_page.approval_matter_setting, text=approvalList)
                    # 审批发起确认
                    order_page.save_approval_matter.click()
                    PageWait(order_page.ok_button)
                    order_page.ok_button.click()

                fee_list = {'refund_name': refund_name, 'refund_pre_fee': refund_pre_fee,
                            'refund_course_count': refund_course_count, 'refund_course_consume': refund_course_consume,
                            'refund_fee': refund_fee}
                return fee_list


def approval_matter(driver, message_object, refund_student, approval_type, remind_event_type):
    """
    审批事项
    @param remind_event_type:
    @param driver:
    @param message_object:
    @param refund_student:
    @param approval_type:
    @return:
    """
    home_page = GfyHomePage(driver)
    home_page.more_remind.click()
    PageWait(home_page.remind_center_approve_btn)
    PageSelect(home_page.remind_type, value=remind_event_type)
    home_page.message_object_input.send_keys(message_object)
    home_page.message_content.send_keys(refund_student)
    sleep(1)
    home_page.remind_center_approve_btn.click()
    # 等待审批事项界面loading完成
    if home_page.approval_matter_loading:
        PageSelect(home_page.approval_matter_type, value=approval_type)
        if home_page.approval_matter_loading:
            # 进入审批流程界面
            home_page.approval_matter_approval_detail.click()
            sleep(1)
            # 勾选审批通过
            home_page.approval_result_input.click()
            # 保存审批结果
            home_page.save_approval_result.click()
            PageWait(home_page.ok_button)
            home_page.ok_button.click()


def cal_refund_fee(pre_fee, course_count, course_consume):
    """
    计算退费结算金额 = 预收 - （预收/课程总量*消耗课程数量）
    :param pre_fee:预收金额
    :param course_count:课程总数量
    :param course_consume:已消耗课程
    :return:退费结果
    """
    pre_fee = float(pre_fee)
    course_count = float(course_count)
    course_consume = float(course_consume)
    refund_fee = pre_fee - (pre_fee / course_count * course_consume)
    # 保留两位、四舍五入,以字符串格式返回
    # return str(Context(prec=6, rounding=ROUND_HALF_UP).create_decimal(refund_fee))
    refund_fee = "%.2f" % refund_fee
    refund_fee = float(refund_fee)
    return refund_fee


class studentCourseManagement:

    @staticmethod
    def student_change_class(driver, school_id, course_params_status, student_name, class_name, student_count,
                             order_course_id):
        """

        @param order_course_id:
        @param driver:
        @param school_id:
        @param course_params_status:
        @param student_name:
        @param class_name:
        @param student_count:
        @return: 学员分班保存状态
        """
        i = 0
        className = []
        # order_course_id = order_course_id.split(",")
        course_page = GfyStudentOrderManagement(driver)
        # 已分班界面
        course_page.course_management_Divided.click()
        # 选择校区
        PageSelect(course_page.course_school_id, text=school_id)
        # 选择在校状态
        PageSelect(course_page.course_params_status, text=course_params_status)
        # 输入学院名称
        course_page.course_student_name.send_keys(student_name)
        # 移除教学老师
        course_page.course_set_teacher_close.click()
        # 查询
        course_page.course_management_query.click()
        find_object = find_object_element(driver)
        if course_page.course_loading:
            # 勾选学员
            while i < len(order_course_id):
                course_page.course_checkbox[i].click()
                i += 1
            # 批量换班按钮
            course_page.batch_change_class.click()
            # 等待班级列表loading完成
            if course_page.class_loading:
                # 输入目标班级名称
                course_page.class_name.send_keys(class_name)
                # 选择目标班级
                course_page.class_choice.click()
                # 等待分班确认模态框loading完成
                if course_page.confirm_dialog_loading:
                    # 确定保存
                    course_page.save_change_class.click()
                    # 等待换班状态弹出
                    PageWait(driver.find_element_by_xpath("//p[contains(.,'学员分班保存')]/b"))
                    # 获得换班状态
                    changeStatus = driver.find_element_by_xpath("//p[contains(.,'学员分班保存')]/b").text
                    sleep(1)
                    # 获取换班后的班级名称
                    for re in order_course_id:
                        className.append(find_object.find_course_class(re).text)
                    course_page.ok_button.click()
                    assert_dict = {"changeStatus": changeStatus, "className": className}
                    return assert_dict

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
