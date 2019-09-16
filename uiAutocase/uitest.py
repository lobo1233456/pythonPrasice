# import time
#
# import requests
#
# url = "http://csf.91clt.com:8090/fycms/ms/check_login.do"
#
# payload = "{\r\n  \"accountName\": \"liubo\",\r\n  \"checkCode\": \"\",\r\n  \"password\": \"123456\"\r\n}"
# headers = {
#
# }
#
# response = requests.request("POST", url, data=payload, headers=headers)
#
# print(response.text)
#
# url = "http://csf.91clt.com:8090/fycms/ms/sys/sys_manager/save.do"
#
# payload = "{\r\n  \"createBy\": 0,\r\n  \"createDate\": \"2019-08-01T01:25:03.800Z\",\r\n  \"createDateStr\": \"string\",\r\n  \"del\": 0,\r\n  \"managerName\": \"test15646623847\",\r\n  \"managerNickname\": \"string\",\r\n  \"managerPassword\": \"string\",\r\n  \"managerSalt\": \"string\",\r\n  \"roleIdList\": [\r\n    0\r\n  ],\r\n  \"updateBy\": 0,\r\n  \"updateDate\": \"2019-08-01T01:25:03.800Z\",\r\n  \"updateDateStr\": \"string\"\r\n}"
# headers = {
#     'Content-Type': "application/json,text/plain",
#     'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36",
#     'Accept': "*/*",
#     'Cache-Control': "no-cache",
#     'Postman-Token': "587e55da-a129-4d45-bde9-2b2e5bcb519e,9eefcdb3-8a4d-40a3-b142-0548ad2dfe21",
#     'Host': "csf.91clt.com:8090",
#     'Cookie': "JSESSIONID=ee758395-40bc-4ef1-a9c3-fe49684a5f2a",
#     'Accept-Encoding': "gzip, deflate",
#     'Content-Length': "363",
#     'Connection': "keep-alive",
#     'cache-control': "no-cache"
# }
# time.sleep(2)
# response = requests.request("POST", url, data=payload, headers=headers)
#
# print(response.text)
x = [1,2,3,4,5]
print(6 in x)
y = list(filter(lambda x: x!=2, x))
print(y)