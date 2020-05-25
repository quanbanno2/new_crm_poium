import datetime

import pymysql
from selenium import webdriver
from time import sleep
import re
from _pydecimal import Context, ROUND_HALF_UP


def database_connect():
    db = pymysql.connect('rm-wz9ex1m8zw6c8ui55o.mysql.rds.aliyuncs.com',
                         'edu_test_user',
                         'Quanlang_edu_test')
    # cursor = db.cursor()
    # return cursor
    return db


def new_staff_name_by_sql():
    """
    新增员工名称
    :return:
    """
    staff_name = []
    my_con = database_connect()
    my_cursor = my_con.cursor()
    sql = 'SELECT name FROM test_user.usr_staff_base_info ' \
          'WHERE staff_base_id = (SELECT MAX(staff_base_id) ' \
          'FROM test_user.usr_staff_base_info WHERE name LIKE "高分云员工%")'
    my_cursor.execute(sql)
    result = my_cursor.fetchall()
    for re in result:
        staff_name = re[0]
    # 读取客户名称后的数字
    a = staff_name[5:]
    staff_num = int(a)
    staff_num += 1
    new_name = "高分云员工" + str(staff_num)
    my_con.close()
    return new_name


# def new_student_name():
#     """
#     连接集成数据库得出客户***,返回集成数据库最新"客户"***+1的名称
#     :return:
#     """
#     # db = pymysql.connect('rm-wz9ex1m8zw6c8ui55o.mysql.rds.aliyuncs.com',
#     #                      'edu_test_user',
#     #                      'Quanlang_edu_test')
#     db = pymysql.connect('192.168.0.195',
#                          'root',
#                          '123456')
#     cursor = db.cursor()
#     sql = 'SELECT cust_name FROM test_customer.cust_info ' \
#           'WHERE cust_id = (SELECT MAX(cust_id) ' \
#           'FROM test_customer.cust_info WHERE cust_name LIKE "客户%" AND cust_status="S01")'
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     for re in result:
#         cust_name = re[0]
#     # 读取客户名称后的数字
#     a = cust_name[2:]
#     clinetnum = int(a)
#     clinetnum = clinetnum + 1
#     clinetname = "客户" + str(clinetnum)
#     return clinetname
#     db.close()


def new_staff_name():
    staff_name = []
    db = pymysql.connect('rm-wz9ex1m8zw6c8ui55o.mysql.rds.aliyuncs.com',
                         'edu_test_user',
                         'Quanlang_edu_test')
    # db = pymysql.connect('192.168.0.195',
    #                      'root',
    #                      '123456')
    cursor = db.cursor()
    sql = 'SELECT `name`  FROM `test_user`.`usr_staff_base_info` ' \
          ' WHERE `staff_base_id`  = (SELECT MAX(`staff_base_id`) ' \
          ' FROM `test_user`.`usr_staff_base_info`  WHERE `name`  LIKE "高分云员工%" AND `status_cd` ="S01" ' \
          ' OR `status_cd`= "S03")'
    cursor.execute(sql)
    result = cursor.fetchall()
    for re in result:
        staff_name = re[0]
    # 读取客户名称后的数字
    a = staff_name[5:]
    client_num = int(a)
    client_num = client_num + 1
    client_name = "高分云员工" + str(client_num)
    db.close()
    return client_name


def eliminate_account(account_name):
    my_con = pymysql.connect('rm-wz9ex1m8zw6c8ui55o.mysql.rds.aliyuncs.com',
                             'edu_test_user',
                             'Quanlang_edu_test')
    my_cursor = my_con.cursor()
    sql = 'DELETE FROM test_user.usr_account_info WHERE login_name="%s"' % account_name
    my_cursor.execute(sql)
    my_con.commit()
    my_cursor.close()
    my_con.close()


def update_account(exist_account):
    my_con = pymysql.connect('rm-wz9ex1m8zw6c8ui55o.mysql.rds.aliyuncs.com',
                             'edu_test_user',
                             'Quanlang_edu_test')
    my_cursor = my_con.cursor()
    sql1 = "UPDATE `test_student`.`stu_info` SET `account_no`=NULL " \
           "WHERE `account_no` = (SELECT account_no FROM `test_user`.`usr_account_info` " \
           "WHERE `login_name` = '%s');" % exist_account
    my_cursor.execute(sql1)
    my_con.commit()
    my_cursor.close()
    my_con.close()


def get_account_info(login_name):
    my_con = pymysql.connect('rm-wz9ex1m8zw6c8ui55o.mysql.rds.aliyuncs.com',
                             'edu_test_user',
                             'Quanlang_edu_test')
    my_cursor = my_con.cursor()
    sql = "SELECT object_type_cd FROM `test_user`.`usr_account_info` WHERE login_name ='%s'" % login_name
    my_cursor.execute(sql)
    result = my_cursor.fetchall()
    for res in result:
        object_type = res[0]
    try:
        if object_type == "A01":
            sql_2 = "SELECT b.staff_name FROM `test_user`.`usr_account_info` AS a,`test_user`.`usr_staff_info` AS b " \
                    "WHERE a.login_name='%s' AND a.object_id=b.staff_id" % login_name
            my_cursor.execute(sql_2)
            result = my_cursor.fetchall()
            for res in result:
                teacher_name = res[0]
            my_con.close()
            return teacher_name
        elif object_type == "A02":
            sql_2 = "SELECT b.teacher_name FROM `test_user`.`usr_account_info` AS a" \
                    ",`test_user`.`usr_teacher_info` AS b " \
                    "WHERE a.login_name='%s' AND a.object_id=b.teacher_id" % login_name
            my_cursor.execute(sql_2)
            result = my_cursor.fetchall()
            for res in result:
                teacher_name = res[0]
            my_con.close()
            return teacher_name
    except:
        print("账号名称错误")


# name = "客户577"
# eliminate_account(name)

# new_staff_name_by_sql()

# lis = get_account_info("高分云辅导哈")
# print(lis)


def by_xpath(driver, context):
    # wd = webdriver.Chrome()
    # wd.get("https://www.baidu.com")

    return driver.find_element_by_xpath("//a[contains(.,'%s')]" % context)


# wd = webdriver.Chrome()
# wd.get("https://www.baidu.com")
#
# xt = by_xpath(wd, "抗击肺炎").click()
# sleep(5)
#
# tezt = filter(str.isdigit, "￥24.4")
# print(''.join(list(tezt)))
#
# tezt1 = re.search("\d+(\.\d+)?", "-550")
# print(tezt1.group())


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
    # return str(Context(prec=7, rounding=ROUND_HALF_UP).create_decimal(refund_fee))
    refund_fee = "%.2f" % refund_fee
    refund_fee = float(refund_fee)
    print(type(refund_fee))

    return refund_fee


# p = cal_refund_fee("55", "3", "0")
#
# print(p)
#
# print(float("55"))


# 补课时间-当前时间加1小时
makeUpTime = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y/%m/%d %H:%M:%S")
print(makeUpTime)

