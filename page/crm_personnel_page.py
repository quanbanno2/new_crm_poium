from poium import Page, PageElement, PageElements


class GfyPersonnel(Page):
    load_staff_base_list = PageElement(
        xpath="//button[@title='查询']",
        describe="员工信息-查询按钮")
    load_result = PageElement(
        xpath="//span[@ng-show='pageInfo.totalNum'][2]",
        describe="员工信息-总记录数")
    add_staff_base_info = PageElement(
        xpath="//button[@title='新增']",
        describe="员工信息-新增按钮")
    add_staff_name = PageElements(
        xpath="//input[@name='name']",
        describe="员工信息-新增-员工姓名")
    staff_job_number = PageElements(
        xpath="//input[@name='jobNumber']",
        describe="员工信息-新增-员工工号")
    staff_account = PageElements(
        xpath="//button[@title='新建账号']",
        describe="员工信息-新增-员工账号新建按钮")
    staff_loginName = PageElement(
        xpath="//input[@ng-model='staffAccountInfo.loginName']",
        describe="员工信息-新增-登录名")
    staff_password = PageElement(
        xpath="//input[@ng-model='staffAccountInfo.passwordNo']",
        describe="员工信息-新增-登录密码")
    staff_passwordConfirm = PageElement(
        xpath="//input[@ng-model='passwordNoTemp']",
        describe="员工信息-新增-确认密码")
    staff_phoneNumber = PageElement(
        xpath="//input[@name='phoneNo']",
        describe="员工信息-新增-手机号")
    staff_department = PageElement(
        xpath="//select[@ng-model='staffAccountInfo.departmentId']",
        describe="员工信息-新增-归属部门")
    save_staff_account = PageElement(
        xpath="//button[@ng-click='addStaffAccount()']",
        describe="员工信息-员工账号保存按钮")
    staff_entryDate = PageElements(
        xpath="//input[@name='entryDate']",
        describe="员工信息-新增-入职时间")
    staff_birthDate = PageElements(
        xpath="//input[@name='birthDate']",
        describe="员工信息-新增-出生日期")
    staff_identityCard = PageElements(
        xpath="//input[@name='identityCard']",
        describe="员工信息-新增-身份证")
    staff_cardEffDate = PageElements(
        xpath="//input[@name='cardEffDate']",
        describe="员工信息-新增-身份证生效日期")
    staff_cardExpDate = PageElements(
        xpath="//input[@name='cardExpDate']",
        describe="员工信息-新增-身份证失效日期")
    staff_nativePlace = PageElements(
        xpath="//input[@name='nativePlace']",
        describe="员工信息-新增-籍贯")
    staff_cardAddress = PageElements(
        xpath="//input[@name='cardAddress']",
        describe="员工信息-新增-户口所在地")
    staff_liveAddress = PageElements(
        xpath="//input[@name='liveAddress']",
        describe="员工信息-新增-现住地址")
    save_staff_base_info = PageElement(
        xpath="//button[@ng-click='addStaffBaseInfo()']",
        describe="员工信息-新增-保存按钮")
    status = PageElement(
        xpath="//div[@class='bootbox-body']",
        describe="保存状态")
    ok_button = PageElement(
        xpath="//button[@data-bb-handler='ok']",
        describe="状态确认按钮")
    cancel_button = PageElement(
        xpath="//button[@data-bb-handler='cancel']",
        describe="取消按钮")
