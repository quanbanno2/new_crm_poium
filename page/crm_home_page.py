from poium import Page, PageElement


class GfyHomePage(Page):
    approval_matter_loading = PageElement(
        xpath="//div[@ng-show='showLoading' and @class='overlay ng-hide']",
        describe="等待审批事项界面加载完成")
    more_remind = PageElement(
        xpath="//button[text()='更多']",
        describe="待办消息信息-更多按钮")
    remind_type = PageElement(
        xpath="//select[@ng-model='homeRemindParams.eventType']",
        describe="提醒消息-提醒类型")
    message_object_input = PageElement(
        xpath="//input[@placeholder='消息对象']",
        describe="提醒消息-消息对象输入框")
    message_content = PageElement(
        xpath="//input[@placeholder='消息内容']",
        describe="提醒消息-消息内容输入框")
    remind_center_approve_btn = PageElement(
        xpath="//button[@ng-click='homeRemindToModule(item)']",
        describe="提醒中心-审批按钮")
    approval_matter_type = PageElement(
        xpath="//select[@ng-change='loadNotApprovalMatterList()']",
        describe="审批事项-审批类型选择框")
    approval_matter_approval_detail = PageElement(
        xpath="//a[@ng-click='getApprovalFlowList(item.approvalId)']",
        describe="审批事项-审批办理（审批明细）")
    approval_result_input = PageElement(
        xpath="//input[@ng-value=\"'R01'\"]",
        describe="审批事项审核-通过")
    save_approval_result = PageElement(
        xpath="//button[@ng-click='saveApprovalResult()']",
        describe="审批事项审核-保存审批结果按钮")
    status = PageElement(
        xpath="//div[@class='bootbox-body']",
        describe="审批状态")
    ok_button = PageElement(
        xpath="//button[@data-bb-handler='ok']",
        describe="审批状态确定按钮")
    approval_matter = PageElement(
        xpath="//div[@class='modal fade']",
        describe="审批事项模态框")
