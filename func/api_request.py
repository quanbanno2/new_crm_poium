import requests
from config import CRM_REQ_URL


class crmRequest:
    # def __init__(self, customer_name):
    #     self.customer_name = customer_name
    @staticmethod
    def save_customer_info(customer_name):
        data = '{"sex":"S01","isFather":"F04","attributeValue":"V00","grade":"G07","belongSchoolId":24,' \
               '"intentLevel":"I02","businessType":"B01","custStatus":"S01","custType":"T00",' \
               '"custName":"%s","schoolId":"33","schoolName":"四基初级中学","infoId":1073,' \
               '"infoType":"T01","infoName":"高分云信息单","phoneInfo":"13437829328",' \
               '"operateAccountId":17297}' % customer_name
        request_data = {"requestJson": data}
        requests.post(CRM_REQ_URL + "saveCustInfo.action", data=request_data)
        # rj = r.json()
        # return rj
        # self.ass`ertEqual(rj["flag"], flag)

    @staticmethod
    def allot_order(cust_id):
        data = '{"accountNo":17288,"accountName":"辅导1","departmentId":4,"schoolId":24,"recruitTeacherType":"R03",' \
               '"operateAccountId":17297,"status":"S01","issueDate":"2020/05/09 15:16:09",' \
               '"custIds":"%s"}' % cust_id
        request_data = {"requestJson": data}
        requests.post(CRM_REQ_URL + "allotOrder.action", data=request_data)
