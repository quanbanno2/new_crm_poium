from poium import Page, PageElement, PageElements


class GfyRefundInfo(Page):
    """
    财务管理-退费信息管理
    """
    refund_info_loading = PageElement(
        xpath="//div[@ng-show='showLoading' and @class='overlay ng-hide']",
        describe="退费信息等待loading完成")
    refund_order_id_input = PageElement(
        xpath="//input[@name='orderId']",
        describe="退费信息-订单号输入框")
    query_refund_info_btn = PageElement(
        xpath="//button[@ng-click='queryRefundFn()']",
        describe="退费信息-查询按钮")
    # refund_check_confirm_btn = PageElement(
    #     xpath="//button[@ng-click='financeRefundCheckConfirm(item.refundApplyId)']",
    #     describe="退费信息-确认退费按钮")
    refund_confirm_btn = PageElement(
        xpath="//button[@ng-click='financeRefundConfirm()']",
        describe="退费信息-确认退费按钮")
    refund_dialog = PageElement(
        xpath="//div[@class='modal fade in']",
        describe="对话框出现")
    refund_status = PageElement(
        xpath="//div[@class='bootbox-body']/div/strong",
        describe="退费信息-退费状态")
    refund_achievement = PageElement(
        xpath="//button[text()='查看责任']",
        describe="退费信息-查看责任")
    refund_achievement_loading = PageElement(
        xpath="//div[@ng-show='refundAchievementLoading' and @class='overlay ng-hide']",
        describe="退费业绩loading完成")
    refund_achievement_edit = PageElement(
        xpath="//button[@ng-click=\"refundInfoAchievementEdit('edit',item)\"]",
        describe="退费责任编辑")
