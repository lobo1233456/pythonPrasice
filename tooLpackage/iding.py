import json

import requests
from dingtalkchatbot.chatbot import DingtalkChatbot


def dingTalkSend():
    '''
    钉钉固定推送

    targetToken = 0609d4c6c66900d43ea42e1d9e6510825424171cae211c0f648a70662b807460
    :param content: 推送信息
    :return:
    '''
    content = 'lalal '
    url = "https://oapi.dingtalk.com/robot/send?access_token=ac2931327c6b5c30f3c9d22e40cf9a05db6c5379170a7c8423205d2eac0ef957"
    headers = {"Content-Type": "application/json ;charset=utf-8 "}
    msg = {
        # "msgtype": "text",
        # "text": {"content": content},
        "msgtype": "image",
        "image": {
            "media_id": r"C:\Users\liubo\Pictures\Camera Roll\1556515438186.jpg"
        },
        "at": {
            "atMobiles": [
                "15198292675"],
            "isAtAll": False
        }
    }
    post_data = json.dumps(msg)  # 将Python对象编码成 JSON 字符串
    status = requests.post(url, data=post_data, headers=headers)

    return status.json()

class Student(object):
    def __init__(self, name, age):  # 构造实例时将参数值传递给当前那个实例的成员
        self.name = name
        self.age = age

if __name__ == '__main__':
    url = "https://oapi.dingtalk.com/robot/send?access_token=ac2931327c6b5c30f3c9d22e40cf9a05db6c5379170a7c8423205d2eac0ef957"
    Ding = DingtalkChatbot(url)
    Ding.send_image(r"https://cn.bing.com/th?id=OIP.4uO2P16ozlUXwNi0SkO8egHaE8&pid=Api&rs=1")
    msg = {
        "msgtype": "text",
        "text": {"content": "hello"},
    }
    Ding.post(msg)
