from poium import Page, PageElement


class GfyCrmAddCustomer(Page):
    """
    crm 增加客户、客户分单、转为学员
    """
    login_input = PageElement(css='input.ng-valid-maxlength', describe="账号")
    pwd_input = PageElement(css='div.form-group:nth-child(2) > div:nth-child(1) > '
                                'input:nth-child(2)', describe="密码")
    verification_code = PageElement(css=".ng-binding", describe="验证码")
    code_input = PageElement(
        css='input.form-control:nth-child(1)', describe="输入验证码")
    enter = PageElement(css='#enter', describe="登录按钮")
    account_name = PageElement(
        css="body > div.wrapper > header > nav > div > ul > li.dropdown.user.user-menu > a > span",
        describe="左上角用户名称")
    # 新增客户
    cust_manger = PageElement(link_text='客户管理', describe="客户管理")
    my_cust = PageElement(link_text='我的客户', describe='我的客户')
    add_cust = PageElement(css='button.pull-left:nth-child(2)', describe="新增客户")
    add_cust_name = PageElement(css='#custNewDialog > div > div > div.modal-body > form > div:nth-child(1) > input',
                                describe='新增客户名称')
    school_name = PageElement(css='#custNewDialog > div > div > div.modal-body > form > div:nth-child(7) > input',
                              describe='新建客户-公校名称')
    pub_school_list = PageElement(xpath='//*[@id=\"schListSimpleDialog\"]/div/div/div[2]/div[1]/form/div[1]/div/input',
                                  describe='新建客户-公校列表-公校名称')
    pub_school_query = PageElement(xpath='//*[@id=\"schListSimpleDialog\"]/div/div/div[2]/div[1]/form/div[2]/button',
                                   describe='新建客户-公校名称-公校列表-查询')
    pub_school_choice = PageElement(link_text='选定学校', describe='新建客户-公校名称-公校列表-查询')
    grade = PageElement(css='div.input-group:nth-child(8) > select:nth-child(2)', describe="年级")
    cust_activity = PageElement(css='div.input-group:nth-child(12) > button:nth-child(3)', describe='客户来源')
    # 活动列表
    cust_activity_type = PageElement(
        css='#marActivityListDialog > div > div > div.modal-body > form > '
            'div:nth-child(1) > div:nth-child(2) > '
            'div > select',
        describe='活动列表-活动类型')
    cust_activity_name = PageElement(
        xpath="//*[@id=\"marActivityListDialog\"]/div/div/div[2]/form/div[2]/div[1]/div/input",
        describe='活动列表-活动名称')
    cust_activity_query = PageElement(
        css='div.col-lg-1:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
        describe='活动查询')

    cust_activity_selected = PageElement(link_text="选中活动", describe="选择活动")
    ###
    phone = PageElement(css='div.input-group:nth-child(13) > div:nth-child(2) > '
                            'div:nth-child(1) > input:nth-child(5)', describe='联系方式')
    add_cust_save = PageElement(
        css='#custNewDialog > div:nth-child(1) > div:nth-child(1) > '
            'div:nth-child(3) > button:nth-child(2)',
        describe='保存按钮')
    cust_name = PageElement(
        xpath="//*[@id=\"custIndex\"]/section[2]/div[1]/"
              "div/div/div[1]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[3]/a",
        describe='客户管理列表排第一的客户名称')
    cust_name2 = PageElement(
        xpath="//*[@id=\"custIndex\"]/section[2]/div[1]/"
              "div/div/div[1]/div/div[2]/div/div[1]/table/tbody/tr[4]/td[3]/a",
        describe='客户管理列表排第二的客户名称')

    cust_check = PageElement(
        xpath="//*[@id=\"custIndex\"]/section[2]/div[1]/div/"
              "div/div[1]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[1]/input",
        describe="勾选第一个客户")
    cust_split = PageElement(css="button.btn:nth-child(4)", describe="分单按钮")
    # 机构老师列表
    tech_attribution_department = PageElement(
        css="select.ng-touched", describe="归属部门")
    tech_login_name = PageElement(
        xpath="/html/body/div[2]/div/div/div[2]/div[1]/form/div[3]/div/input",
        describe="登录名")
    tech_query = PageElement(
        css="div.col-sm-3:nth-child(4) > button:nth-child(1)", describe="老师查询")
    tech_select = PageElement(link_text="选中老师", describe="选择老师")
    ###
    confirm_split = PageElement(
        css="#allotOrderDialog > div:nth-child(1) > div:nth-child(1) > "
            "div:nth-child(3) > button:nth-child(2)",
        describe="确认分单按钮")
    checkbox_split_count = PageElement(
        css="#custIndex > section.content.no-padding > "
            "div.row.padding-top-5 > div > div > "
            "div.tab-pane.active > div > div:nth-child(1) > "
            "label:nth-child(5) > span",
        describe="勾选显示分单次数")
    split_count = PageElement(
        css=".bg-active > td:nth-child(7)", describe="列表-分单次数")
    convert_to_student = PageElement(
        # css=".bg-active > td:nth-child(12) > button:nth-child(3)",
        xpath="//*[@id=\"custIndex\"]/section[2]/"
              "div[1]/div/div/div[1]/div/div[2]/div/div[1]"
              "/table/tbody/tr[1]/td[13]/button[3]",
        describe="第一个客户转为学员按钮")
    confirm_convert = PageElement(
        xpath="/html/body/div[15]/div/div/div[2]/button[2]",
        describe="确认转为学员按钮")
    convert_success_tips = PageElement(
        xpath="/html/body/div[15]/div/div/div[3]/button",
        describe="转换成功提示按钮")
    checkbox_student = PageElement(
        xpath='//*[@id=\"custIndex\"]/section[2]/div[1]/div/div/div[1]/div/div[1]/label[11]/input',
        describe="勾选显示是否学员")
    student_or_not = PageElement(
        css='.bg-active > td:nth-child(12) > span:nth-child(1)',
        describe="列表-是否学员")
    student_name = PageElement(
        css=".bg-active > td:nth-child(3) > a:nth-child(1)",
        describe="第一位客户名称")
    customer_add_order = PageElement(
        css="div.active:nth-child(2) > div:nth-child(4) > "
            "div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > "
            "form:nth-child(1) > div:nth-child(1) > div:nth-child(4) > "
            "button:nth-child(1)",
        describe="查看客户综合信息-学员信息-客户新增订单按钮")

    # 同步教学帐号
    customer_create_account = PageElement(
        css="div.col-xs-12:nth-child(3) > table:nth-child(1) > "
            "tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(2) >"
            " span:nth-child(2)",
        describe="我的客户-客户信息-同步教学帐号按钮")
    customer_create_account_btn = PageElement(
        xpath="//*[@id=\"stuBaseDialog\"]/div/div/div[2]/div[1]/form/div[2]/button[2]",
        describe="我的客户-客户信息-同步教学帐号-创建教学平台帐号")
    customer_create_account_name = PageElement(
        xpath="//*[@id=\"userNewDialog\"]/div/div/div[2]/form/table/tbody/tr[1]/td/input",
        describe="我的客户-客户信息-同步教学帐号-创建教学平台帐号-登录账号")
    customer_create_account_password = PageElement(
        xpath="//*[@id=\"userNewDialog\"]/div/div/div[2]/form/table/tbody/tr[2]/td/input",
        describe="我的客户-客户信息-同步教学帐号-创建教学平台帐号-密码")
    customer_create_account_repeat_password = PageElement(
        xpath="//*[@id=\"userNewDialog\"]/div/div/div[2]/form/table/tbody/tr[3]/td/input",
        describe="我的客户-客户信息-同步教学帐号-创建教学平台帐号-确认密码")
    customer_create_account_birthday = PageElement(
        xpath="//*[@id=\"userNewDialog\"]/div/div/div[2]/form/table/tbody/tr[7]/td/input",
        describe="我的客户-客户信息-同步教学帐号-创建教学平台帐号-生日")
    customer_create_account_birthday_today = PageElement(
        xpath="//*[@id=\"jedatebox\"]/div[4]/div[2]/span[2]",
        describe="我的客户-客户信息-同步教学帐号-创建教学平台帐号-生日(今日)")
    customer_create_account_save = PageElement(
        xpath="//*[@id=\"userNewDialog\"]/div/div/div[3]/button[2]",
        describe="我的客户-客户信息-同步教学帐号-创建教学平台帐号-保存")
    customer_create_account_save_status = PageElement(
        xpath="/html/body/div[15]/div/div/div[1]/h4/h3",
        describe="我的客户-客户信息-同步教学帐号-创建教学平台帐号-保存状态")
    # 导入客户
    import_customer_btn = PageElement(
        xpath="//*[@id=\"custIndex\"]/section[2]/div[1]/div/div/div[1]/form/div[2]/div/button[3]",
        describe="客户管理-客户列表-导入客户")
    import_customer_school = PageElement(
        xpath="//*[@id=\"schoolId\"]",
        describe="客户管理-客户列表-导入客户-归属校区")
    import_customer_school_name = PageElement(
        xpath="//*[@id=\"schoolName\"]",
        describe="客户管理-客户列表-导入客户-来源公校")
    import_customer_info_name = PageElement(
        xpath="//*[@id=\"infoName\"]",
        describe="客户管理-客户列表-导入客户-客户来源活动")
    import_customer_select_files = PageElement(
        xpath="//*[@id=\"selectfiles\"]",
        describe="客户管理-客户列表-导入客户-选择文件")
    import_customer_postfiles = PageElement(
        xpath="//*[@id=\"postfiles\"]",
        describe="客户管理-客户列表-导入客户-开始上传")

    # 添加教务老师
    educational_detail = PageElement(
        css="li.active:nth-child(4) > a:nth-child(1) > strong:nth-child(1)",
        describe="学员信息-教务老师")
    add_educational = PageElement(
        xpath="//*[@id=\"custIndex\"]/section[2]/div[1]/div/div/div[2]/div[4]"
              "/div/div/div[4]/div[1]/div[2]/button[1]",
        describe="学员信息-教务老师-添加教务老师")
    educational_account_name = PageElement(
        xpath="//*[@id=\"eduStudentInfoDialog\"]/div/div/div[2]/form/table/tbody/tr[1]/td/input",
        describe="学员信息-教务老师-添加教务老师-教务老师账号")
    educational_invalid_date = PageElement(
        xpath="//*[@id=\"eduStudentInfoDialog\"]/div/div/div[2]/form/table/tbody/tr[2]/td/input",
        describe="学员信息-教务老师-添加教务老师-生效时间")
    educational_invalid_date_today = PageElement(css=".jedatetodaymonth", describe="生效时间-今天")
    save_educational = PageElement(
        xpath="//*[@id=\"eduStudentInfoDialog\"]/div/div/div[3]/button[2]",
        describe="保存添加教务老师")
    assert_educational = PageElement(
        xpath="//*[@id=\"custIndex\"]/section[2]/div[1]/div/div/div[2]/div[4]"
              "/div/div/div[4]/div[2]/div/div/div[1]/table/tbody/tr[1]/td[3]",
        describe="断言教务老师")


class GfyCustAddOrder(Page):
    """
    新增订单（新建、支付）
    条件：新建客户
    """
    # todo_list = PageElement(xpath="/html/body/div[15]/div/div/div[3]/button", describe="待办事项弹窗-确定")
    cust_order_info = PageElement(
        xpath='//*[@id=\"custIndex\"]/section[2]/div[1]/div/div/div[2]/div[4]/div/ul/li[1]',
        describe='我的客户-查看客户综合信息-学员订单')
    cust_order_add = PageElement(
        xpath='//*[@id=\"custIndex\"]/section[2]/div[1]/div/div/div[2]/div[4]/div/div/div[1]/form/div/div[4]/button[1]',
        describe='我的客户-查看客户综合信息-学员订单-新增')
    order_sharing_object_select = PageElement(
        css='tr.ng-scope:nth-child(2) > td:nth-child(4) > select:nth-child(1)',
        describe='创建订单-订单分成相关对象-对象名称')
    order_sharing_object_select_btn = PageElement(
        css='tr.ng-scope:nth-child(2) > td:nth-child(5) > button:nth-child(1)',
        describe='创建订单-订单分成相关对象-对象名称-确定')
    order_select_course = PageElement(css='button.pull-right:nth-child(2)', describe='创建订单-订单课程列表 -添加课程')
    order_select_coursename = PageElement(
        xpath='//*[@id=\"stuOrderCourseSchDialog\"]/div/div/div[2]/form/div[3]/div[1]/div/input',
        describe='创建订单-订单课程列表 -添加课程-输入课程名称')
    order_select_coursename_query = PageElement(css='.btn-md', describe='创建订单-订单课程列表 -添加课程-查询')
    order_select_course_btn = PageElement(
        xpath='//*[@id=\"stuOrderCourseSchDialog\"]/div/div/div[2]/div[2]/div[1]'
              '/div/table/tbody/tr[1]/td[2]/p[2]/button',
        describe='创建订单-订单课程列表 -添加课程-选择课程')
    order_selected_course = PageElement(link_text='自动化专用语文智慧月课', describe='创建订单-订单课程列表-课程')
    order_save_stu_order = PageElement(
        xpath="/html/body/div[1]/div[1]/div[1]/section[2]/div[1]/form/div[3]/div/button",
        describe='确认创建订单')

    order_status = PageElement(xpath="/html/body/div[15]/div/div/div[1]/h4/h3", describe='订单创建状态')
    """
    支付
    """
    order_list_pay = PageElement(css='.fa-cny', describe='学员信息-学员订单-操作-订单支付')
    add_order_discount_btn = PageElement(
        css='.box-info > div:nth-child(1) > table:nth-child(1) > '
            'tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(1) > button:nth-child(1)',
        describe='学员订单管理-课程优惠列表-添加优惠')
    add_order_discount_fee = PageElement(
        css='.box-info > div:nth-child(1) > table:nth-child(1) >'
            ' tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3) > input:nth-child(1)',
        describe='学员订单管理-课程优惠列表-添加优惠-金额')
    order_pre_fee = PageElement(
        xpath="/html/body/div[1]/div[1]/div[1]/section[2]/div[4]/div[1]/div/h2/span[1]/span",
        describe="支付列表-预收账款")
    order_accounts_receivable = PageElement(
        xpath="/html/body/div[1]/div[1]/div[1]/section[2]/div[1]/form/div[1]/div[3]/table/tbody/tr[2]/td/span",
        describe='缴费信息-应收账款')
    add_order_discount_save = PageElement(
        css='.box-info > div:nth-child(1) > table:nth-child(1) > '
            'tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(5) > button:nth-child(1)',
        describe='学员订单管理-课程优惠列表-添加优惠-保存按钮')

    add_order_pay_btn = PageElement(
        css="body > div.wrapper > div.content-wrapper > "
            "div:nth-child(1) > section.content > div:nth-child(4) > "
            "div.row.padding-top-5 > div > div > div > table > tbody > "
            "tr.ng-scope > td > button",
        describe='学员订单管理-课程优惠列表-添加支付项')
    add_order_pay_fee = PageElement(
        xpath='/html/body/div[1]/div[1]/div[1]/section[2]/div[4]/div[2]/div/div/div/table/tbody/tr[1]/td[3]/input',
        describe='学员订单管理-课程优惠列表-添加支付项-支付金额')
    add_order_pay_save = PageElement(
        xpath='/html/body/div[1]/div[1]/div[1]/section[2]/div[4]/div[2]/div/div/div/table/tbody/tr[1]/td[7]/button[1]',
        describe='学员订单管理-课程优惠列表-添加支付项-保存')
    add_order_orther_btn = PageElement(
        xpath="/html/body/div[1]/div[1]/div[1]/section[2]/div[5]/div[2]/div/div/div/table/tbody/tr[2]/td/button",
        describe='学员订单管理-其他费用-添加其他费用')
    add_order_otrher_fee = PageElement(
        xpath='/html/body/div[1]/div[1]/div[1]/section[2]/div[5]/div[2]/div/div/div/table/tbody/tr[1]/td[2]/input',
        describe='学员订单管理-其他费用-添加其他费用-支付金额')
    add_order_otrher_save = PageElement(
        xpath='/html/body/div[1]/div[1]/div[1]/section[2]/div[5]/div[2]/div/div/div/table/tbody/tr[1]/td[4]/button[1]',
        describe='学员订单管理-其他费用-添加其他费用-保存')
    pay_stu_order = PageElement(
        css="body > div.wrapper > div.content-wrapper > "
            "div:nth-child(1) > section.content > div:nth-child(1) > "
            "form > div:nth-child(2) > div > button",
        describe='学员订单管理-提交支付')
    pay_order_status = PageElement(
        css="body > div.bootbox.modal.fade.in > div > div > div.modal-body > div > span:nth-child(1)",
        describe='订单支付状态')
    pay_order_calculation_status = PageElement(css='span.text-green:nth-child(3)', describe='业绩计算状态')

    # 退费
    order_info_detail = PageElement(
        xpath="//*[@id=\"custIndex\"]/section[2]/div[1]/div/div/div[2]"
              "/div[4]/div/div/div[1]/div/div/div/div[1]/table/tbody"
              "/tr[1]/td[7]/button[1]",
        describe="客户综合信息-学员信息-订单详情")
    order_info_refund = PageElement(
        css="button.btn:nth-child(5)", describe="订单详情-退费按钮")
    application_for_refund = PageElement(
        # xpath="//*[@id=\"stuOrderRefundDialog\"]/div/div/div[2]/form/div/table/tbody/tr[5]/td/input",
        css="input.ng-valid-required",
        describe="退费申请-结算金额")
    save_order_refund = PageElement(
        xpath="//*[@id=\"stuOrderRefundDialog\"]/div/div/div[3]/button[2]",
        describe="退费申请-保存退费")
    save_approval_matter = PageElement(
        xpath="//*[@id=\"approvalMatterDialog\"]/div/div/div[3]/button[2]",
        describe="审批事项确认")
    assert_approval_matter = PageElement(
        xpath="/html/body/div[19]/div/div/div[1]/div",
        describe="断言审批申请")
    approval_matter = PageElement(
        xpath="/html/body/div[19]/div/div/div[2]/button",
        describe="审批申请确定")


class CustRecruitStudents(Page):
    """
    辅导招生
    """
    # 邀约
    cust_communicate_switch_tab = PageElement(
        xpath="//*[@id=\"custIndex\"]/section[2]/div[1]/div/div/div[2]/div[2]/div/ul/li[3]/a/strong",
        describe="我的客户-查看客户综合信息-沟通信息")
    cust_communicate_add = PageElement(
        xpath="//*[@id=\"custIndex\"]/section[2]/div[1]/div/div/div[2]/div[2]/div/div/div[3]/form/div/div[5]/button[1]",
        describe="我的客户-查看客户综合信息-沟通信息-新增")
    cust_communicate_responsible_personal_name = PageElement(
        xpath="//*[@id=\"custCommunicateDialog\"]/div/div/div[2]/form/table/tbody/tr[2]/td/input",
        describe="我的客户-查看客户综合信息-沟通信息-新增-跟进人")
    cust_communicate_responsible_personal_department = PageElement(
        xpath="//*[@id=\"custGuardianListDialog\"]/div/div/div[2]/div[1]/form/div[2]/div/select",
        describe="我的客户-查看客户综合信息-沟通信息-新增-跟进人-部门")
    cust_communicate_responsible_personal_query = PageElement(
        xpath="//*[@id=\"custGuardianListDialog\"]/div/div/div[2]/div[1]/form/div[3]/button",
        describe="我的客户-查看客户综合信息-沟通信息-新增-跟进人-查询")
    cust_communicate_responsible_personal_selected = PageElement(
        xpath="//*[@id=\"custGuardianListDialog\"]/div/div/div[2]/div[2]/div/div[1]/table/tbody/tr[1]/td[8]/button",
        describe="我的客户-查看客户综合信息-沟通信息-新增-跟进人-选中老师")
    cust_communicate_select_file = PageElement(
        link_text="插入文件",
        describe="我的客户-查看客户综合信息-沟通信息-新增-沟通内容-插入文件")
    cust_communicate_content = PageElement(
        xpath="/html/body/div[1]/div[1]/div[1]/div[7]/div/div/div[2]/form/table/tbody/tr[6]/td/div[1]/div[2]/div",
        describe="我的客户-查看客户综合信息-沟通信息-新增-沟通内容-内容框")
    cust_communicate_visit_date = PageElement(
        xpath="//*[@id=\"custCommunicateDialog\"]/div/div/div[2]/form/table/tbody/tr[9]/td/input",
        describe="我的客户-查看客户综合信息-沟通信息-新增-到访时间")
    cust_communicate_remark = PageElement(
        css="textarea.form-control:nth-child(1)",
        describe="我的客户-查看客户综合信息-沟通信息-新增-备注")
    cust_communicate_enable = PageElement(
        xpath="//*[@id=\"custCommunicateDialog\"]/div/div/div[3]/button[2]",
        describe="我的客户-查看客户综合信息-沟通信息-新增-确定")
    cust_communicate_status = PageElement(
        xpath="//*[@id=\"custIndex\"]/section[2]/div[1]/div/div/div[2]/div[2]/"
              "div/div/div[3]/div/div/div/div[1]/table/tbody/tr[1]/td[4]/a",
        describe="我的客户-查看客户综合信息-沟通信息-备注信息")

    # 到会

    cust_meeting_swtich_tab = PageElement(
        xpath="//*[@id=\"custIndex\"]/section[2]/div[1]/div/div/div[2]/div[2]/div/ul/li[4]/a",
        describe="我的客户-查看客户综合信息-到会信息")
    cust_meeting_add = PageElement(
        xpath="//*[@id=\"custIndex\"]/section[2]/div[1]/div/div/div[2]/div[2]/div/div/div[4]/form/div/div[3]/button[1]",
        describe="我的客户-查看客户综合信息-到会信息-新增")
    cust_meeting_user = PageElement(
        xpath="//*[@id=\"custIndex\"]/section[2]/div[1]/div/div/div[2]/div[2]"
              "/div/div/div[4]/div[1]/div/div/div[1]/table/tbody/tr[1]/td[5]/input",
        describe="我的客户-查看客户综合信息-到会信息-新增-跟进人")
    cust_meeting_parent_list = PageElement(
        xpath="//*[@id=\"custIndex\"]/section[2]/div[1]/div/div/div[2]/div[2]"
              "/div/div/div[4]/div[1]/div/div/div[1]/table/tbody/tr[1]/td[6]/select",
        describe="我的客户-查看客户综合信息-到会信息-新增-陪同人")
    cust_meeting_save = PageElement(
        xpath="//*[@id=\"custIndex\"]/section[2]/div[1]/div/div/div[2]/div[2]/div/div"
              "/div[4]/div[1]/div/div/div[1]/table/tbody/tr[1]/td[12]/button[1]",
        describe="我的客户-查看客户综合信息-到会信息-新增-保存/确认到会")
    cust_meeting_confirm_meeting = PageElement(
        xpath="//*[@id=\"model-comfirm-meeting\"]/div/div/div[2]/div/div/select",
        describe="我的客户-查看客户综合信息-到会信息-确认到会-陪同人")
    cust_meeting_confirm_save = PageElement(
        xpath="//*[@id=\"model-comfirm-meeting\"]/div/div/div[3]/button[2]",
        describe="我的客户-查看客户综合信息-到会信息-确认到会-保存")
    cust_meeting_confirm_person = PageElement(
        xpath="//*[@id=\"custIndex\"]/section[2]/div[1]/div/div/div[2]/div[2]/div/div"
              "/div[4]/div[1]/div/div/div[1]/table/tbody/tr[1]/td[8]/span[1]",
        describe="我的客户-查看客户综合信息-到会信息-确认人")
