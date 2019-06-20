#!user/bin/env python3
# -*- coding: UTF-8 -*-

import requests

url = "http://60.205.200.186/api/auth/add"
headers = {"addUser": "zhuhao","ProjectName": "Coco都可奶茶茶饮","ProjectID":"ProjectID:","CatalogName": "项目库>餐饮>奶茶饮品",
"CatalogInnerCode": "001336000001000001","Tel": "13764743158",}
# querystring = {"ProjectID":"640109","Name":"testLiubo","Tel":"13764743102"}
# '''
# [{id: 236, projectID: 792408, projectName: "卡乐巴巴", catalogInnerCode: "001336000001000001",…},…]
# debugInfo: null
# desc: "成功"
# status: 1000
# '''
payload = ""
# headers = {
#     }
response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)