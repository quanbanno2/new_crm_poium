import pymysql

db = pymysql.connect('rm-wz9ex1m8zw6c8ui55o.mysql.rds.aliyuncs.com',
                     'jiaoyupingtai_re',
                     'QuanLang@123')
cursor = db.cursor()
sql = 'SELECT cust_name FROM test_customer.cust_info ' \
      'WHERE cust_id = (SELECT MAX(cust_id) ' \
      'FROM test_customer.cust_info WHERE cust_name LIKE "客户%" AND cust_status="S01")'
cursor.execute(sql)
result = cursor.fetchall()

print(result)
