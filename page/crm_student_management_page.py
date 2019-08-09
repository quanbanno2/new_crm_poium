from poium import Page, PageElement


class GfyCrmStudentCourseManagement(Page):
    """
    学员课程管理
    """
    # 分班
    student_management = PageElement(
        xpath="//*[@id=\"sysMenu\"]/li[3]/a",
        describe="菜单栏-学员管理")
    student_course_management = PageElement(
        xpath="//*[@id=\"sysMenu\"]/li[3]/ul/li[4]",
        describe="学员课程管理")
    undivided_student = PageElement(
        css=".nav-tabs > li:nth-child(2)",
        describe="学员课程管理-未分班学员")
    student_name = PageElement(
        xpath="/html/body/div[1]/div[1]/div[1]/section[2]/div/div"
              "/div/div[2]/form/div[1]/div[5]/div/input",
        describe="学员名称筛选输入框")
    student_undivided_query = PageElement(
        xpath="/html/body/div[1]/div[1]/div[1]"
              "/section[2]/div/div/div/div[2]/form/div[2]/div/button[1]",
        describe="未分班查询")
    student_select_class = PageElement(
        xpath="/html/body/div[1]/div[1]/div[1]/section[2]/div/div/div/div[2]"
              "/div/div/div/div[1]/table/tbody/tr[1]/td[14]/button",
        describe="学员课程管理-未分班学员-分配班级")
    sch_course_class_search_classname = PageElement(
        xpath="//*[@id=\"stuCourseSelectClassDialog\"]/div/div/div[2]/div[1]/div[2]/div/input",
        describe="上课班级-班级名称输入框")
    sch_course_class_search_classname_button = PageElement(
        xpath="//*[@id=\"stuCourseSelectClassDialog\"]/div/div/div[2]/div[2]"
              "/div/div/div[1]/table/tbody/tr[1]/td[5]/button",
        describe="上课班级-选定班级")
    sch_course_class_search_classname_confirm = PageElement(
        css="div.modal-footer:nth-child(2) > button:nth-child(2)",
        describe="上课班级-确认分配")
    student_select_class_status = PageElement(
        xpath="/html/body/div[19]/div/div/div[1]/div",
        describe="分配班级结果（成功）")


class GfyCrmStudentInClassManagement(Page):
    """
    学员上课管理
    """
    # 新增上课记录
    student_class_management = PageElement(
        xpath="//*[@id=\"sysMenu\"]"
              "/li[3]/ul/li[4]/a",
        describe="学员上课管理")
    add_in_class_record = PageElement(
        xpath="/html/body/div[1]/div[1]/div[1]/section[2]"
              "/div/div/div/div[1]/form/div[2]/div[2]/button[1]",
        describe="学员上课-新增")
    makeup_school_list = PageElement(
        xpath="//*[@id=\"stuClassDialog\"]"
              "/div/div/div[2]/form/div[1]/select",
        describe="新增课程上课记录-归属校区")
    makeup_class_name = PageElement(
        xpath="//*[@id=\"stuClassDialog\"]"
              "/div/div/div[2]/form/div[3]/input",
        describe="新增课程上课记录-课程班级")
    select_a_classes_search = PageElement(
        xpath="//*[@id=\"stuClassCourseDialog\"]"
              "/div/div/div[2]/div/div/div[1]/div/input",
        describe="新增课程上课记录-课程班级-关键字搜索输入框")
    select_a_classes = PageElement(
        xpath="//*[@id=\"stuClassCourseDialog\"]"
              "/div/div/div[2]/div/div/div[1]/table/tbody/tr/td[4]/a",
        describe="新增课程上课记录-课程班级-选中班级")
    makeup_time_cycle = PageElement(
        css="select.ng-valid-required",
        describe="新增课程上课记录-时间周期")
    makeup_in_class_date = PageElement(
        css="div.input-group:nth-child(6) > input:nth-child(2)",
        describe="新增课程上课记录-开始时间")
    makeup_in_class_date_today = PageElement(
        xpath="//*[@id=\"jedatebox\"]/div[4]/div[2]/span[2]",
        describe="新增课程上课记录-开始时间-今天")
    makeup_save = PageElement(
        xpath="//*[@id=\"stuClassDialog\"]"
              "/div/div/div[3]/button[2]",
        describe="新增课程上课记录-保存")
    makeup_status = PageElement(
        xpath="/html/body/div[19]/div/div/div[1]/div",
        describe="新增课程上课记录-保存状态")
    makeup_in_class_status = PageElement(
        xpath="/html/body/div[19]/div/div/div[2]/button",
        describe="新增课程上课记录-保存状态确认")

    # 点名
    teacher_class_list = PageElement(
        xpath="/html/body/div[1]/div[1]/div[1]/section[2]"
              "/div/div/div/div[1]/form/div[1]/div[4]/div/select",
        describe="学员上课管理-老师班级")
    query_in_class_record = PageElement(
        css="button.margin-r-5:nth-child(2)",
        describe="学员上课管理-查询")
    in_class_school_list = PageElement(
        xpath="/html/body/div[1]/div[1]/div[1]/section[2]"
              "/div/div/div/div[1]/form/div[1]/div[1]/div/select",
        describe="学员上课管理-归属校区")
    in_class_status_list = PageElement(
        xpath="/html/body/div[1]/div[1]/div[1]/section[2]"
              "/div/div/div/div[1]/form/div[1]/div[2]/div/select",
        describe="学员上课管理-状态")
    in_class_sign = PageElement(
        xpath="/html/body/div[1]/div[1]/div[1]/section[2]"
              "/div/div/div/div[1]/div/div/div/div[1]/table"
              "/tbody/tr[1]/td[8]/span[1]/button[1]",
        describe="学员上课管理-点名")
    in_class_sign_save = PageElement(
        xpath="//*[@id=\"stuClassSign\"]/div/div/div[3]/button[3]",
        describe="学员上课点名-保存点名")
    in_class_sign_confirm = PageElement(
        xpath="/html/body/div[20]/div/div/div[2]/button[2]",
        describe="学员上课点名-确认点名")
    in_class_sign_status = PageElement(
        xpath="/html/body/div[19]/div/div/div[1]/div",
        describe="学员上课点名-点名状态")
