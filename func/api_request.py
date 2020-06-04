import requests
from config import CRM_REQ_URL


class crmRequest:
    @staticmethod
    def save_customer_info(customer_name):
        """
        输入客户名称生成客户信息
        @param customer_name:
        @return:
        """
        data = '{"sex":"S01","isFather":"F04","attributeValue":"V00","grade":"G07","belongSchoolId":24,' \
               '"intentLevel":"I02","businessType":"B01","custStatus":"S01","custType":"T00",' \
               '"custName":"%s","schoolId":"33","schoolName":"四基初级中学","infoId":1073,' \
               '"infoType":"T01","infoName":"高分云信息单","phoneInfo":"13800138000",' \
               '"operateAccountId":17297}' % customer_name
        request_data = {"requestJson": data}
        requests.post(CRM_REQ_URL + "saveCustInfo.action", data=request_data)

    @staticmethod
    def allot_order(customer_id):
        """
        将客户id分单给高分云顾问2
        @param customer_id:
        @return:
        """
        data = '{"accountNo":27034,"accountName":"高分云顾问2","departmentId":4,"schoolId":24,"recruitTeacherType":"R03",' \
               '"operateAccountId":17297,"status":"S01","issueDate":"2020/05/09 15:16:09",' \
               '"custIds":"%s"}' % customer_id
        request_data = {"requestJson": data}
        requests.post(CRM_REQ_URL + "allotOrder.action", data=request_data)
