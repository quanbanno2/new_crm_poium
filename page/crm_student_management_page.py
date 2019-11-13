from poium import Page, PageElement,PageElements


class GfyCrmStudentCourseManagement(Page):
    """
    学员课程管理
    """
    # 分班
    undivided_student = PageElement(
        link_text="未分班学员",
        describe="学员课程管理-未分班学员")
    student_select_class = PageElements(
        xpath="//button[text()='分配班级']",
        describe="学员课程管理-未分班学员-分配班级按钮")
    sch_course_class_search_class_name = PageElement(
        xpath="//input[@ng-model='schCourseClassRelationSearch.className']",
        describe="上课班级-班级名称输入框")
    sch_course_class_search_class_name_button = PageElements(
        xpath="//button[text()='选定班级']",
        describe="上课班级-选定班级")
    sch_order_course_class_save = PageElement(
        xpath="//button[@ng-click='stuOrderCourseChangClassSave()']",
        describe="上课班级-分班确认")
    # sch_course_class_search_class_name_confirm = PageElement(
    #     xpath="//button[@data-bb-handler='confirm']",
    #     describe="上课班级-确认分配")
    student_select_class_status = PageElement(
        xpath="//h3[text()='保存成功']",
        describe="学员分配班级结果（成功）")
    student_select_class_ok = PageElement(
        xpath="//button[@data-bb-handler='ok']",
        describe="分班成功确认按钮")


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
    del_in_class_record = PageElement(
        xpath="//button[text()='删除']",
        describe="学员上课管理-删除上课记录按钮")

    # 点名
    teacher_class_list = PageElement(
        xpath="//select[@ng-model='stuCourseInClassRecordParam.classId']",
        describe="学员上课管理-老师班级选择框")
    query_in_class_record = PageElement(
        xpath="//button[@ng-click='loadStuCourseInClassRecordList(1,initPageInfo.pageSize)']",
        describe="学员上课管理-查询按钮")
    in_class_school_list = PageElement(
        xpath="//select[@ng-model='stuCourseInClassRecordParam.schoolId']",
        describe="学员上课管理-归属校区下拉框")
    in_class_status_list = PageElement(
        xpath="//select[@ng-model='stuCourseInClassRecordParam.status']",
        describe="学员上课管理-状态下拉框")
    in_class_sign = PageElement(
        xpath="//button[@ng-click=\"toEditStuCourseInClassRecord('sign',item)\"]",
        describe="学员上课管理-点名按钮")
    in_class_sign_save = PageElement(
        xpath="//button[@ng-click='stuClassSaveStuCourseDetail()']",
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
    in_class_record = PageElement(
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
    make_up_student_name = PageElement(
        xpath="//input[@name='studentName']",
        describe="补课管理-学员姓名输入框")
    query_makeup_student = PageElement(
        xpath="//button[@ng-click='loadStuLeaveDetail(1,pageInfo.pageSize)']",
        describe="补课管理-查询按钮")
    plan_student_makeup = PageElement(
        xpath="//button[@ng-click='stuToMakeup(item)']",
        describe="补课管理-安排补课")
    makeup_select_class = PageElement(
        xpath="//button[@ng-click='stuMakeupSelectClass(item)']",
        describe="补课管理-选择补课班级")
