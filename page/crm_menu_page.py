from poium import Page, PageElement


class GfyMenu(Page):
    dashboard = PageElement(
        link_text="首页",
        describe="首页按钮")
    customer_management = PageElement(
        link_text='客户管理',
        describe="客户管理")
    my_customer = PageElement(
        link_text='我的客户',
        describe='我的客户')
    student_management = PageElement(
        xpath="//i[@class='fa fa-users']",
        describe="菜单页面-学员管理")
    student_order_management = PageElement(
        xpath="//i[@class='fa fa-file-text']",
        describe="菜单页面-学员管理-学员订单管理")
    finance_menu = PageElement(
        xpath="//i[@class='fa fa-pie-chart']",
        describe="菜单-财务管理按钮")
    finance_fee_info = PageElement(
        link_text="缴费退费信息",
        describe="菜单-财务管理-缴费退费信息按钮")
    finance_refund_info = PageElement(
        xpath="//i[@class='fa fa-reply-all']",
        describe="菜单-财务管理-缴费退费信息-退费信息按钮")
