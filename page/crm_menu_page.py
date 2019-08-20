from poium import Page, PageElement


class GfyMenu(Page):
    finance_menu = PageElement(
        xpath="//*[@id=\"sysMenu\"]/li[4]/a",
        describe="菜单-财务管理按钮")
    finance_fee_info = PageElement(
        xpath="//*[@id=\"sysMenu\"]/li[4]/ul/li[4]/a",
        describe="菜单-财务管理-缴费退费信息按钮")
    finance_refund_info = PageElement(
        xpath="//*[@id=\"sysMenu\"]/li[4]/ul/li[4]/ul/li[2]/a",
        describe="菜单-财务管理-缴费退费信息-退费信息按钮")

