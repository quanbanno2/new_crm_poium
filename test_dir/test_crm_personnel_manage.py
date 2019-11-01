import pytest
import sys
import pymysql
from time import sleep
from page.crm_personnel_page import GfyPersonnel
from page.crm_menu_page import GfyMenu
from poium import PageWait, PageSelect
from test_dir.test_crm_cust_manger import login
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))


def new_staff_name():
    customer_name = []
    # db = pymysql.connect('rm-wz9ex1m8zw6c8ui55o.mysql.rds.aliyuncs.com',
    #                      'edu_test_user',
    #                      'Quanlang_edu_test')
    db = pymysql.connect('192.168.0.195',
                         'root',
                         '123456')
    cursor = db.cursor()
    sql = 'SELECT `name`  FROM `test_user`.`usr_staff_base_info` ' \
          ' WHERE `staff_base_id`  = (SELECT MAX(`staff_base_id`) ' \
          ' FROM `test_user`.`usr_staff_base_info`  WHERE `name`  LIKE "高分云员工%" AND `status_cd` ="S01" ' \
          ' OR `status_cd`= "S03")'
    cursor.execute(sql)
    result = cursor.fetchall()
    for re in result:
        customer_name = re[0]
    # 读取客户名称后的数字
    a = customer_name[5:]
    client_num = int(a)
    client_num = client_num + 1
    client_name = "高分云员工" + str(client_num)
    db.close()
    return client_name


def add_staff_base_info(driver):
    menu_page = GfyMenu(driver)
    page = GfyPersonnel(driver)
    menu_page.personnel_manage.click()
    sleep(1)
    menu_page.staff_info.click()
    sleep(1)
    menu_page.staff_base_info.click()
    PageWait(page.add_staff_base_info)
    page.add_staff_base_info.click()
    PageWait(page.staff_name[1])
    page.staff_name[1].send_keys()


class TestStaffInfo:

    def test_load_staff_info(self, browser1, crm_url, supervisor_account, pass_word):
        menu_page = GfyMenu(browser1)
        personnel_page = GfyPersonnel(browser1)
        login(crm_url, browser1, supervisor_account, pass_word)
        menu_page.personnel_manage.click()
        sleep(1)
        menu_page.staff_info.click()
        menu_page.staff_base_info.click()
        sleep(5)
        personnel_page.load_staff_base_list.click()
        sleep(5)
        # 断言当前总条数如果为0，即认为查询失败，否则认为成功
        assert personnel_page.load_result.text != "0"

    def test_add_staff_base_info(self, browser1, crm_url, supervisor_account, pass_word):
        login(crm_url, browser1, supervisor_account, pass_word)
        add_staff_base_info(browser1)

        sleep(10)


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_crm_personnel_manage.py::TestStaffInfo::test_add_staff_base_info"])
