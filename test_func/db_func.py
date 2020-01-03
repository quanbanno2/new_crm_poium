import pymysql


def database_connect():
    """
    集成数据库链接
    :return:
    """
    my_con = pymysql.connect('rm-wz9ex1m8zw6c8ui55o.mysql.rds.aliyuncs.com',
                             'edu_test_user',
                             'Quanlang_edu_test')
    return my_con


def new_customer_name_by_sql():
    """
    连接集成数据库得出客户***,返回集成数据库最新"客户"***+1的名称
    :return:
    """
    customer_name = []
    my_con = database_connect()
    my_cursor = my_con.cursor()
    sql = 'SELECT cust_name FROM test_customer.cust_info ' \
          'WHERE cust_id = (SELECT MAX(cust_id) ' \
          'FROM test_customer.cust_info WHERE cust_name LIKE "客户%" AND cust_status="S01")'
    my_cursor.execute(sql)
    result = my_cursor.fetchall()
    for re in result:
        customer_name = re[0]
    # 读取客户名称后的数字
    a = customer_name[2:]
    client_num = int(a)
    client_num += 1
    client_name = "客户" + str(client_num)
    my_con.close()
    return client_name


def eliminate_account_by_sql(account_name):
    """
    删除指定客户账号
    链接-执行-提交事务-关闭数据库
    :param account_name:
    :return:
    """
    my_con = database_connect()
    my_cursor = my_con.cursor()
    sql = 'DELETE FROM test_user.usr_account_info WHERE login_name="%s"' % account_name
    my_cursor.execute(sql)
    my_con.commit()
    my_cursor.close()
    my_con.close()
