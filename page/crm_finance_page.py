from poium import Page, PageElement


class GfyRefundInfo(Page):
    """
    财务管理-退费信息管理
    """
    refund_order_id_input = PageElement(
        css="div.col-sm-6:nth-child(3) > div:nth-child(1) > input:nth-child(3)",
        describe="退费信息-订单号输入框")
    query_refund_info_btn = PageElement(
        css="button.ng-scope:nth-child(1)",
        describe="退费信息-查询按钮")
    refund_check_confirm_btn = PageElement(
        css="button.ng-scope:nth-child(4)",
        describe="退费信息-确认退费按钮")
    refund_confirm_btn = PageElement(
        xpath="//*[@id=\"refundAchievementConfirmDialog\"]/div/div/div[3]/button[2]",
        describe="退费信息-确认退费按钮")
    refund_status = PageElement(
        xpath="/html/body/div[1]/div[1]/div[1]/section[2]"
              "/div/div/div/div[1]/table/tbody/tr[1]/td[7]/span",
        describe="退费信息-退费状态")

