# -*- coding:utf-8 -*-
# __author__ == 'chenmingle'
import websocket
class msg(object):

    # from = 1122698273883017218  #访客id
    to = id#客服id
    content= 'test'
    direction= 1
    # session=gfyStatusInfo.session  #对话session，由ws获取
    url_no= ''
    # clientMsgId= timestamp #时间戳
    # appId=  #对应的appID

try:
    import thread
except ImportError:
    import _thread as thread
import time

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")



def on_open(ws):
    def run(*args):
        message = '/im/visitor?uid=1123042841212432386&uuid=69de69253591bbc7e0ea4aef90201895&linkType=1'
        # ws.send(message)
        for i in range(3):
            time.sleep(1)
            ws.send(message)
        time.sleep(1)
        ws.close()
        print("thread terminating...")
        thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    # webUrl = 'ws//47.93.186.159:10090' + '/im/visitor' + '?uid=' + '112269827388301721' + '&uuid=' + '97462a693ca0f76e71f9c3bffadc9427'+
    ws = websocket.WebSocketApp("ws://csf.91clt.com:10086/socket.io/?uid=1123042841212432386&uuid=84d02cf1bd79b6ad98eec22689ac8adf&linkType=1&EIO=3&transport=websocket",
                             on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()