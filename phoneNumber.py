

import requests



import string
# def phone_num():
#     import random


        # 随机生成手机号码

def phone_num():
    l = []
    prelist = ["2a33""130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
               "153", "155", "156", "157", "158", "159", "186", "187", "188","166"]
    for i in prelist:
        l.append(i+"64743157")

    return l


def checkNum(num):
    url = "https://www.kmway.com/jm/msgsubmit"

    querystring = {"jsonpCallback":"jsonpCallback","ProjectID":"837192","URLTitle":"%E5%90%8D%E4%BA%BA%E6%95%99%E8%82%B2%E5%8A%A0%E7%9B%9F%E8%B4%B9_%E5%90%8D%E4%BA%BA%E6%95%99%E8%82%B2%E5%8A%A0%E7%9B%9F%E5%BA%97_%E5%BF%AB%E9%A9%AC%E5%8A%A0%E7%9B%9F%E7%BD%91","Tel":"%s"%num,"URL":"https%3A%2F%2Fwww.kmway.com%2Fjy%2F837192.shtml","_":"1570677266620"}

    headers = {
        'User-Agent': "PostmanRuntime/7.17.1",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "a122c119-cb55-4a80-829b-3d340c5cb07f,d4bf9d1f-d6ca-41bb-94cb-fd4fce16c723",
        'Host': "www.kmway.com",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "0",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    response = requests.request("POST", url, headers=headers, params=querystring)

    return (response.text)

if __name__ == '__main__':
    phone_num()


    for i in phone_num():
        print(i,checkNum(i))
