#!user/bin/env python3
# -*- coding: gbk -*-
from functools import wraps
import time



def logit(logfile=r'out.log',userName = 'Null'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            ts = int(time.time())
            timeFlag = time.strftime(" %Y-%m-%d %H:%M:%S", time.localtime(ts))
            # print(func.__name__ + timeFlag)
            # ��logfile����д������
            with open(logfile, 'a') as opened_file:
                # ���ڽ���־��ָ����logfile
                opened_file.write(userName +" has open it"+'\t'+  timeFlag + '\n')
            return func(*args, **kwargs)
        return wrapped_function
    return logging_decorator


# class email_logit(logit):
#     '''
#     һ��logit��ʵ�ְ汾�������ں�������ʱ����email������Ա
#     '''
#     def __init__(self, email='admin@myproject.com', *args, **kwargs):
#         self.email = email
#         super(logit, self).__init__(*args, **kwargs)
#
#     def notify(self):
#         print("has been send email to "+ self.email)
#         pass

# @logit(logfile=r'../test1/reporter/out123.log',userName = 'liubo')
@email_logit
class dte:
    def judgeMsg(self):
        s = abs(123.6)
        print(s)
        return s
    def judgeling(self):
        s = abs(13.6)
        print(s)
        return s
if __name__ == '__main__':
    case = dte()
    func = case.judgeling()
