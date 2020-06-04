from poium import Page, PageElement, PageElements


class GfyCrmCustomerManagement(Page):
    """
    crm 增加客户、客户分单、转为学员、客户回收、新增教务老师
    """

    # 客户列表
    customer_name_input = PageElement(
        xpath="//input[@ng-model='custInfoParam.custName']",
        describe="我的客户列表-客户姓名输入框")
    customer_list_school_list = PageElement(
        xpath="//select[@ng-model='custInfoParam.schoolId']",
        describe="我的客户-归属校区")
    customer_list = PageElement(
        xpath="//b[text()='客户列表']",
        describe="我的客户-客户列表")
    customer_list_load_button = PageElement(
        xpath="//button[contains(@ng-click,'loadCustInfoList')]",
        describe="我的客户-客户列表-查询按钮")
    customer_loading = PageElement(
        xpath="//div[@ng-show='custInfoLoading' and @class='overlay ng-hide']",
        describe="我的客户列表查询完结")

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
    grade = PageElements(
        xpath="//select[@name='grade']",
        describe="年级选择框")
    customer_activity = PageElement(
        xpath="//button[@ng-disabled=\"custInfoDialogType==='detail'\"]",
        describe='客户来源按钮')
    customer_business_type = PageElement(
        xpath="//select[@name='businessType']",
        describe="客户业务类型选择框")
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

    # 邀约、到会、接待
    communication_info = PageElement(
        xpath="//strong[text()='沟通信息(邀约)']",
        describe="客户信息-沟通信息(邀约)")
    meeting_info = PageElement(
        xpath="//strong[text()='到会信息']",
        describe="客户信息-到会信息")
    interview_info = PageElement(
        xpath="//strong[text()='接待信息']",
        describe="客户信息-接待信息")
    communication_loading = PageElement(
        xpath="//div[@ng-show='custCommunicateLoading' and @class='overlay ng-hide']",
        describe="沟通邀约loading")
    meeting_loading = PageElement(
        xpath="//div[@ng-show='custMeetingLoading' and @class='overlay ng-hide']",
        describe="到会信息列表loading")
    interview_loading = PageElement(
        xpath="//div[@ng-show='custAdmitLoading' and @class='overlay ng-hide']",
        describe="接待信息loading")
    communication_add = PageElement(
        xpath="//button[contains(@ng-click,'newCommunicate')]",
        describe="客户信息-新增沟通信息按钮")
    communicate_liable = PageElement(
        xpath="//input[contains(@ng-click,'setCustCommunicateDialog')]",
        describe="新增沟通信息-跟进人")
    responsible_list_loading = PageElement(
        xpath="//div[@ng-show='custResponsibleDialogLoading' and @class='overlay ng-hide']",
        describe="跟进人列表loading")
    responsible_dialog = PageElement(
        xpath="//div[@id='custResponsibleDialog' and @class='modal fade in']",
        describe="跟进人弹窗dialog")
    textarea = PageElement(
        xpath="//div[@contenteditable='true']",
        describe="富文本框")
    save_communication = PageElement(
        xpath="//button[@ng-click='saveCustCommunication()']",
        describe="保存沟通信息")
    meeting_add = PageElement(
        xpath="//button[contains(@ng-if,'crm_cust_meeting_add')]",
        describe="到会信息-新增到会信息")
    confirm_meeting = PageElement(
        xpath="//button[@title='确认到会']",
        describe="到会信息-确认到会")
    meeting_liable_name = PageElement(
        xpath="//input[@ng-model='custMeetingDialog.userName']",
        describe="到会信息-选择跟进人")
    meeting_time = PageElement(
        xpath="//input[@ng-model='custMeetingDialog.meetingTime']",
        describe="到会信息-到会时间")
    save_meeting = PageElement(
        xpath="//button[@ng-click='saveCustMeeting(custMeetingDialog)']",
        describe="到会信息-保存到会信息")
    meeting_meeting_dialog = PageElement(
        xpath="//div[@class='modal fade in' and @id='model-comfirm-meeting']",
        describe="到会信息-确认到会模态框")
    meeting_confirm_parent_name = PageElement(
        xpath="//select[@ng-model='modalEscortType']",
        describe="确认到会信息-选择陪同人")
    meeting_add_parent_name = PageElement(
        xpath="//select[@ng-model='custMeetingDialog.escortType']",
        describe="新增到会信息-选择陪同人")
    save_meeting_confirm = PageElement(
        xpath="//button[@ng-click='confirmCustMeeting()']",
        describe="到会信息-保存确认到会")
    interview_add = PageElement(
        xpath="//button[contains(@ng-if,'crm_cust_admit_add')]",
        describe="到会信息-新增接待信息")
    admit_liable_name = PageElement(
        xpath="//input[@ng-model='custAdmitDialog.userName']",
        describe="接待信息-接待人")
    save_admit = PageElement(
        xpath="//button[contains(@ng-click,'custAdmitDialog')]",
        describe="接待信息-保存接待信息按钮")
    add_interview = PageElement(
        xpath="//button[@title='新增面谈结果']",
        describe="接待信息-新增面谈结果按钮")
    save_interview = PageElement(
        xpath="//button[@ng-click='saveCustInterviewResult()']",
        describe="接待信息-保存面谈结果")
    confirm_admit = PageElement(
        xpath="//button[@title='确认接待']",
        describe="接待信息-确认接待按钮")
    visit_date = PageElement(
        xpath="//input[@name='visitDate']",
        describe="到访时间输入框")
    communicate_dialog = PageElement(
        xpath="//div[@class='modal fade in' and @id='custCommunicateDialog']",
        describe="新增沟通信息模态框")
    communicate_result = PageElement(
        xpath="//span[contains(@ng-repeat,'dicCodeDomainIsEffectList')]",
        describe="沟通结果")
    is_visit = PageElement(
        xpath="//span[contains(@ng-repeat,'dicCodeDomainIsPromiseVisitList')]",
        describe="承诺到访结果")
    meeting_result = PageElement(
        xpath="//span[contains(@ng-repeat,'dicCodeDomainMeetingStatusList')]",
        describe="到会结果")
    responsible_list_dialog = PageElement(
        xpath="//div[@class='modal fade in' and @id='custGuardianListDialog']",
        describe="接待人列表选择模态框")
    admit_result = PageElement(
        xpath="//span[contains(@ng-repeat,'dicCodeDomainAdmitStatusList')]",
        describe="接待结果")

    # 业务意向
    business_intent = PageElement(
        xpath="//strong[text()='业务意向']",
        describe="客户信息-业务意向")
    new_business_intent = PageElement(
        xpath="//button[@ng-click=\"toEditCustBusinessIntent('newBusinessIntent')\"]",
        describe="客户信息-业务意向-新增")
    choice_activity_name = PageElement(
        xpath="//input[@ng-model='custBusinessIntentDialog.activityName']",
        describe="客户信息-业务意向-新增-点击选择活动名称")
    # 活动列表
    activity_school = PageElement(
        xpath="//select[@ng-model='parentActivityParam.schoolId']",
        describe="活动列表-所属校区")
    activity_list_business_type = PageElement(
        xpath="//div[@class='input-group']/div[@ng-model='parentActivityParam.activityType']/div/button",
        describe="活动列表-活动类型")
    activity_type_touched = PageElement(
        # xpath="//input[@class='form-control ng-pristine ng-untouched ng-valid' and @ng-model='gfySelectSearch']",
        xpath='//*[@id=\"marActivityListDialog\"]/div/div/div[2]/form/div[1]/div[2]/div/div[2]/div/div/input',
        describe="活动列表-活动类型-输入框")

    activity_name = PageElement(
        xpath="//input[@name='activityName']",
        describe='活动列表-活动名称')
    activity_query = PageElement(
        xpath="//button[@ng-click='parentActivityDialogLoad(1,pageInfoDialog.pageSize)']",
        describe='活动列表-活动列表查询按钮')
    activity_selected = PageElement(
        # link_text="选中活动",
        # xpath='//*[@id="marActivityListDialog"]/div/div/div[2]/div[1]/div/div[1]/table/tbody/tr[1]/td[6]/a',
        xpath="//a[@ng-click='parentActivityDialogSelect(item)']",
        describe="选择活动")
    activity_save = PageElement(
        xpath="//button[@ng-click='saveCustBusinessIntent()']",
        describe="保存业务意向按钮")
    # 客户跟进人
    responsible_add = PageElement(
        xpath="//button[@ng-click=\"toEditCustResponsible('newResponsible')\"]",
        describe="客户综合信息-客户跟进人-新增")
    responsible_name_input = PageElement(
        xpath="//input[@placeholder='责任人非空']",
        describe="客户跟进人-新增-跟进人姓名")
    responsible_save = PageElement(
        xpath="//button[@ng-click='saveCustResponsible()']",
        describe="客户跟进人-新增-保存跟进人按钮")
    user_list_dialog = PageElement(
        xpath="//div[@id='userListDialog' and @class='modal fade in']",
        describe="机构老师列表")
    customer_phone = PageElement(
        xpath="//input[@name='phone1']",
        describe='联系方式输入框1')
    add_customer_save = PageElements(
        xpath="//button[@ng-click='saveCustInfo()']",
        describe='客户创建保存按钮')
    save_status = PageElement(
        xpath="//strong[text()='保存成功']",
        describe="添加客户保存成功状态")
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
    choose_teacher_a = PageElement(
        # xpath="//a[text()='选中老师']",
        link_text="选中老师",
        describe="选择老师")
    choose_teacher_button = PageElement(
        xpath="//button[text()='选中老师']",
        # link_text="选中老师",
        describe="选择老师")
    teacher_list_school = PageElement(
        xpath="//select[@ng-model='teacherInfoParam.schoolId']",
        describe="机构老师列表-归属校区")
    teacher_list_loading = PageElement(
        xpath="//div[@ng-show='teacherInfoLoading' and @class='overlay ng-hide']",
        describe="机构老师列表查询完结")

    confirm_split = PageElement(
        xpath="//button[@ng-click='allotOrder()']",
        describe="确认分单按钮")
    checkbox_split_count = PageElement(
        xpath="//span[text()='分单次数']",
        describe="勾选显示分单次数")
    # 只勾选分单次数和联系方式
    split_count = PageElement(
        css=".bg-active > td:nth-child(7)",
        describe="列表-分单次数")
    split_customer = PageElement(
        css=".bg-active > td:nth-child(9)",
        describe="列表-主跟进人")
    batch_convert_student = PageElement(
        xpath="//button[text()='转为学员']",
        describe="批量转为学员按钮")
    convert_to_student = PageElement(
        xpath="//button[@ng-click='changeToStu(item)']",
        describe="客户管理列表-第一名客户转为学员按钮")
    convert_confirm = PageElement(
        xpath="//button[@ng-disabled='!messageJson.inputValue']",
        describe="我的客户-转为学员确定")
    convert_success_text = PageElement(
        xpath="//h3[text()='转为学员保存成功']",
        describe="转换成功文字提示")
    convert_success_tips = PageElement(
        xpath="//span[text()='该客户已经是学员！']",
        describe="转为学员失败提示")
    confirm_btn = PageElement(
        xpath="//button[@data-bb-handler='confirm']",
        describe="确认按钮")
    cancel_btn = PageElement(
        xpath="//button[@data-bb-handler='Cancel']",
        describe="取消按钮")
    customer_ok_button = PageElement(
        xpath="//button[@data-bb-handler='ok']",
        describe="转换成功确认按钮")

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
    customer_info = PageElement(
        xpath="//li[@ng-class=\"{'integration':'active'}[customerType]\" and @class='active']",
        describe="查看客户综合信息-选中")
    customer_create_account = PageElement(
        xpath="//button[contains(.,'同步教学账号')]",
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
    customer_create_account_like = PageElement(
        xpath="//input[@ng-model='stuBaseUserInfoParam.loginNameLike']",
        describe="我的客户-客户信息-同步教学帐号-输入教学帐号")
    customer_create_account_query = PageElement(
        xpath="//button[@ng-click='loadStuBaseUserInfoList()']",
        describe="我的客户-客户信息-同步教学帐号-查询")
    customer_create_account_select = PageElement(
        xpath="//button[@ng-click='selectStuBaseUserInfo(item)']",
        describe="我的客户-客户信息-同步教学帐号-选择账号")

    # 客户回收
    customer_recovery = PageElements(
        xpath="//button[@ng-click='allotRecovery(item)']",
        describe="我的客户-回收按钮")
    customer_multi_recovery = PageElement(
        xpath="//button[text()='批量回收']",
        describe="我的客户-批量回收按钮")
    customer_recovery_status = PageElement(
        xpath="//strong[text()='保存成功']",
        describe="回收成功状态")
    customer_is_deal = PageElement(
        xpath="//select[@ng-model='custInfoParam.isDeal']",
        describe="我的客户-是否成交选择框")
    customer_is_order = PageElement(
        xpath="//select[@ng-model='custInfoParam.isOrder']",
        describe="我的客户-是否分单选择框")
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
    customer_recovery_date = PageElements(
        xpath="//td[@ng-if=\"customerColShow['回收时间']\"]",
        describe="我的客户-回收时间")
    customer_recovery_teacher = PageElements(
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
