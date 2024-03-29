from poium import Page, PageElement


class GfyMenu(Page):
    menu_loading = PageElement(
        xpath="//div[@ng-show='$root.somethingLoading' and @class='overlay ng-hide']",
        describe="登录后loading目录")
    menu_active = PageElement(
        xpath="//li[@class='treeview ng-scope active']",
        describe="1级目录展开")
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
        xpath="//span[text()='学员管理']",
        describe="菜单页面-学员管理")
    student_order_management = PageElement(
        xpath="//a[text()='学员订单管理']",
        describe="菜单页面-学员管理-学员订单管理")
    student_course_management = PageElement(
        xpath="//a[text()='学员课程管理']",
        describe="菜单-学员管理-学员课程管理")
    student_class_management = PageElement(
        xpath="//a[text()='学员上课管理']",
        describe="菜单页面-学员管理-学员上课管理")
    student_makeup_management = PageElement(
        xpath="//a[text()='学员补课管理']",
        describe="菜单页面-学员管理-学员补课管理")
    finance_menu = PageElement(
        xpath="//span[text()='财务管理']",
        describe="菜单-财务管理按钮")
    finance_fee_info = PageElement(
        # xpath="//span[text()='缴费退费信息']",
        link_text="缴费退费信息",
        describe="菜单-财务管理-缴费退费信息按钮")
    finance_refund_info = PageElement(
        xpath="//a[text()='退费信息']",
        describe="菜单-财务管理-缴费退费信息-退费信息")
    personnel_manage = PageElement(
        link_text="人事管理",
        describe="人事管理")
    staff_info = PageElement(
        xpath="//span[text()='员工信息']",
        describe="人事管理-员工信息")
    menu_active_2 = PageElement(
        xpath="//li[@class='treeview active']",
        describe="2级目录展开")
    staff_base_info = PageElement(
        xpath="//a[text()='基础信息']",
        describe="人事管理-员工信息-基础信息")

