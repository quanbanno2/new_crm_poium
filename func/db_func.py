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
            self.my_cursor = self.my_con.cursor()
        except Exception as db_ex:
            print(db_ex)

    def exe_update(self, sql):  # 更新,删除或插入操作
        sta = self.my_cursor.execute(sql)
        self.my_con.commit()
        return sta

    def exe_query(self, sql):  # 查找操作
        self.my_cursor.execute(sql)
        return self.my_cursor

    def conn_close(self):  # 关闭连接，释放资源
        self.my_cursor.close()
        self.my_con.close()

    def new_customer_name_by_sql(self):
        """
        连接集成数据库得出客户***,返回集成数据库最新"客户"***+1的名称
        :return:
        """
        customer_name = []
        sql = 'SELECT cust_name FROM test_customer.cust_info ' \
              'WHERE cust_id = (SELECT MAX(cust_id) ' \
              'FROM test_customer.cust_info WHERE cust_name LIKE "高分云客户%" AND cust_status="S01")'
        result = self.exe_query(sql).fetchone()
        # for re in result:
        #     customer_name = re[0]
        # 读取客户名称后的数字
        customer_name = result[0]
        a = customer_name[5:]
        client_num = int(a)
        client_num += 1
        client_name = "高分云客户" + str(client_num)
        self.conn_close()
        return client_name

    def eliminate_account_by_sql(self, account_name):
        """
        删除指定客户账号
        链接-执行-提交事务-关闭数据库
        :param account_name:
        :return:
        """
        sql = 'DELETE FROM test_user.usr_account_info WHERE login_name="%s"' % account_name
        self.exe_update(sql)
        self.conn_close()

    def new_staff_name_by_sql(self):
        """
        新增员工名称
        @return: 返回生成的员工名称
        """
        staff_name = []
        sql = 'SELECT name FROM test_user.usr_staff_base_info ' \
              'WHERE staff_base_id = (SELECT MAX(staff_base_id) ' \
              'FROM test_user.usr_staff_base_info WHERE name LIKE "高分云员工%")'
        self.exe_query(sql)
        result = self.my_cursor.fetchall()
        for re in result:
            staff_name = re[0]
        a = staff_name[5:]
        staff_num = int(a)
        staff_num += 1
        new_name = "高分云员工" + str(staff_num)
        self.conn_close()
        return new_name

    def update_account(self, exist_account):
        """
        更新账号信息
        @return:
        """
        # 查出已存在的账号
        sql = "UPDATE `test_student`.`stu_info` SET `account_no`=NULL " \
              "WHERE `account_no` = (SELECT account_no FROM `test_user`.`usr_account_info` " \
              "WHERE `login_name` = '{}');".format(exist_account)
        self.exe_update(sql)
        self.conn_close()

    def get_account_name(self, login_name):
        """
        根据登录名查询教师名称
        @param login_name:
        @return:
        """
        object_type = ""
        teacher_name = ""
        sql = "SELECT object_type_cd FROM `test_user`.`usr_account_info` WHERE login_name ='{}'".format(login_name)
        self.exe_query(sql)
        result = self.my_cursor.fetchall()
        for res in result:
            object_type = res[0]
        # 运营人员
        if object_type == "A01":
            sql_2 = "SELECT b.staff_name FROM `test_user`.`usr_account_info` AS a" \
                    ",`test_user`.`usr_staff_info` AS b " \
                    "WHERE a.login_name='{}' AND a.object_id=b.staff_id".format(login_name)
            self.exe_query(sql_2)
            result = self.my_cursor.fetchall()
            for res in result:
                teacher_name = res[0]
            self.conn_close()
            return teacher_name
        # 老师
        elif object_type == "A02":
            sql_2 = "SELECT b.teacher_name FROM `test_user`.`usr_account_info` AS a" \
                    ",`test_user`.`usr_teacher_info` AS b " \
                    "WHERE a.login_name='{}' AND a.object_id=b.teacher_id".format(login_name)
            self.exe_query(sql_2)
            result = self.my_cursor.fetchall()
            for res in result:
                teacher_name = res[0]
            self.conn_close()
            return teacher_name

    def reset_order_status(self, status, order_id):
        """
        重置订单状态
        @param status:
        @param order_id:
        @return:
        """
        if status == "未缴费":
            sql = [
                "UPDATE test_student.stu_order_info SET order_status='S01' WHERE order_id='{}' ".format(order_id),
                "UPDATE test_student.stu_order_course SET course_status='S05',paid_in=receivable,discount='0.00' "
                "WHERE order_id='{}'".format(order_id),
                "UPDATE test_finance.finance_payment_info "
                "SET payment_status='S01',bank_paid_in='0.00',discount='0.00',paid_in=receivable,other_fee='0.00' "
                "WHERE order_id='{}'".format(order_id),
                "DELETE FROM test_finance.finance_pay_detail WHERE order_id='{}'".format(order_id),
                "DELETE FROM test_finance.finance_discount_detail WHERE order_id='{}'".format(order_id),
                "DELETE FROM test_finance.finance_other_fee_detail WHERE order_id='{}'".format(order_id)
            ]
            for ex in sql:
                self.exe_update(ex)
        elif status == "已缴部分":
            sql = [
                "UPDATE test_student.stu_order_info SET order_status='S05' WHERE order_id='{}'".format(order_id),
                "UPDATE test_student.stu_order_course SET course_status='S05' WHERE order_id='{}'".format(order_id),
                "UPDATE test_finance.finance_payment_info SET payment_status='S05',bank_paid_in='500.00' "
                "WHERE order_id='{}'".format(order_id),
                "DELETE FROM test_finance.finance_pay_detail WHERE order_id='{}' AND pay_fee = '7000.00'".format(
                    order_id)
            ]
            for ex in sql:
                self.exe_update(ex)
        self.conn_close()

    def reset_order_class_status(self, status, order_id):
        """
        重置订单状态和订单课程状态
        @param status:
        @param order_id:
        @return:
        """
        if status == "全部退费":
            sql = [
                "update test_student.stu_order_info set order_status='S02' where order_id='{}'".format(order_id),
                "update test_student.stu_order_course set course_status='S01' where course_status='S03' "
                "and order_id='{}'".format(order_id),
                "update test_finance.finance_fee_detail set refund_status='R01' where refund_status='R02' "
                "and order_id='[]'".format(order_id),
                "update test_finance.finance_payment_info set payment_status='S02' where order_id='{}'".format(
                    order_id),
                "delete from test_finance.finance_refund_apply where order_id='{}'".format(order_id),
                "delete from test_finance.finance_refund_detail where order_id='{}'".format(order_id),
                "delete from test_finance.finance_department_achievement_detail "
                "where achievement_type='A02' and order_id='{}'".format(order_id),
                "delete from test_finance.finance_department_achievement_detail "
                "where achievement_type='A02' and order_id='{}'".format(order_id),
                "delete from test_finance.finance_staff_achievement_detail "
                "where achievement_type='A02' and order_id='{}'".format(order_id)
            ]
            for exe in sql:
                self.exe_update(exe)
        elif status == "部分退费":
            sql = [
                "update test_student.stu_order_info set order_status='S02' where order_id='{}'".format(order_id),
                "update test_student.stu_order_course set course_status='S01',cons_count='12.5' "
                "where course_status='S03' and order_id='{}'".format(order_id),
                "update test_finance.finance_fee_detail set refund_status='R01' "
                "where refund_status='R02' and order_id='{}'".format(order_id),
                "update test_finance.finance_payment_info set payment_status='S02' where order_id='{}'".format(
                    order_id),
                "delete from test_finance.finance_refund_apply where order_id='{}'".format(order_id),
                "delete from test_finance.finance_refund_detail where order_id='{}'".format(order_id),
                "delete from test_finance.finance_department_achievement_detail "
                "where achievement_type='A02' and order_id='{}'".format(order_id)
            ]
            for exe in sql:
                self.exe_update(exe)
        self.conn_close()

    def reset_order_course_status(self, order_course_id, origin_class_id):
        """
        重置学生班级
        @param order_course_id: 订单课程编号
        @param origin_class_id: 充值课程编号
        @return:
        """
        for re in order_course_id:
            sql = "UPDATE test_student.stu_order_course SET class_id='{}' WHERE order_course_id='{}';".format(
                origin_class_id, re)
            self.exe_update(sql)
        self.conn_close()

    def get_customer_id(self, customer_name):
        """
        根据客户名称获取客户id
        @param customer_name:
        @return:
        """
        sql = "SELECT cust_id FROM test_customer.cust_info WHERE cust_name = '{}'".format(customer_name)
        result = self.exe_query(sql).fetchone()
        result = result[0]
        self.conn_close()
        return result

    def get_teacher_id(self, teacher_name):
        """
        根据老师登录名称查询对应account_no
        @param teacher_name:
        @return:
        """
        sql = "SELECT account_no FROM test_user.usr_account_info WHERE login_name = '{}'".format(teacher_name)
        self.exe_query(sql)
        result = self.my_cursor.fetchall()
        for res in result:
            teacher_name = res[0]
        self.conn_close()
        return teacher_name

    def update_admin_status(self, user_id):
        """
        取消老师的在接待状态
        @param user_id:
        @return:
        """
        sql = "UPDATE test_customer.cust_admit_info SET status = 'S02' WHERE user_id = '{}' AND status='S01'".format(
            user_id)
        self.exe_update(sql)
        self.conn_close()

    def delete_customer_info(self, cust_id=None, cust_name=None):
        """
        删除客户信息
        @param cust_id:
        @param cust_name:
        @return:
        """
        if cust_id is not None and cust_name is None:
            sql = "DELETE FROM `test_customer`.`cust_info` WHERE `cust_id` = '{}'".format(cust_id)
            self.exe_update(sql)
        elif cust_name is not None and cust_id is None:
            sql = "DELETE FROM `test_customer`.`cust_info` WHERE `cust_name` = '{}'".format(cust_name)
            self.exe_update(sql)
        self.conn_close()
