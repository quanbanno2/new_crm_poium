from poium import Page, PageElement


class GfyHomePage(Page):
    more_home_remind = PageElement(
        xpath="//button[@ng-click=\"$parent.switchModule('homeRemind')\"]",
        describe="待办消息信息-更多按钮")
    search_object_name_input = PageElement(
        xpath="//input[@placeholder='消息对象']",
        describe="提醒消息-消息对象输入框")
    remind_content_search_input = PageElement(
        xpath="//input[@placeholder='消息内容']",
        describe="提醒消息-消息内容输入框")
    remind_center_approve_btn = PageElement(
        css="//button[@ng-click='homeRemindToModule(item)']",
        describe="提醒中心-审批按钮")
    approval_matter_type = PageElement(
        xpath="//select[@ng-change='loadNotApprovalMatterList()']",
        describe="审批事项-审批类型选择框")
    approval_matter_approval_detail = PageElement(
        xpath="//a[@ng-click='getApprovalFlowList(item.approvalId)']",
        describe="审批事项-审批办理（审批明细）")
    approval_result_input = PageElement(
        xpath="//input[@ng-value=\"'R01'\"]",
        describe="审批事项审核-选择审核结果为通过的按钮")
    save_approval_result = PageElement(
        xpath="//button[@ng-click='saveApprovalResult()']",
        describe="审批事项审核-保存审批结果按钮")
    status = PageElement(
        xpath="//div[@class='bootbox-body']",
        describe="审批状态")
    ok_button = PageElement(
        xpath="//button[@data-bb-handler='ok']",
        describe="审批状态确定按钮")
