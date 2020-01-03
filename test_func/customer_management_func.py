import sys
from time import sleep
from poium import PageWait, PageSelect
from _pydecimal import Context, ROUND_HALF_UP

from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))

from page.crm_cust_manger_page import GfyCrmCustomerManagement, GfyCustomerAddOrder, GfyCustomerDataEliminate
from page.crm_menu_page import GfyMenu
from page.crm_login_page import GfyLogin


def operate_delete_customer(driver):
    """
    我的客户-删除客户信息操作
    @param driver:
    @return:
    """
    eliminate_page = GfyCustomerDataEliminate(driver)
    eliminate_page.customer_eliminate[0].click()
    PageWait(eliminate_page.eliminate_confirm)
    eliminate_page.eliminate_confirm.click()
    sleep(1)


def login(url, driver, account, password):
    """

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


def add_customer(driver, customer_name, phone_number):
    """
    创建客户：新招生类型
    :param driver:
    :param customer_name:
    :param phone_number:
    :return:
    """
    page = GfyCrmCustomerManagement(driver)
    menu_page = GfyMenu(driver)
    menu_page.customer_management.click()
    menu_page.my_customer.click()
    page.add_customer.click()
    sleep(2)
    page.add_customer_name.send_keys(customer_name)
    sleep(1)
    page.school_name.click()
    PageWait(page.pub_school_list)
    page.pub_school_list.send_keys("四基初级中学")
    page.pub_school_query.click()
    PageWait(page.pub_school_choice)
    page.pub_school_choice.click()
    PageWait(page.grade)
    PageSelect(page.grade, value='string:G09')
    page.customer_activity.click()
    sleep(1)
    page.activity_name.send_keys('高分云信息单')
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
    page.teacher_select.click()
    sleep(1)
    js = 'document.getElementsByName("effDate")[0].removeAttribute("readonly");'
    driver.execute_script(js)
    sleep(1)
    page.educational_effect_date.send_keys(educational_effect_time)
    sleep(1)
    page.student_educational_save.click()


def split_customer(driver, adviser_account):
    """
    单个学员分单
    :param driver:
    :param adviser_account:分单目标账号
    :return:
    """
    page = GfyCrmCustomerManagement(driver)
    sleep(1)
    # 勾选第一个客户
    page.customer_check[0].click()
    sleep(1)
    page.customer_split.click()
    sleep(1)
    page.teacher_list_login_name.clear()
    sleep(1)
    page.teacher_list_login_name.send_keys(adviser_account)
    sleep(1)
    page.teacher_list_query.click()
    PageWait(page.teacher_select)
    page.teacher_select.click()
    PageWait(page.confirm_split)
    page.confirm_split.click()


def convert_student(driver, school_name):
    """
    单个客户转为学员
    :param driver:
    :param school_name:
    :return:
    """
    page = GfyCrmCustomerManagement(driver)
    PageSelect(page.customer_list_school_list, text=school_name)
    sleep(1)
    page.convert_to_student.click()
    sleep(1)
    page.convert_confirm.click()


def create_account(driver, password, school_name):
    """
    客户详情创建教学帐号绑定
    :param driver:
    :param password:
    :param school_name:
    :return:
    """
    page = GfyCrmCustomerManagement(driver)
    PageSelect(page.customer_list_school_list, text=school_name)
    sleep(1)
    account_name = page.first_student_name.text
    page.first_student_name.click()
    sleep(1)
    page.customer_create_account.click()
    sleep(1)
    page.customer_create_account_btn.click()
    sleep(1)
    page.customer_create_account_name.send_keys(account_name)
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


def customer_edit():
    pass


def add_new_order(driver, consultant, course_name, school_name):
    """
    客户创建订单
    :param driver:
    :param consultant:分成对象
    :param course_name:
    :param school_name:
    :return:
    """
    customer_page = GfyCrmCustomerManagement(driver)
    order_page = GfyCustomerAddOrder(driver)
    PageSelect(customer_page.customer_list_school_list, text=school_name)
    sleep(1)
    customer_page.customer_name.click()
    sleep(1)
    order_page.customer_order_info.click()
    sleep(1)
    order_page.customer_order_add.click()
    sleep(1)
    PageSelect(order_page.order_sharing_object_select, text=consultant)
    sleep(1)
    order_page.order_sharing_object_select_btn.click()
    sleep(1)
    order_page.order_select_course.click()
    sleep(1)
    order_page.order_select_course_name.send_keys(course_name)
    sleep(1)
    order_page.order_select_course_name_query.click()
    sleep(1)
    order_page.order_select_course_btn.click()
    sleep(1)
    order_page.order_save_stu_order.click()


def customer_recovery(driver):
    """
    新单招生的客户回收
    :param driver:
    :return: 返回第一位跟进人名称
    """
    customer_page = GfyCrmCustomerManagement(driver)
    sleep(1)
    # 获取第一位跟进人名称
    customer_teacher_name = customer_page.customer_teacher[3].text
    sleep(1)
    # 回收
    customer_page.customer_recovery.click()
    sleep(1)
    customer_page.confirm_btn.click()
    return customer_teacher_name


def pay_new_order(driver):
    """
    新招生单单支付（优惠、支付项、手续费、支付）
    :param driver:
    :return:
    """
    order_page = GfyCustomerAddOrder(driver)
    menu_page = GfyMenu(driver)
    other_page = GfyCrmCustomerManagement(driver)
    sleep(1)
    menu_page.student_management.click()
    sleep(1)
    menu_page.student_order_management.click()
    sleep(1)
    order_page.student_order_pay_btn.click()
    sleep(1)
    # 优惠项
    preferential_amount = cal_preferential_amount(order_page.order_accounts_receivable.text)
    sleep(1)
    order_page.add_order_discount_btn.click()
    sleep(1)
    order_page.add_order_discount_fee.send_keys(preferential_amount)
    sleep(1)
    order_page.add_order_discount_save.click()
    # 支付项
    sleep(1)
    order_page.add_order_pay_btn.click()
    sleep(1)
    order_page.add_order_pay_fee.send_keys(order_page.order_pre_fee.text)
    sleep(1)
    order_page.add_order_pay_save_btn.click()
    # 计算其他费用
    sleep(1)
    service_charge = cal_service_charge(order_page.order_pre_fee.text)
    sleep(1)
    order_page.add_order_other_btn.click()
    sleep(1)
    order_page.add_order_other_fee.send_keys(service_charge)
    sleep(1)
    order_page.add_order_other_save.click()
    sleep(1)
    # 支付
    driver.execute_script("arguments[0].click();", order_page.pay_stu_order)
    sleep(1)
    other_page.confirm_btn.click()


def refund_apply(driver, remarks):
    """
     订单退费
    :param driver:
    :param remarks:
    :return: customer_name 客户名称、order_id_text 订单编号、refund_fee_text 应退费值
    """
    menu_page = GfyMenu(driver)
    order_page = GfyCustomerAddOrder(driver)
    sleep(1)
    menu_page.student_management.click()
    sleep(1)
    menu_page.student_order_management.click()
    sleep(1)
    order_page.order_detail.click()
    sleep(1)
    driver.execute_script("arguments[0].click();", order_page.order_info_refund)
    sleep(1)
    # 获取预收款、订购数量、消耗数量、学员名称、订单编号
    refund_pre_fee_text = order_page.refund_pre_fee.text
    refund_course_count_text = order_page.refund_course_count.text
    refund_course_consume_text = order_page.refund_course_consume.text
    customer_name = order_page.order_customer_name.text
    order_id_text = order_page.order_id.text
    sleep(1)
    order_page.refund_remark.send_keys(remarks)
    sleep(1)
    order_page.save_order_refund.click()
    PageWait(order_page.approval_matter_setting)
    PageSelect(order_page.approval_matter_setting, text="辅导督导1-->通知发起人")
    sleep(1)
    order_page.save_approval_matter.click()
    sleep(1)
    refund_fee_text = cal_refund_fee(refund_pre_fee_text, refund_course_count_text, refund_course_consume_text)
    return customer_name, order_id_text, refund_fee_text


def cal_preferential_amount(charge):
    """
    计算优惠
    :param charge:
    :return:
    """
    preferential_amount = int(int(charge) * 0.1)
    return preferential_amount


def cal_service_charge(charge):
    """
    计算手续费
    :param charge:
    :return:
    """
    service_charge = int(int(charge) * 5 / 1000)
    return service_charge


def cal_refund_fee(pre_fee, course_count, course_consume):
    """
    计算退费结算金额 = 预收 - （预收/课程单价*消耗课程数量）
    :param pre_fee:预收金额
    :param course_count:课程总数量
    :param course_consume:已消耗课程
    :return:
    """
    pre_fee = float(pre_fee)
    course_count = float(course_count)
    course_consume = float(course_consume)
    refund_fee = pre_fee - (pre_fee / course_count * course_consume)
    # 保留两位、四舍五入,以字符串格式返回
    return str(Context(prec=6, rounding=ROUND_HALF_UP).create_decimal(refund_fee))


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


def set_content_by_id(driver, content_id, text):
    """
    文本框输入
    :param driver:
    :param content_id:
    :param text:
    :return:
    """
    js = 'document.getElementById("%s").innerHTML = "%s" ' % (content_id, text)
    driver.execute_script(js)


def set_content_by_name(driver, content_name, text):
    """
    文本框输入
    :param driver:
    :param content_name:
    :param text:
    :return:
    """
    js = 'document.getElementsByName("%s").innerHTML = "%s" ' % (content_name, text)
    driver.execute_script(js)
