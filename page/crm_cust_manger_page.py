from poium import Page, PageElement, PageElements


class GfyCrmCustomerManagement(Page):
    """
    crm 增加客户、客户分单、转为学员、客户回收、新增教务老师
    """
    # 客户列表
    customer_list_school_list = PageElement(
        xpath="//select[@ng-model='custInfoParam.schoolId']",
        describe="我的客户-归属校区")
    customer_list = PageElement(
        xpath="//b[text()='客户列表']",
        describe="我的客户-客户列表")
    # 新增客户
    add_customer = PageElement(
        xpath="//button[@ng-click=\"toEditCustInfo('newCust')\"]",
        describe="客户管理-新增客户按钮")
    add_customer_name = PageElement(
        xpath="//input[@ng-model='custInfoDialog.custName']",
        describe='新增客户名称')
    school_name = PageElement(
        xpath="//input[@ng-model='custInfoDialog.schoolName']",
        describe='新建客户-公校名称')
    pub_school_list = PageElement(
        xpath="//input[@ng-model='parentSchoolDialogParam.schoolName']",
        describe='新建客户-公校列表-公校名称输入框')
    pub_school_query = PageElement(
        xpath="//button[@ng-click='parentSchoolDialogLoad()']",
        describe='新建客户-公校名称-公校列表-查询')
    pub_school_choice = PageElement(
        link_text='选定学校',
        describe='新建客户-公校名称-公校列表-选择学校')
    grade = PageElement(
        xpath="//select[@ng-change=\"custInfoDialog.className=''\"]",
        describe="年级选择框")
    customer_activity = PageElement(
        xpath="//button[@ng-disabled=\"custInfoDialogType==='detail'\"]",
        describe='客户来源按钮')

    # 编辑客户
    customer_edit_button = PageElements(
        xpath="//button[@title='编辑']",
        describe="客户列表-编辑客户按钮")
    edit_customer_parentSet = PageElement(
        xpath="//input[@value='F01']",
        describe="客户列表-编辑家长关系")
    edit_customer_sex = PageElement(
        xpath="//input[@ng-model='custInfoDialog.sex'][@value='S02']",
        describe="客户列表-编辑性别")
    edit_customer_school = PageElement(
        xpath="//select[@name='belongSchoolId']",
        describe="客户列表-编辑校区")
    edit_customer_intentLevel = PageElement(
        xpath="//select[@name='intentLevel']",
        describe="客户列表-编辑意向级别")
    edit_customer_type = PageElement(
        xpath="//select[@name='custType']",
        describe="客户列表-编辑客户类型")

    # 活动列表
    activity_school = PageElement(
        xpath="//select[@ng-model='parentActivityParam.schoolId']",
        describe="活动列表-所属校区")
    activity_name = PageElement(
        xpath="//input[@name='activityName']",
        describe='活动列表-活动名称')
    activity_query = PageElement(
        xpath="//button[@ng-click='parentActivityDialogLoad(1,pageInfoDialog.pageSize)']",
        describe='活动列表查询按钮')
    activity_selected = PageElement(
        link_text="选中活动",
        describe="选择活动")
    customer_phone = PageElement(
        xpath="//input[@name='phone1']",
        describe='联系方式输入框1')
    add_customer_save = PageElements(
        # xpath="//button[@ng-show=\"custInfoDialogType==='edit'||custInfoDialogType==='add'\"]",
        xpath="//button[@ng-click='saveCustInfo()']",
        describe='客户创建保存按钮')
    customer_name = PageElement(
        xpath="//a[@ng-click='selectCust(item)'][1]",
        describe='我的客户-客户管理列表排第一的客户名称')
    customer_check = PageElements(
        xpath="//input[@ng-model='item.selectState']",
        describe="我的客户-勾选客户")
    customer_split = PageElement(
        xpath="//button[@ng-click=\"$parent.openTeacherDialog(toAllotOrder,'')\"]",
        describe="分单按钮")
    # 机构老师列表
    teacher_attribution_department = PageElement(
        xpath="//select[@ng-model='teacherInfoParam.departmentId']",
        describe="归属部门")
    teacher_list_login_name = PageElement(
        xpath="//input[@ng-model='teacherInfoParam.loginName']",
        describe="机构老师列表-登录名输入框")
    teacher_list_query = PageElement(
        xpath="//button[@ng-click='loadTeacherInfoList()']",
        describe="机构老师列表-查询按钮")
    teacher_select = PageElement(
        link_text="选中老师",
        describe="选择老师")
    teacher_list_school = PageElement(
        xpath="//select[@ng-model='teacherInfoParam.schoolId']",
        describe="机构老师列表-归属校区")

    confirm_split = PageElement(
        xpath="//button[@ng-click='allotOrder()']",
        describe="确认分单按钮")
    checkbox_split_count = PageElement(
        xpath="//span[text()='分单次数']",
        # xpath="//input[@ng-model=\"customerColShow['分单次数']\"]",
        describe="勾选显示分单次数")
    # 只勾选分单次数和联系方式
    split_count = PageElement(
        css=".bg-active > td:nth-child(7)",
        describe="列表-分单次数")
    split_customer = PageElement(
        css=".bg-active > td:nth-child(10)",
        describe="列表-主跟进人")
    convert_to_student = PageElement(
        xpath="//button[@ng-click='changeToStu(item)']",
        describe="客户管理列表-第一名客户转为学员按钮")
    convert_confirm = PageElement(
        xpath="//button[@ng-disabled='!messageJson.inputValue']",
        describe="我的客户-转为学员确定")
    confirm_btn = PageElement(
        xpath="//button[@data-bb-handler='confirm']",
        describe="确认按钮")
    cancel_btn = PageElement(
        xpath="//button[@data-bb-handler='Cancel']",
        describe="取消按钮")
    customer_ok_button = PageElement(
        xpath="//button[@data-bb-handler='ok']",
        describe="转换成功确认按钮")
    convert_success_text = PageElement(
        xpath="//span[@class='text-green']",
        describe="转为学员-转换成功提示文字")
    student_or_not = PageElement(
        css='.bg-active > td:nth-child(12) > span:nth-child(1)',
        describe="列表-是否学员")
    first_student_name = PageElement(
        xpath="//a[@ng-click='selectCust(item)']",
        describe="客户管理列表-第一位客户名称")
    customer_add_order = PageElement(
        css="div.active:nth-child(2) > div:nth-child(4) > "
            "div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > "
            "form:nth-child(1) > div:nth-child(1) > div:nth-child(4) > "
            "button:nth-child(1)",
        describe="查看客户综合信息-学员信息-客户新增订单按钮")

    # 同步教学帐号
    customer_create_account = PageElement(
        xpath="//button[@class='btn btn-primary btn-xs']",
        describe="我的客户-客户信息-同步教学帐号按钮")
    customer_create_account_btn = PageElement(
        xpath="//button[@ng-click='stuBaseCreateStudentAccount(stuBaseUserCallBack.param,"
              "stuBaseUserCallBack.loadFun)']",
        describe="我的客户-客户信息-同步教学帐号-创建教学平台帐号")
    customer_create_account_name = PageElement(
        xpath="//input[@ng-model='userStudentAccountInfo.loginName']",
        describe="我的客户-客户信息-同步教学帐号-创建教学平台帐号-登录账号")
    customer_create_account_password = PageElement(
        xpath="//input[@type='password']",
        describe="我的客户-客户信息-同步教学帐号-创建教学平台帐号-密码")
    customer_create_account_repeat_password = PageElement(
        xpath="//input[@ng-model='passwordNoTemp']",
        describe="我的客户-客户信息-同步教学帐号-创建教学平台帐号-确认密码")
    customer_create_account_birthday = PageElement(
        xpath="//input[@name='birthDate']",
        describe="我的客户-客户信息-同步教学帐号-创建教学平台帐号-生日")
    customer_create_account_birthday_today = PageElement(
        xpath="//span[@class='jedatetodaymonth']",
        describe="我的客户-客户信息-同步教学帐号-创建教学平台帐号-生日(今日)")
    customer_create_account_save = PageElement(
        xpath="//button[@ng-click='addStuInfo()']",
        describe="我的客户-客户信息-同步教学帐号-创建教学平台帐号-保存")
    customer_create_account_save_status = PageElement(
        xpath="//span[@ng-show='integrationStuInfo.accountNo']",
        describe="我的客户-客户信息-同步教学帐号-教学帐号")

    # 客户回收
    customer_recovery = PageElement(
        xpath="//button[@ng-click='allotRecovery(item)']",
        describe="我的客户-回收按钮")
    customer_recovery_status = PageElement(
        xpath="//strong[text()='保存成功']",
        describe="回收成功状态")
    customer_teacher = PageElements(
        # xpath="//*[@id=\"custIndex\"]/section[2]/div[1]/div/div/div[1]"
        #       "/div/div[2]/div/div[1]/table/tbody/tr[1]/td[9]",
        xpath="//td[@class='ng-binding']",
        describe="我的客户-客户的主跟进人名称")
    customer_recovery_date_button = PageElement(
        xpath="//span[text()='回收时间']",
        describe="回收时间勾选按钮")
    customer_recovery_teacher_button = PageElement(
        xpath="//span[text()='回收跟进人']",
        describe="回收跟进人勾选按钮")
    customer_recovery_date = PageElement(
        xpath="//td[@ng-if=\"customerColShow['回收时间']\"]",
        describe="我的客户-回收时间")
    customer_recovery_teacher = PageElement(
        xpath="//td[@ng-if=\"customerColShow['回收跟进人']\"]",
        describe="我的客户-第一位客户回收跟进人")

    """
    新增教务老师
    """
    student_educational = PageElement(
        xpath="//strong[text()='教务老师']",
        describe="客户综合信息-学员信息-教务老师按钮")
    student_educational_add = PageElement(
        xpath="//button[@ng-click=\"eduStudentRelationOpen('add','',studentInfo)\"]",
        describe="客户综合信息-学员信息-新增教务老师按钮")
    educational_account_name = PageElement(
        xpath="//input[@name='educationalAccountName']",
        describe="学员教务老师-选择教务老师")
    educational_effect_date = PageElement(
        xpath="//input[@name='effDate']",
        describe="学员教务老师-选择生效时间")
    student_educational_save = PageElement(
        xpath="//button[@ng-click='eduStudentRelationAdd()']",
        describe="学员教务老师-保存")
    add_educational_status = PageElement(
        xpath="/html/body/div[21]/div/div/div/div/div/strong",
        describe="学员教务老师新增状态")


class GfyCustomerAddOrder(Page):
    """
    新增订单（新建、支付、退费）
    条件：新建客户
    """
    customer_order_info = PageElement(
        xpath="//a[@ng-click=\"switchTab('StuOrderInfo','student')\"]",
        describe='我的客户-查看客户综合信息-学员订单')
    customer_order_add = PageElement(
        xpath="//button[@ng-click=\"toStuOrderDetail('orderNew')\"]",
        describe='我的客户-查看客户综合信息-学员订单-新增')
    order_sharing_object_select = PageElement(
        xpath="//select[@title='分成对象']",
        describe='创建订单-订单分成相关对象-对象名称')
    order_sharing_object_select_btn = PageElement(
        xpath="//button[@ng-click='stuOrderRelationObjectAdd(item,$index)']",
        describe='创建订单-订单分成相关对象-对象名称-确定')
    order_select_course = PageElement(
        xpath="//button[@ng-click='toStuSelectCourse()']",
        describe='创建订单-订单课程列表 -添加课程')
    order_select_course_name = PageElement(
        xpath="//input[@ng-model='stuSchCourseParam.courseName']",
        describe='创建订单-订单课程列表 -添加课程-课程名称输入框')
    order_select_course_name_query = PageElement(
        xpath="//button[@ng-click='stuLoadSchCourseList()']",
        describe='创建订单-订单课程列表 -添加课程-查询按钮')
    order_select_course_btn = PageElement(
        xpath="//button[@ng-click='stuSelectCourse(item)']",
        describe='创建订单-订单课程列表 -添加课程-选择课程')
    order_save_stu_order = PageElement(
        xpath="//button[@ng-click='saveStuOrder()']",
        describe='创建订单-确认创建订单按钮')
    order_status = PageElement(
        xpath="//span[@class='text-green']",
        describe='订单创建状态')
    order_status_confirm = PageElement(
        xpath="//button[@data-bb-handler='ok']",
        describe="确认订单保存状态按钮")
    order_info_loadStuOrderList = PageElement(
        xpath="//button[@ng-click='loadStuOrderList()']",
        describe="客户管理-学员信息-学员订单查询")
    order_info_totalNum = PageElements(
        xpath="//span[@ng-show='pageInfo.totalNum']",
        describe="客户管理-学员信息-学员订单总订单数")

    """
    支付
    """
    student_order_pay_btn = PageElement(
        xpath="//button[@title='订单支付']",
        describe="学员订单管理-列表第一个学员订单支付按钮")
    add_order_discount_btn = PageElement(
        xpath="//button[@ng-disabled='financeDiscountDetailEditingItem']",
        describe='学员订单管理-课程优惠列表-添加优惠按钮')
    add_order_discount_fee = PageElement(
        xpath="//input[@placeholder='优惠金额']",
        describe='学员订单管理-课程优惠列表-添加优惠-金额输入框')
    add_order_discount_save = PageElement(
        xpath="//button[@ng-click=\"toEditFinanceDiscountDetail(item,'discountAdd')\"]",
        describe='学员订单管理-课程优惠列表-添加优惠-保存按钮')
    order_pre_fee = PageElement(
        xpath="/html/body/div[1]/div[1]/div[1]/section[2]/div[4]/div[1]/div/h2/span[1]/span",
        # xpath="//span[@class='ng-binding']",
        describe="支付列表-预收账款")
    order_accounts_receivable = PageElement(
        xpath="/html/body/div[1]/div[1]/div[1]/section[2]/div[1]/form/div[1]/div[3]/table/tbody/tr[2]/td/span",
        # xpath="//span[@class='ng-binding']",
        describe='缴费信息-应收账款')
    add_order_pay_btn = PageElement(
        xpath="//button[@ng-disabled='financePayDetailEditingItem']",
        describe='学员订单管理-课程优惠列表-添加支付项')
    add_order_pay_fee = PageElement(
        xpath="//input[@ng-model='financePayDetailDialog.payFee']",
        describe='学员订单管理-课程优惠列表-添加支付项-支付金额')
    add_order_pay_save_btn = PageElement(
        xpath="//button[@ng-click=\"toEditFinancePayDetail('','payAdd')\"]",
        describe='学员订单管理-支付列表 -添加支付项-保存按钮')
    add_order_other_btn = PageElement(
        xpath="//button[@ng-click=\"toEditFinanceOtherFeeDetail('','otherFeeNew')\"]",
        describe='学员订单管理-其他费用-添加其他费用')
    add_order_other_fee = PageElement(
        xpath="//input[@ng-model='financeOtherFeeDetailDialog.fee']",
        describe='学员订单管理-其他费用-添加其他费用-支付金额输入框')
    add_order_other_save = PageElement(
        xpath="//button[@ng-click=\"toEditFinanceOtherFeeDetail('','otherFeeAdd')\"]",
        describe='学员订单管理-其他费用-添加其他费用-保存')
    pay_stu_order = PageElement(
        xpath="//button[@ng-click='payStuOrder()']",
        describe='学员订单管理-提交支付')
    pay_order_status = PageElement(
        xpath="//span[@class='text-green'][1]",
        describe='订单支付-支付成功订单支付状态')
    pay_order_calculation_status = PageElement(
        xpath="//span[@class='text-green'][2]",
        describe='订单支付-支付成功业绩计算状态')
    OK_button = PageElement(
        xpath="//button[@data-bb-handler='OK']",
        describe="确认按钮")
    ok_button = PageElement(
        xpath="//button[@data-bb-handler='ok']",
        describe="确认按钮")
    pay_order_stay = PageElement(
        xpath="/html/body/div[19]/div/div/div[3]/button[1]",
        describe="支付成功后留在当前页面按钮")
    pay_cancel_button = PageElement(
        xpath="//button[@data-bb-handler='Cancel']",
        describe="取消按钮")

    """
    退费
    """
    order_detail = PageElement(
        xpath="//i[@class='fa fa-fw fa-search']",
        describe="学员订单管理-第一名学员的订单详情按钮")
    order_customer_name = PageElement(
        xpath="//*[@id=\"stuOrderRefundDialog\"]/div/div/div[2]/form/div/table/tbody/tr[1]/td[2]",
        describe="订单详情-退费申请-学员名称")
    order_id = PageElement(
        xpath="//*[@id=\"stuOrderRefundDialog\"]/div/div/div[2]/form/div/table/tbody/tr[1]/td[1]",
        describe="订单详情-退费申请-订单编号")
    order_info_refund = PageElement(
        xpath="//button[@ng-click=\"stuToRefund(item,'refund')\"]",
        describe="订单详情-退费按钮")
    application_for_refund = PageElement(
        xpath="//input[@name='refundFee']",
        describe="退费申请-结算金额")
    refund_pre_fee = PageElement(
        xpath="/html/body/div[1]/div[1]/div[1]/div[2]/div/div/div[2]/form/div/table/tbody/tr[2]/td[2]",
        describe="退费申请-预收金额")
    refund_course_count = PageElement(
        xpath="//*[@id=\"stuOrderRefundDialog\"]/div/div/div[2]/form/div/table/tbody/tr[5]/td[1]/span",
        describe="退费申请-订购数量")

    refund_course_consume = PageElement(
        xpath="//*[@id=\"stuOrderRefundDialog\"]/div/div/div[2]/form/div/table/tbody/tr[5]/td[2]/span",
        describe="退费申请-消耗数量")
    refund_remark = PageElement(
        xpath="//textarea[@name='remark']",
        describe="退费申请-备注")
    save_order_refund = PageElement(
        xpath="//button[@ng-click='stuOrderSaveFinanceRefundApply()']",
        describe="退费申请-保存退费按钮")
    approval_confirm_account = PageElement(
        xpath="//*[@id=\"approvalMatterDialog\"]/div/div/div[2]/table/tbody/tr[5]/td/span",
        describe="审批事项确认-审批流程账号")
    approval_matter_setting = PageElement(
        xpath="//select[@title='选择审批流程']",
        describe="审批事项确认-审批流程选择框")
    save_approval_matter = PageElement(
        xpath="//button[@ng-click='saveApprovalMatter(approvalMatter)']",
        describe="审批事项确认按钮")
    approval_matter_status = PageElement(
        xpath="//div[@class='bootbox-body']",
        describe="断言审批申请")


class GfyCustomerDataEliminate(Page):
    """
    清理数据
    """
    customer_eliminate = PageElements(
        xpath="//button[@title='删除']",
        describe="我的客户-客户删除按钮")
    eliminate_confirm = PageElement(
        xpath="//button[@data-bb-handler='confirm']",
        describe="确认删除按钮")
