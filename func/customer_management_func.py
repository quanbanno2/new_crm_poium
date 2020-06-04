from time import sleep
from poium import PageWait, PageSelect
from page.crm_customer_management_page import GfyCrmCustomerManagement
from page.crm_menu_page import GfyMenu
from page.crm_login_page import GfyLogin
from func.xpath_element import by_xpath_contains
from func.find_element_by_js import find_js_element


class customerManagementFunc:

    def __init__(self, driver):
        self.driver = driver
        self.customer_page = GfyCrmCustomerManagement(driver)

    def customer_communication(self, communication_info, communication_result, is_visit, next_day):
        """
        新增客户沟通邀约流程
        @param next_day:
        @param is_visit:
        @param communication_result:
        @param communication_info:
        @return:
        """
        customer_page = self.customer_page
        customer_page.communication_info.click()
        # 等待沟通界面加载完成
        sleep(1)
        # 新增沟通信息
        customer_page.communication_add.click()
        # 等待新增沟通信息模态框
        sleep(1)
        # 点击添加跟进人
        customer_page.communicate_liable.click()
        # 等待跟进人列表加载完成
        if customer_page.responsible_list_loading != "None":
            customer_page.choose_teacher_button.click()
            # 输入沟通内容
            customer_page.textarea.send_keys(communication_info)
            # 勾选沟通结果
            by_xpath_contains(self.driver, "label", communication_result).click()
            # 勾选承诺到访
            self.driver.find_element_by_xpath(
                "//th[text()='承诺到访']/following::td/label[contains(.,'{}')]".format(is_visit))
            if is_visit == "是":
                visitDate = customer_page.visit_date
                # 清除到会日期readonly
                self.driver.execute_script(find_js_element.remove_attribute("readonly"), visitDate)
                # 输入到会时间
                visitDate.send_keys(next_day)
                # 保存沟通记录
            customer_page.save_communication.click()
            PageWait(customer_page.save_status)
            save_status = customer_page.save_status.text
            # 得到沟通结果
            communicationResult = customer_page.communicate_result.text
            # 得到承诺到访结果
            isVisit = customer_page.is_visit.text
            # 返回保存状态、沟通结果、是否到访
            assert_dict = {"save_status": save_status, "communication_result": communicationResult,
                           "is_visit": isVisit}
            return assert_dict

    def customer_meeting(self, is_visit, parent):
        """
        客户到会确认
        @param is_visit:
        @param parent:
        @return:
        """
        customer_page = self.customer_page
        customer_page.meeting_info.click()
        if customer_page.meeting_loading:
            # 诺到会自动生成到会信息直接确认
            if is_visit == "是":
                customer_page.confirm_meeting.click()
                # PageWait(customer_page.meeting_meeting_dialog)
                PageSelect(customer_page.meeting_confirm_parent_name, text=parent)
                # 确认到会
                customer_page.save_meeting_confirm.click()
                PageWait(customer_page.save_status)
                save_status = customer_page.save_status.text
                if customer_page.meeting_loading:
                    meetingResult = customer_page.meeting_result.text
                    # 返回到会保存状态、到会结果
                    assert_dict = {"save_status": save_status, "meetingResult": meetingResult}
                    return assert_dict
        else:
            print("暂不支持非诺到会流程")
        # # 非诺到会需要手动新建到会信息再确认到会
        # else:
        #     customer_page.meeting_add.click()
        #     customer_page.meeting_liable_name.click()
        #     if customer_page.responsible_list_loading:
        #         customer_page.choose_a_teacher.click()
        #         # 新增到会信息，选择陪同人
        #         PageSelect(customer_page.meeting_add_parent_name, text=parent)

    def customer_admit(self):
        """
        接待客户
        @return:
        """
        customer_page = self.customer_page
        # 点击接待信息
        customer_page.interview_info.click()
        # 等待加接待信息loading
        if customer_page.interview_loading != "None":
            # 添加接待信息按钮
            customer_page.interview_add.click()
            customer_page.admit_liable_name.click()
            if customer_page.responsible_list_loading != "None":
                # 选中老师
                sleep(1)
                customer_page.choose_teacher_button.click()
                customer_page.save_admit.click()
                if customer_page.interview_loading != "None":
                    customer_page.confirm_admit.click()
                    customer_page.confirm_btn.click()
                    PageWait(customer_page.save_status)
                    # 获取保存状态
                    save_status = customer_page.save_status.text
                    if customer_page.interview_loading != "None":
                        # 获取接待结果
                        admit_result = customer_page.admit_result.text
                        assert_dict = {"save_status": save_status, "admit_result": admit_result}
                        return assert_dict


def login(url, driver, account, password):
    """
    登录
    :param url:
    :param driver:
    :param account:
    :param password:
    :return:
    """
    page = GfyLogin(driver)
    page.get(url)
    page.login_input.send_keys(account)
    page.pwd_input.send_keys(password)
    code = page.verification_code.text
    page.code_input.send_keys(code)
    page.enter.click()
    sleep(1)


def add_customer(driver, customer_name, business_type, activity_name, phone_number, school_name):
    """
    创建客户
    @param driver:
    @param customer_name:
    @param business_type:
    @param activity_name:
    @param phone_number:
    @param school_name:
    @return:
    """
    page = GfyCrmCustomerManagement(driver)
    menu_page = GfyMenu(driver)
    menu_page.customer_management.click()
    menu_page.my_customer.click()
    if page.customer_loading:
        page.add_customer.click()
        sleep(2)
        # 输入客户名称
        page.add_customer_name.send_keys(customer_name)
        sleep(1)
        # 输入公校名称
        if school_name != "":
            page.school_name.click()
            PageWait(page.pub_school_list)
            page.pub_school_list.send_keys(school_name)
            page.pub_school_query.click()
            PageWait(page.pub_school_choice)
            page.pub_school_choice.click()
        # 选择年级
        PageWait(page.grade[0])
        PageSelect(page.grade[0], value='string:G09')
        # 选择业务类型
        if business_type != "":
            PageSelect(page.customer_business_type, text=business_type)
        # 选择活动来源
        if activity_name != "":
            page.customer_activity.click()
            sleep(1)
            page.activity_name.send_keys(activity_name)
            page.activity_query.click()
            sleep(1)
            page.activity_selected.click()
            sleep(1)
        page.customer_phone.send_keys(phone_number)
        page.add_customer_save[0].click()


def add_educational(driver, educational_effect_time, educational_account):
    """
    添加教务老师
    :param driver:
    :param educational_effect_time: 教务老师生效时间
    :param educational_account: 教务老师登录账号
    :return:
    """
    page = GfyCrmCustomerManagement(driver)
    menu_page = GfyMenu(driver)
    menu_page.customer_management.click()
    sleep(1)
    menu_page.my_customer.click()
    sleep(1)
    page.first_student_name.click()
    sleep(1)
    page.student_educational.click()
    sleep(1)
    page.student_educational_add.click()
    sleep(1)
    page.educational_account_name.click()
    sleep(1)
    PageSelect(page.teacher_list_school, value="number:24")
    sleep(1)
    PageSelect(page.teacher_attribution_department, text="全部")
    sleep(1)
    page.teacher_list_login_name.send_keys(educational_account)
    sleep(1)
    page.teacher_list_query.click()
    sleep(1)
    page.choose_teacher_a.click()
    sleep(1)
    js = 'document.getElementsByName("effDate")[0].removeAttribute("readonly");'
    driver.execute_script(js)
    sleep(1)
    page.educational_effect_date.send_keys(educational_effect_time)
    sleep(1)
    page.student_educational_save.click()


def split_customer(driver, adviser_account, customer_num=None):
    """
    学员分单功能
    @param driver:
    @param adviser_account:跟进人
    @param customer_num:客户数量
    @return:
    """
    i = 0
    page = GfyCrmCustomerManagement(driver)
    if customer_num == 1 or customer_num is None:
        # 勾选列表第一个客户
        page.customer_check[0].click()
    else:
        # 勾选多个客户
        while i < customer_num:
            page.customer_check[i].click()
            i += 1
    # 分单按钮
    page.customer_split.click()
    sleep(1)
    # 输入账号查询
    page.teacher_list_login_name.clear()
    page.teacher_list_login_name.send_keys(adviser_account)
    # 机构老师列表查询
    page.teacher_list_query.click()
    if page.teacher_list_loading:
        # 选择老师
        page.choose_teacher_a.click()
        PageWait(page.confirm_split)
        # 确认分班
        page.confirm_split.click()


def convert_student(driver, school_name, customer_num=None):
    """
    客户转为学员操作
    @param driver:
    @param school_name:
    @param customer_num:
    @return:
    """
    page = GfyCrmCustomerManagement(driver)
    PageSelect(page.customer_list_school_list, text=school_name)
    page.customer_list_load_button.click()
    sleep(2)
    # 单个勾选
    if customer_num == 1 or customer_num is None:
        page.customer_check[0].click()
    # 多个勾选
    elif customer_num == 2:
        i = 0
        while i < customer_num:
            page.customer_check[i].click()
            i += 1
    # 部分成功
    else:
        page.customer_check[0].click()
        page.batch_convert_student.click()
        PageWait(page.convert_confirm)
        page.convert_confirm.click()
        PageWait(page.customer_ok_button)
        page.customer_ok_button.click()
        sleep(1)
        i = 0
        while i < customer_num:
            page.customer_check[i].click()
            i += 1
    page.batch_convert_student.click()
    PageWait(page.convert_confirm)
    page.convert_confirm.click()


def create_account(driver, school_name, exist_account, exist_account_name, customer_name, password):
    """
    客户账号创建和绑定
    @param password:
    @param customer_name:
    @param driver:
    @param school_name:
    @param exist_account:
    @param exist_account_name:
    @return:
    """
    page = GfyCrmCustomerManagement(driver)
    PageSelect(page.customer_list_school_list, text=school_name)
    sleep(1)
    # 获得和打开第一个客户名称
    by_xpath_contains(driver, "a", customer_name, tag_2="@title").click()
    sleep(1)
    # 同步教学帐号按钮
    page.customer_create_account.click()
    sleep(1)
    # 绑定已有客户账户
    if exist_account == "是":
        page.customer_create_account_like.send_keys(exist_account_name)
        page.customer_create_account_query.click()
        PageWait(page.customer_create_account_select)
        page.customer_create_account_select.click()
    # 创建和绑定账户
    if exist_account == "否":
        # 创建教学平台按钮
        page.customer_create_account_btn.click()
        sleep(1)
        page.customer_create_account_name.send_keys(customer_name)
        sleep(1)
        page.customer_create_account_password.send_keys(password)
        sleep(1)
        page.customer_create_account_repeat_password.send_keys(password)
        sleep(1)
        page.customer_create_account_birthday.click()
        sleep(1)
        page.customer_create_account_birthday_today.click()
        sleep(1)
        page.customer_create_account_save.click()


def add_customer_responsible(driver, responsible_name, department_name, school_name):
    """
    添加客户跟进人
    起点：新增客户跟进人界面
    @param driver:
    @param responsible_name:跟进人登录名
    @param department_name:
    @param school_name:
    @return:
    """
    responsible_page = GfyCrmCustomerManagement(driver)
    responsible_page.responsible_name_input.click()
    if responsible_page.user_list_dialog != "":
        PageSelect(responsible_page.teacher_list_school, text=school_name)
        PageSelect(responsible_page.teacher_attribution_department, text=department_name)
        responsible_page.teacher_list_login_name.clear()
        sleep(1)
        responsible_page.teacher_list_login_name.send_keys(responsible_name)
        responsible_page.teacher_list_query.click()
        if responsible_page.teacher_list_loading:
            responsible_page.choose_teacher_a.click()
            sleep(1)
            responsible_page.responsible_save.click()


def add_customer_intent(driver, school_name, activity_type, activity_name, responsible_department, responsible_Name,
                        case, teacher_name, teacher_department):
    """
    添加客户意向
    @param driver:
    @param school_name:
    @param activity_type:
    @param activity_name:
    @param responsible_department:
    @param responsible_Name:
    @param case:
    @param teacher_name:
    @param teacher_department:
    @return:
    """
    intent_page = GfyCrmCustomerManagement(driver)
    # 综合信息-客户业务意向
    intent_page.business_intent.click()
    sleep(1)
    # 新增业务意向
    intent_page.new_business_intent.click()
    sleep(1)
    intent_page.choice_activity_name.click()
    sleep(1)
    PageSelect(intent_page.activity_school, text=school_name)
    intent_page.activity_list_business_type.click()
    sleep(1)
    # 输入活动类型名称
    intent_page.activity_type_touched.send_keys(activity_type)
    sleep(1)
    # 选择活动类型
    by_xpath_contains(driver, "button", activity_type, "@title").click()
    sleep(1)
    # 输入活动名称
    intent_page.activity_name.send_keys(activity_name)
    intent_page.activity_query.click()
    sleep(1)
    intent_page.activity_selected.click()
    sleep(1)
    intent_page.activity_save.click()
    PageWait(intent_page.confirm_btn)
    intent_page.confirm_btn.click()
    sleep(1)
    if intent_page.responsible_dialog != "":
        if case == "新招生":
            add_customer_responsible(driver, responsible_Name, responsible_department, school_name)
        if case == "辅导续费" or case == "顾问转介绍":
            add_customer_responsible(driver, teacher_name, teacher_department, school_name)
            sleep(1)
            intent_page.responsible_add.click()
            sleep(2)
            add_customer_responsible(driver, responsible_Name, responsible_department, school_name)


def customer_recovery(driver, student_num, i=0):
    """
    回收未成交客户
    @param i:
    @param driver:
    @param student_num:
    @return:
    """
    customer_page = GfyCrmCustomerManagement(driver)
    PageSelect(customer_page.customer_is_deal, text="未成交")
    PageSelect(customer_page.customer_is_order, text="是")
    customer_page.customer_list_load_button.click()
    if customer_page.customer_loading:
        if student_num == 1:
            # 回收
            customer_page.customer_recovery[0].click()
            sleep(1)
            customer_page.confirm_btn.click()
        if student_num > 1:
            while i < student_num:
                customer_page.customer_check[i].click()
                i += 1
            customer_page.customer_multi_recovery.click()
            PageWait(customer_page.confirm_btn)
            customer_page.confirm_btn.click()

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
