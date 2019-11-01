import pymysql


def new_student_name():
    """
    连接集成数据库得出客户***,返回集成数据库最新"客户"***+1的名称
    :return:
    """
    # db = pymysql.connect('rm-wz9ex1m8zw6c8ui55o.mysql.rds.aliyuncs.com',
    #                      'edu_test_user',
    #                      'Quanlang_edu_test')
    db = pymysql.connect('192.168.0.195',
                         'root',
                         '123456')
    cursor = db.cursor()
    sql = 'SELECT cust_name FROM test_customer.cust_info ' \
          'WHERE cust_id = (SELECT MAX(cust_id) ' \
          'FROM test_customer.cust_info WHERE cust_name LIKE "客户%" AND cust_status="S01")'
    cursor.execute(sql)
    result = cursor.fetchall()
    for re in result:
        cust_name = re[0]
    # 读取客户名称后的数字
    a = cust_name[2:]
    clinetnum = int(a)
    clinetnum = clinetnum + 1
    clinetname = "客户" + str(clinetnum)
    return clinetname
    db.close()


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


print(new_staff_name())
