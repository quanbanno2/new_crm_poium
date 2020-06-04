import sys
import pytest

from poium import PageWait
# # 定义搜索模块顺序，优先搜索new_crm_poium文件夹
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.crm_login_page import GfyLogin

from func.customer_management_func import login
from func.get_data import get_json_data
from conftest import DATA_DIR


class TestLogin:
    @pytest.mark.parametrize(
        "name,password,case,msg",
        get_json_data(DATA_DIR + "login_success.json")
    )
    def test_login_success(self, crm_url, browser1, password, name, case, msg):
        """
        测试登录成功
        @param crm_url:
        @param browser1:
        @param password:
        @param name:
        @param case:
        @param msg:
        @return:
        """
        page = GfyLogin(browser1)
        if case == "登陆成功":
            login(crm_url, browser1, name, password)
            PageWait(page.account_name)
            assert page.account_name.text == msg

    @pytest.mark.parametrize(
        "case,name,password,msg",
        get_json_data(DATA_DIR + "login_fail.json")
    )
    def test_login_fail(self, crm_url, browser1, password, name, case, msg):
        """
        测试登录失败
        @param crm_url:
        @param browser1:
        @param password:
        @param name:
        @param case:
        @param msg:
        @return:
        """
        page = GfyLogin(browser1)
        if case == "账号错误":
            login(crm_url, browser1, name, password)
            assert page.get_alert_text == msg
            page.dismiss_alert()
        elif case == "密码错误":
            login(crm_url, browser1, name, password)
            assert page.get_alert_text == msg
            page.dismiss_alert()
        elif case == "账号或密码为空":
            page.get(crm_url)
            assert page.enter.get_attribute("disabled") == msg


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_crm_login.py"])
