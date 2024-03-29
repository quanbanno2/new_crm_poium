from poium import Page, PageElement, PageElements


class GfyCrmStudentInClassManagement(Page):
    """
    学员上课管理
    """
    in_class_table = PageElement(
        xpath="//a[@ng-click=\"changeInClassType('inClass')\"]",
        describe="学员上课tab")
    # 新增上课记录
    add_in_class_record = PageElement(
        xpath="//button[@ng-click=\"toEditStuCourseInClassRecord('add','')\"]",
        describe="学员上课-新增按钮")
    makeup_school_list = PageElement(
        xpath="//select[@ng-model='stuClassDialog.schoolId']",
        describe="新增课程上课记录-归属校区选择框")
    makeup_class_name = PageElement(
        xpath="//input[@placeholder='点击选择课程班级']",
        describe="新增课程上课记录-课程班级")
    select_a_classes_search = PageElement(
        xpath="//input[@placeholder='关键信息匹配查询']",
        describe="新增课程上课记录-课程班级-关键字搜索输入框")
    select_a_classes = PageElement(
        link_text="选中班级",
        describe="新增课程上课记录-课程班级-选中班级按钮")
    makeup_time_cycle = PageElement(
        xpath="//select[@title='时间周期']",
        describe="新增课程上课记录-时间周期")
    makeup_in_class_date = PageElement(
        xpath="//input[@name='inclassDate']",
        describe="新增课程上课记录-开始时间")
    makeup_in_class_date_today = PageElement(
        xpath="//span[@class='jedatetodaymonth']",
        describe="新增课程上课记录-开始时间-今天")
    makeup_save = PageElement(
        xpath="//button[@ng-click='addStuCourseInClassRecord()']",
        describe="新增课程上课记录-保存按钮")
    status = PageElement(
        xpath="//div[@class='bootbox-body']",
        describe="弹出窗保存状态")
    ok_button = PageElement(
        xpath="//button[@data-bb-handler='ok']",
        describe="弹出窗保存状态确认按钮")
    add_in_class_title = PageElement(
        xpath="//h4[text()='新增课程上课记录']",
        describe="新增课程上课记录title")
    delete_button = PageElement(
        xpath="//button[text()='删除']",
        describe="学员上课管理-删除上课记录按钮")

    # 点名
    teacher_class_list = PageElement(
        xpath="//select[@ng-model='stuCourseInClassRecordParam.classId']",
        describe="学员上课管理-老师班级选择框")
    query_in_class_record = PageElement(
        xpath="//button[@ng-click='loadStuCourseInClassRecordList(1,initPageInfo.pageSize)']",
        describe="学员上课管理-查询按钮")
    in_class_record = PageElement(
        xpath="//tr[@ng-repeat='item in stuCourseInClassRecordList']/td[3]",
        describe="学员上课管理-上课记录")
    in_class_school_list = PageElement(
        xpath="//select[@ng-model='stuCourseInClassRecordParam.schoolId']",
        describe="学员上课管理-归属校区下拉框")
    in_class_status_list = PageElement(
        xpath="//select[@ng-model='stuCourseInClassRecordParam.status']",
        describe="学员上课管理-状态下拉框")
    in_class_sign = PageElement(
        # xpath="//button[@ng-click=\"toEditStuCourseInClassRecord('sign',item)\"]",
        xpath="//button[text()='点名']",
        describe="学员上课管理-点名按钮")
    in_class_sign_save = PageElement(
        # xpath="//button[@ng-click='stuClassSaveStuCourseDetail()']",
        xpath="//button[@ng-if='classFlagObj.flag']",
        describe="学员上课点名-保存点名按钮")
    in_class_sign_confirm = PageElement(
        xpath="//button[@data-bb-handler='confirm']",
        describe="学员上课点名-确认点名按钮")
    in_class_edit = PageElement(
        xpath="//button[@ng-click=\"toEditStuCourseInClassRecord('edit',item)\"]",
        describe="学员上课管理-记录调整")

    # 请假
    in_class_leave = PageElement(
        xpath="//button[@ng-click=\"toEditStuCourseInClassRecord('leave',item)\"]",
        describe="学员上课管理-请假按钮")
    in_class_leave_student = PageElement(
        xpath="//span[text()='自动化测试学生']",
        describe="学员上课管理-选择学生请假")
    in_class_leave_type = PageElement(
        xpath="//select[@title='请假类型']",
        describe="学员上课管理-请假-请假类型选择框")
    in_class_leave_save = PageElement(
        xpath="//button[@ng-click='studentLeaveAdd()']",
        describe="学员上课管理-保存请假按钮")
    in_class_record_tab = PageElement(
        xpath="//a[@ng-click=\"changeInClassType('classSales')\"]",
        describe="学员上课管理-上课记录tab")
    record_teacher_list = PageElement(
        xpath="//select[@ng-model='stuCourseInClassRecordForSalesParam.classId']",
        describe="上课记录-老师班级列表")
    record_query = PageElement(
        xpath="//button[@ng-click='stuCourseInClassRecordForSalesLoadList(1,pageInfoSecond.pageSize)']",
        describe="上课记录-查询按钮")
    record_detail = PageElement(
        xpath="//button[@ng-click=\"toGetInClassRecordForSales('detail',item)\"]",
        describe="上课记录-查看明细")

    # 补课
    make_up_student_name_input = PageElement(
        xpath="//input[@name='studentName']",
        describe="补课管理-学员姓名输入框")
    make_up_student_name = PageElements(
        xpath="//tr[@ng-repeat='item in stuLeaveDetailList']/td[12]",
        describe="补课管理-查询数据第一行的学员姓名")
    query_makeup_student = PageElement(
        xpath="//button[@ng-click='loadStuLeaveDetail(1,pageInfo.pageSize)']",
        describe="补课管理-查询按钮")
    cancel_makeup = PageElement(
        xpath="//button[@title='撤销请假']",
        describe="补课管理-撤销请假")
    cancel_makeup_confirm = PageElement(
        xpath="//button[@ng-click='messageCallBack(true,messageJson.inputValue)']",
        describe="补课管理-撤销请假确认")
    plan_student_makeup = PageElement(
        xpath="//button[@ng-click='stuToMakeup(item)']",
        describe="补课管理-安排补课")
    makeup_select_class = PageElement(
        xpath="//button[@ng-click='stuMakeupSelectClass(item)']",
        describe="补课管理-选择补课班级")
    leave_status_select = PageElement(
        xpath="//select[@ng-model='stuLeaveDetailParam.makeupType']",
        describe="补课管理-补课状态下拉框")


class GfyStudentOrderManagement(Page):
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
    order_sharing_object_select = PageElements(
        xpath="//select[@title='分成对象']",
        describe='创建订单-订单分成相关对象-对象名称')
    order_sharing_object_select_btn = PageElement(
        xpath="//button[@ng-click='stuOrderRelationObjectAdd(item,$index)']",
        timeout=1,
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
    order_school_list = PageElement(
        xpath="//select[@title='选择校区']",
        describe="订单详情-添加课程-选择校区")
    order_subject_group = PageElement(
        xpath="//select[@ng-model='item.sharingObjectType']",
        describe="订单详情-分成对象类型-科组选择")
    student_order_loading = PageElement(
        xpath="//div[@ng-show='stuOrderLoading' and @class='overlay ng-hide']",
        describe="学员订单列表查询完结")
    """
    支付
    """
    student_order_id = PageElement(
        xpath="//input[@name='orderId']",
        describe="学员订单管理-订单编号")
    student_order_school_id = PageElement(
        xpath="//select[@ng-model='stuOrderParam.schoolId']",
        describe="学员订单管理-归属校区下拉框")
    student_order_pay_btn = PageElement(
        xpath="//button[@title='订单支付']",
        describe="学员订单管理-列表第一个学员订单支付按钮")
    add_order_discount_btn = PageElement(
        xpath="//button[text()='添加优惠']",
        describe='学员订单管理-课程优惠列表-添加优惠按钮')
    add_order_discount_fee = PageElement(
        xpath="//input[@placeholder='优惠金额']",
        describe='学员订单管理-课程优惠列表-添加优惠-金额输入框')
    add_order_discount_save = PageElement(
        xpath="//button[@ng-click=\"toEditFinanceDiscountDetail(item,'discountAdd')\"]",
        describe='学员订单管理-课程优惠列表-添加优惠-保存按钮')
    order_unpaid = PageElement(
        xpath="//span[text()='未缴：￥']/span",
        describe="订单详情-支付列表-未缴费用")
    order_paid = PageElement(
        xpath="//span[text()='已缴']/span",
        describe="订单详情-支付列表-未缴费用")
    add_order_pay_btn = PageElement(
        xpath="//button[text()='添加支付项']",
        describe='学员订单管理-课程优惠列表-添加支付项')
    add_order_pay_fee = PageElement(
        xpath="//input[@ng-model='financePayDetailDialog.payFee']",
        describe='学员订单管理-课程优惠列表-添加支付项-支付金额')
    add_order_pay_save_btn = PageElement(
        xpath="//button[@ng-click=\"toEditFinancePayDetail('','payAdd')\"]",
        describe='学员订单管理-支付列表 -添加支付项-保存按钮')
    add_order_other_btn = PageElement(
        xpath="//button[text()='添加其他费用']",
        describe='学员订单管理-其他费用-添加其他费用')
    add_order_other_fee = PageElement(
        xpath="//input[@ng-model='financeOtherFeeDetailDialog.fee']",
        describe='学员订单管理-其他费用-添加其他费用-支付金额输入框')
    add_order_other_save = PageElement(
        xpath="//button[@ng-click=\"toEditFinanceOtherFeeDetail('','otherFeeAdd')\"]",
        describe='学员订单管理-其他费用-添加其他费用-保存')
    pay_stu_order = PageElement(
        xpath="//button[text()='提交支付']",
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
    pay_cancel_button = PageElement(
        xpath="//button[@data-bb-handler='Cancel']",
        describe="取消按钮")

    """
    退费
    """
    order_detail = PageElements(
        xpath="//button[@title='订单详情']",
        describe="学员订单管理-学员的订单详情按钮")
    order_detail_loading = PageElement(
        xpath="//div[@ng-show='$root.somethingLoading' and @class='overlay ng-hide']",
        describe="订单详情已经loading完成")
    order_refund_application = PageElement(
        xpath="//div[@class='modal fade in']",
        describe="等待退费申请模态框出现")
    order_info_refund = PageElement(
        # xpath="//button[@ng-click=\"stuToRefund(item,'refund')\"]",
        xpath="//button[text()='退费']",
        describe="订单详情-退费按钮")
    refund_fee = PageElement(
        xpath="//input[@name='refundFee']",
        describe="退费申请-退费金额")
    refund_name = PageElement(
        xpath="//th[text()='学员姓名']/following-sibling::td[@class='ng-binding']",
        describe="退费申请-学员姓名")
    refund_pre_fee = PageElement(
        xpath="//th[text()='预收金额']/following-sibling::td",
        describe="退费申请-预收金额")
    refund_course_count = PageElement(
        xpath="//th[text()='订购数量']/following-sibling::td[1]/span",
        describe="退费申请-订购总数量")
    refund_course_consume = PageElement(
        xpath="//th[text()='消耗数量']/following-sibling::td[1]/span",
        describe="退费申请-消耗数量")
    save_order_refund = PageElement(
        xpath="//button[@ng-click='stuOrderSaveFinanceRefundApply()']",
        describe="退费申请-确定退费按钮")
    order_confirm_loading = PageElement(
        xpath="//div[@ng-show='stuOrderSaveFinanceRefundApplyLoading' and @class='overlay ng-hide']",
        describe="等待审批事项确认界面")
    approval_matter_setting = PageElement(
        xpath="//select[@title='选择审批流程']",
        describe="审批事项确认-审批流程选择框")
    save_approval_matter = PageElement(
        xpath="//button[@ng-click='saveApprovalMatter(approvalMatter)']",
        describe="审批事项确认按钮")
    # approval_matter_status = PageElement(
    #     xpath="//div[@class='bootbox-body']",
    #     describe="断言审批申请")
    # 学院课程管理
    course_management_Divided = PageElement(
        xpath="//b[text()='已分班学员']",
        describe="学员课程管理-已分班学员页")
    course_school_id = PageElement(
        xpath="//select[@ng-model='stuOrderCourseParam.schoolId']",
        describe="学员课程管理-已分班学员页-归属校区")
    course_params_status = PageElement(
        xpath="//select[@ng-model='stuOrderCourseParamStatus.curr']",
        describe="学员课程管理-已分班学员页-在校状态")
    course_student_name = PageElement(
        xpath="//input[@ng-model='stuOrderCourseParam.studentNameLike']",
        describe="学员课程管理-已分班学员页-学员姓名")
    course_set_teacher_close = PageElement(
        xpath="//button[@ng-click='stuOrderCourseSetParam({})']",
        describe="学员课程管理-已分班学员页-移除教学老师")
    course_management_query = PageElement(
        xpath="//button[@ng-click='loadStuOrderCourseList()']",
        describe="学员课程管理-已分班学员页-查询")
    course_loading = PageElement(
        xpath="//div[@ng-show='stuOrderCourseLoading' and @class='overlay ng-hide']",
        describe="课程查询loading完成")
    class_loading = PageElement(
        xpath="//div[@ng-show='schCourseClassRelationLoading' and @class='overlay ng-hide']",
        describe="等待班级列表loading完成")
    class_name = PageElement(
        xpath="//input[@ng-model='schCourseClassRelationSearch.className']",
        describe="上课班级-班级名称输入框")

    class_choice = PageElement(
        xpath="//button[text()='选定班级']",
        describe="班级列表-选定班级")
    confirm_dialog_loading =PageElement(
        xpath="//div[@class='modal fade in' and @id ='stuCourseDialogClassify']",
        describe="等待分班确认模态框出现")
    save_change_class = PageElement(
        xpath="//button[@ng-click='stuOrderCourseChangClassSave()']",
        describe="保存换班操作")
    change_class_button = PageElement(
        xpath="//button[@ng-click='openClassSelectDialog(item)']",
        describe="学员课程管理-换班按钮")
    course_checkbox = PageElements(
        xpath="//input[@ng-model='item.selected']",
        describe="学课程管理-复选框")
    batch_change_class = PageElement(
        xpath="//button[text()='批量换班']",
        describe="学员课程管理-批量换班")
