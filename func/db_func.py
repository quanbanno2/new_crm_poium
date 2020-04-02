import pymysql


class DB:
    """
    db操作
    """

    def __init__(self):

        """
        初始化集成数据库链接
        :return:
        """
        try:
            self.my_con = pymysql.connect('rm-wz9ex1m8zw6c8ui55o.mysql.rds.aliyuncs.com',
                                          'edu_test_user',
                                          'Quanlang_edu_test')
        except Exception as dbex:
            print(dbex)

    def new_customer_name_by_sql(self):
        """
        连接集成数据库得出客户***,返回集成数据库最新"客户"***+1的名称
        :return:
        """
        customer_name = []
        my_cursor = self.my_con.cursor()
        sql = 'SELECT cust_name FROM test_customer.cust_info ' \
              'WHERE cust_id = (SELECT MAX(cust_id) ' \
              'FROM test_customer.cust_info WHERE cust_name LIKE "高分云客户%" AND cust_status="S01")'
        my_cursor.execute(sql)
        result = my_cursor.fetchall()
        for re in result:
            customer_name = re[0]
        # 读取客户名称后的数字
        a = customer_name[5:]
        client_num = int(a)
        client_num += 1
        client_name = "高分云客户" + str(client_num)
        self.my_con.close()
        return client_name

    def eliminate_account_by_sql(self, account_name):
        """
        删除指定客户账号
        链接-执行-提交事务-关闭数据库
        :param account_name:
        :return:
        """
        my_cursor = self.my_con.cursor()
        sql = 'DELETE FROM test_user.usr_account_info WHERE login_name="%s"' % account_name
        my_cursor.execute(sql)
        self.my_con.commit()
        my_cursor.close()
        self.my_con.close()

    def new_staff_name_by_sql(self):
        """
        新增员工名称
        @return: 返回生成的员工名称
        """
        staff_name = []
        my_cursor = self.my_con.cursor()
        sql = 'SELECT name FROM test_user.usr_staff_base_info ' \
              'WHERE staff_base_id = (SELECT MAX(staff_base_id) ' \
              'FROM test_user.usr_staff_base_info WHERE name LIKE "高分云员工%")'
        my_cursor.execute(sql)
        result = my_cursor.fetchall()
        for re in result:
            staff_name = re[0]
        a = staff_name[5:]
        staff_num = int(a)
        staff_num += 1
        new_name = "高分云员工" + str(staff_num)
        self.my_con.close()
        return new_name

    def update_account(self, exist_account):
        """
        更新账号信息
        @return:
        """
        my_cursor = self.my_con.cursor()
        # 查出已存在的账号
        sql = "UPDATE `test_student`.`stu_info` SET `account_no`=NULL " \
              "WHERE `account_no` = (SELECT account_no FROM `test_user`.`usr_account_info` " \
              "WHERE `login_name` = '%s');" % exist_account
        my_cursor.execute(sql)
        self.my_con.commit()
        my_cursor.close()
        self.my_con.close()
