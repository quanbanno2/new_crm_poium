from page.crm_finance_page import GfyRefundInfo
from poium import PageWait, PageSelect
from func.find_element_demo import find_object_element
from time import sleep
from func.re_demo import re_demo
from func.db_func import DB


class finance_management:
    @staticmethod
    def refund_info(driver, order_id, department, share_teacher):
        """
        退费信息界面
        @param driver:
        @param order_id:
        @param department:
        @param share_teacher:
        @return:退费状态、退费部门业绩、退费个人业绩
        """
        refund_page = GfyRefundInfo(driver)
        # 等待加载界面
        # PageWait(refund_page.refund_info_loading)
        if refund_page.refund_info_loading:
            # 输入订单号
            refund_page.refund_order_id_input.send_keys(order_id)
            # 查询
            refund_page.query_refund_info_btn.click()
            # PageWait(refund_page.refund_info_loading)
            if refund_page.refund_info_loading:
                # 确认退费
                find_object = find_object_element(driver)
                find_object.find_confirm_refund_button(order_id).click()
                # 等待确认退费对话框出现
                if refund_page.refund_dialog:
                    # 确认退费
                    refund_page.refund_confirm_btn.click()
                    PageWait(refund_page.refund_status)
                    refunds_status = refund_page.refund_status.text
                    sleep(1)
                    refund_page.refund_achievement.click()
                    # 退费业绩loading完成
                    if refund_page.refund_achievement_loading:
                        # 部门退费业绩
                        department_fee = re_demo(find_object.find_object_refund_fee(department).text)
                        # print(department_fee)
                        personal_fee = re_demo(
                            find_object.find_object_refund_fee(DB().get_account_name(share_teacher)).text)
                        refund_result = {'refunds_status': refunds_status, 'department_fee': department_fee,
                                         'personal_fee': personal_fee}
                        return refund_result
