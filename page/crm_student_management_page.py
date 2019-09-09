from poium import Page, PageElement


class GfyCrmStudentCourseManagement(Page):
    """
    学员课程管理
    """
    # 分班
    undivided_student = PageElement(
        link_text="未分班学员",
        describe="学员课程管理-未分班学员")
    student_select_class = PageElement(
        xpath="//button[@ng-click='openClassSelectDialog(item)']",
        describe="学员课程管理-未分班学员-分配班级按钮")
    sch_course_class_search_classname = PageElement(
        xpath="//input[@ng-model='schCourseClassRelationSearch.className']",
        describe="上课班级-班级名称输入框")
    sch_course_class_search_classname_button = PageElement(
        xpath="//button[@ng-click='saveStuOrderCourseUndivided(item)']",
        describe="上课班级-选定班级")
    sch_course_class_search_classname_confirm = PageElement(
        xpath="//button[@data-bb-handler='confirm']",
        describe="上课班级-确认分配")
    student_select_class_status = PageElement(
        xpath="//div[@class='bootbox-body']",
        describe="分配班级结果（成功）")
    student_select_class_ok = PageElement(
        xpath="//button[@data-bb-handler='ok']",
        describe="分班成功确认按钮")


class GfyCrmStudentInClassManagement(Page):
    """
    学员上课管理
    """
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
        describe="新增课程上课记录-保存状态")
    makeup_in_class_status = PageElement(
        xpath="//button[@data-bb-handler='ok']",
        describe="新增课程上课记录-保存状态确认按钮")

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
