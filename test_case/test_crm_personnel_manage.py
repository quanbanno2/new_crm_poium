# import pytest
# import sys
# from time import sleep
# from os.path import dirname, abspath
#
# sys.path.insert(0, dirname(dirname(abspath(__file__))))
# from page.crm_personnel_page import GfyPersonnel
# from page.crm_menu_page import GfyMenu
# from func.db_func import DB
# from func.customer_management_func import login
#
#
# def add_staff_base_info(driver):
#     """
#     新增员工
#     @param driver:
#     @return:
#     """
#     staff_info_page = GfyPersonnel(driver)
#     staff_info_page.add_staff_base_info.click()
#     sleep(1)
#     staff_info_page.add_staff_name[1].send_keys(DB().new_staff_name_by_sql())
#     staff_info_page.staff_job_number[1].send_keys()
#     # 员工账号
#
#
# class TestStaffInfo:
#
#     def test_add_staff(self, browser1, human_resource_account, pass_word, crm_url):
#         """
#         测试员工入职
#         入职流程：新建员工-新增岗位-新增基础工资信息
#         @param browser1:
#         @return:
#         """
#         menu_page = GfyMenu(browser1)
#         staff_info_page = GfyPersonnel(browser1)
#         login(crm_url, browser1, human_resource_account, pass_word)
#         menu_page.personnel_manage.click()
#         sleep(1)
#         menu_page.staff_info.click()
#         sleep(1)
#         menu_page.staff_base_info.click()
#         add_staff_base_info(browser1)
#
#
# if __name__ == '__main__':
#     pytest.main(["-v", "-s", "test_crm_personnel_manage.py::TestStaffInfo::test_add_staff"])
