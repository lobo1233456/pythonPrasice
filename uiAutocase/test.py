 # -*- coding:utf-8 -*-
import time

import xlrd

from selenium import webdriver
# driver = webdriver.Chrome()
# url = 'http://kk7-vip.kmstarts.com/admin/index/index.html#/admin/'
# driver.get("url")
# driver.implicitly_wait(10)
# lem = driver.find_element_by_xpath("/html/body/div/p").text
# assert "抱歉，您访问的页面不存在。。" in lem

class kmstartsUrl():
    def __init__(self):
        self.testfile = "testReporter" + self.time()
    def read(self):
        '''
        通过excel读取数据，构建地址url
        :return: 返回所有地址
        '''
        urList = []
        inpath = r"../data/urlId.xlsx"
        data = xlrd.open_workbook(inpath, encoding_override='utf-8')
        table = data.sheets()[0]  # 选定表
        nrows = table.nrows  # 获取行号
        for i in range(0, nrows):  # 第0行为表头
             alldata = table.row_values(i)  # 循环输出excel表中每一行，即所有数据
             result = alldata[0]  # 取出表中第二列数据
             if result is not None:
                 urList.append('http://m.kmstarts.com/detail/'+str(int(result))+'.html')
        return urList


    # def judgeMsg(self.url):
    #     driver = webdriver.Chrome()
    #     driver.maximize_window()
    #     try:
    #         driver.get(url)
    #         driver.implicitly_wait(10)
    #         lem = driver.find_element_by_id("page-topnav").text
    #         assert "首页" in lem
    #         time.sleep(2)
    #         driver.close()
    #     # except Exception:
    #     #     msg = url + " is Wrong "
    #     #     self.__edit(msg)
    #     # else:
    #     #     msg = url + " is Correct "
    #     #     self.__edit(msg)
    #     finally:
    #         driver.close()
    def time(self):
        ts = int(time.time())
        timeFlag = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(ts))
        return timeFlag

    def edit(self, msg):
        print(msg + self.time())
        fh = open(r"../reporter/%s"%self.testfile,encoding='utf-8',mode='a')
        fh.write(msg +  self.time() + " \n")
        fh.close()
class lalla():

    def laa(self):
        pass

if __name__ == '__main__':

    import os
    import os.path
    from shutil import copy
    import pysnooper

    import os

    os.environ["TF_CPP_MIN_LOG_LEVEL"] = '1'
    # 默认的显示等级，显示所有信息
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = '2'