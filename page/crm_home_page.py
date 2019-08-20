from poium import Page, PageElement


class GfyHomePage(Page):
    home_index_menu = PageElement(
        xpath="//*[@id=\"sysMenu\"]/li[1]", describe="系统菜单-首页")
    more_home_remind = PageElement(
        css="button.pull-right:nth-child(2)", describe="待办消息信息-更多")
    search_object_name_input = PageElement(
        xpath="/html/body/div[1]/div[1]/div[1]/section[2]/div[1]/form/div[3]/div/input",
        describe="提醒消息-消息对象输入框")
    remind_content_search_input = PageElement(
        xpath="/html/body/div[1]/div[1]/div[1]/section[2]/div[1]/form/div[4]/div/input",
        describe="提醒消息-消息内容输入框")
    remind_center_approve_btn = PageElement(
        css="tr.ng-scope:nth-child(1) > td:nth-child(7) > button:nth-child(1)",
        describe="提醒中心-审批按钮")
    approval_matter_type = PageElement(
        xpath="/html/body/div[1]/div[1]/div[1]/section[2]"
              "/div/div/div/div[1]/section/div[1]/form/div/div/select",
        describe="审批事项-审批类型选择框")
    approval_matter_approval_detail = PageElement(
        xpath="/html/body/div[1]/div[1]/div[1]/section[2]"
              "/div/div/div/div[1]/section/div[2]/div/div"
              "/div[1]/table/tbody/tr[1]/td[9]/a[1]",
        describe="审批事项-审批办理（审批明细）")
    approval_result_input = PageElement(
        css="label.cursorPointer:nth-child(2)",
        describe="审批事项审核-选择审核结果按钮")
    save_approval_result = PageElement(
        xpath="//*[@id=\"model-approvalDetail\"]/div/div/div[3]/button",
        describe="审批事项审核-保存审批结果按钮")
    approval_status = PageElement(
        xpath="/html/body/div[19]/div/div/div[1]/div",
        describe="审批状态")
    approval_status_confirm = PageElement(
        xpath="/html/body/div[19]/div/div/div[2]/button",
        describe="审批状态确定按钮")

