from poium import Page, PageElement


class GfyLogin(Page):
    """
    CRM登录界面
    """
    login_input = PageElement(
        xpath="//input[@name='username']",
        describe="登录界面-账号输入框")
    pwd_input = PageElement(
        xpath="//input[@name='password']",
        describe="登录界面-密码输入框")
    verification_code = PageElement(
        xpath="//b[@ng-click='createCode()']",
        describe="验证码")
    code_input = PageElement(
        xpath="//input[@name='verify']",
        describe="验证码输入框")
    enter = PageElement(
        xpath="//button[@name='submit']",
        describe="登录按钮")
    account_name = PageElement(
        xpath="//span[@class='hidden-xs ng-binding']",
        describe="信息栏-左上角用户名称")
