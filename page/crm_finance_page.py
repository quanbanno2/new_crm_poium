from poium import Page, PageElement


class GfyRefundInfo(Page):
    """
    财务管理-退费信息管理
    """
    refund_order_id_input = PageElement(
        xpath="//input[@name='orderId']",
        describe="退费信息-订单号输入框")
    query_refund_info_btn = PageElement(
        xpath="//button[@ng-click='queryRefundFn()']",
        describe="退费信息-查询按钮")
    refund_check_confirm_btn = PageElement(
        xpath="//button[@ng-click='financeRefundCheckConfirm(item.refundApplyId)']",
        describe="退费信息-确认退费按钮")
    refund_confirm_btn = PageElement(
        xpath="//button[@ng-click='financeRefundConfirm()']",
        describe="退费信息-确认退费按钮")
    refund_status = PageElement(
        xpath="//span[@ng-if='x.dictKey == item.refundStatus']",
        describe="退费信息-退费状态")
