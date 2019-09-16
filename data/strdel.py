import json

import pysnooper
import requests

urlBase= "http://csf.91clt.com:8090/fycms/"

class urlInfo():
    def urlBasefun(self):
        return urlBase
    def keepSession(self):
        url = urlBase + "ms/check_login.do"
        payload = {
            "accountName": "liubo",
            "checkCode": "",
            "password": "123456"
        }
        headers = {
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        return response.headers['Set-Cookie']

    def test(self):
        url = "http://csf.91clt.com:8090/fycms/ms/online_status.do"

        headers = {
            'Cookie': "%s" % urlInfo().keepSession(),
        }

        response = requests.request("GET", url, headers=headers)

        return (response.text)

#
#
#
# import requests
#
# url = "http://csf.91clt.com:8090/fycms/ms/sys/sys_manager/delete.do"
#
# payload = "[183]"
# headers = {
#     'Postman-Token': "356098ca-1e16-4e36-a170-7f4ed0715280,92cd3e2e-001f-4b05-9e9a-ae5fe298e6aa",
#     'Host': "csf.91clt.com:8090",
#     'Cookie': "%s"%urlInfo().keepSession()
#     }
#
# response = requests.request("POST", url, data=payload, headers=headers)
#
# print(response.text)

import requests


if __name__ == '__main__':
    urlInfo().test()