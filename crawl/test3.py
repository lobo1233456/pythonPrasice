# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 14:01:28 2018
@author: ESionJL数据猫
question:1.当前url若爬取到的pagelinks为[]，则将其移除visited列表。
         2.spiderpage()函数中，当前url爬取到的网页为UNknown，会报错，如何规避，并将此url移除。
         3.返回title为空
         4.网站不可加载
         5.过期网站，垃圾网站
"""
import json
import re
import time
import requests
from bs4 import BeautifulSoup
from urllib import request
from urllib import error

kv = {
    'HOST': "www.jztest.com",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
}

# 此测试首页是否可以链接
def url_get(num_retries=5):
    #    url = input("请输入要爬取的首页url:")
    url = "http://www.jztest.com/xzksjlist"
    #    url = "http://"
    try:
        # 做一个user-agent模拟浏览器发送请求,也可以加入其它字段
        kv = {
            'HOST':"www.jztest.com",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        enp  =requests.get(url, headers=kv)
        # print(enp.status_code)
        return url
    except error.URLError or error.HTTPError as e:
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                url_get(num_retries - 1)
        print("url无法连接")


# 此函数用于提取各链接网站下的所有链接
def spiderpage(url):
    try:
        kv = {
            'HOST': "www.jztest.com",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        r = requests.get(url, headers=kv)
        # print(r.status_code)
        r.encoding = r.apparent_encoding
        pagetext = r.text
        # 正则表达式表示要爬取的是<a href="和"中的内容,"或'都可以,即当前页面下所有的链接url,返回列表
        pagelinks = re.findall(r'(?<=<a href=\").*?(?=\")|(?<=href=\').*?(?=\')', pagetext)
        # print(pagelinks)
        pagelinks = [x for x in pagelinks if "jztest" in x]
        return pagelinks
    except:
        pagelinks = ['http://']
        print("这个网站有点东西")
        return pagelinks


# 此函数用来检测链接是否为外网链接或者不合格链接
# 外网链接不应该被发送至dingding，只发送死链接
# 判断依据为title是404页面
def getTitle(url):
    # 检验是否为本站链接，防止死循环爬取，如链接跳出本站则不进行操作
    headers = {
               'HOST': "www.jztest.com",
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
               }
    print(url)
    req = request.Request(url, headers=headers)
    html = None
    try:
        response = request.urlopen(req)
        html = response.read().decode('utf-8')
        soup = BeautifulSoup(html, "html.parser")
        if soup.body is not None:
            url_list = soup.head.title
            title = url_list.string
            # print(title)
            if title != None:
                return title
            else:
                return "这网站没有灵性"
        else:
            title = "不可加载"
            return title
        #    except error.URLError or error.HTTPError or error.UnicodeDecodeError:
    except:
        enp = requests.get(url, headers=kv)
        if enp.status_code != 200 and 'jztest' in url:
            dingTalkSend(url)
            file = open('FurlsWR%s.txt' % time.strftime("%Y.%m.%d"), 'a', encoding='utf8')
            file.write(f'{url}\n')
            print("这网站没有灵性")
            return "不可加载"

    # 正则删选函数


def url_filtrate(pagelinks):
    same_target_url = []

    try:
        for murl in pagelinks:
            murl = re.sub(r'\s+', '', murl)

            if re.findall("^java", murl) or re.findall("^jse", murl) or re.findall("^ALL", murl) or re.findall("pdf$",
                                                                                                               murl) or re.findall(
                    "^login", murl) or re.findall("css$", murl) or re.findall("@", murl):
                pagelinks.remove(murl)

            elif re.findall("^http", murl) and re.findall("newchinalife", murl) is None:
                pagelinks.remove(murl)

            elif re.findall("^http", murl):
                murl = str(murl)
                same_target_url.append(murl)

            elif re.findall("^java", murl) or re.findall("^jse", murl) or re.findall("^ALL", murl) or re.findall("pdf$",
                                                                                                                 murl) or re.findall(
                    "^login", murl):
                pagelinks.remove(murl)

            elif re.findall("gsp$", murl) or re.findall("shtml$", murl) or re.findall("[0-9]*$", murl):
                murl = "http://www.jztest.com" + str(murl)
                same_target_url.append(murl)

            elif re.findall("^/", murl):
                murl = "http://www.jztest.com" + str(murl)
                same_target_url.append(murl)

            else:
                pass
    except ValueError as e:
        pass
    # 去除重复url
    unrepect_url = []
    for l in same_target_url:
        if l not in unrepect_url:
            unrepect_url.append(l)

    # print(unrepect_url)
    return unrepect_url


class linkQuence:
    def __init__(self):
        # 已访问的url集合
        self.visited = []
        # 待访问的url集合
        self.unvisited = []

    # 获取访问过的url队列
    def getvisitedurl(self):
        return self.visited

    # 获取未访问的url队列
    def getunvisitedurl(self):
        return self.unvisited

    # 添加url到访问过得队列中
    def addvisitedurl(self, url):
        return self.visited.append(url)

    # 添加url到访问过得队列中
    def addvisitedurlSource(self, url):
        return self.visited.append(url)

    # 移除访问过得url
    def removevisitedurl(self, url):
        return self.visited.remove(url)

    # 从未访问队列中取一个url
    def unvisitedurldequence(self):
        try:
            return self.unvisited.pop()
        except:
            return None

    # 添加url到未访问的队列中
    def addunvisitedurl(self, url):
        if url != "" and url not in self.visited and url not in self.unvisited:
            return self.unvisited.insert(0, url)

    # 获得已访问的url数目
    def getvisitedurlount(self):
        return len(self.visited)

    # 获得未访问的url数目
    def getunvistedurlcount(self):
        return len(self.unvisited)

    # 判断未访问的url队列是否为空
    def unvisitedurlsempty(self):
        return len(self.unvisited) == 0


class Spider():
    def __init__(self, url):
        self.linkQuence = linkQuence()  # 将队列引入本类
        self.linkQuence.addunvisitedurl(url)  # 传入待爬取的url,即爬虫入口
        self.local = time.strftime("%Y.%m.%d")
    # 真正的爬取链接函数
    def crawler(self, urlcount):
        # 子页面过多,为测试方便加入循环控制子页面数量
        # visitedurl可以作为出现死链的地址
        x = 1
        while self.linkQuence.unvisited or x == urlcount:
            # 若子页面不是很多,可以直接使用队列中的未访问列表非空作为循环条件
            # while not self.linkQuence.unvisitedurlsempty():
            if x > 1:
                print(f"第{x - 1}个url,开始爬")
            visitedurl = self.linkQuence.unvisitedurldequence()  # 从未访问列表中pop出一个url
            if visitedurl is None or visitedurl == '':
                continue
            title = getTitle(visitedurl)
            url_m = visitedurl.replace(r'//www', r'//m')
            title_m = getTitle(url_m)
            if title == "404页面":
                dingTalkSend(visitedurl)
                file = open('FurlsWR%s.txt' % self.local, 'a', encoding='utf8')
                file.write(f'{visitedurl}\n')
                file.close()
            if title_m == "404页面":
                dingTalkSend(url_m)
                file = open('FurlsWR%s.txt' % self.local, 'a', encoding='utf8')
                file.write(f'{url_m}\n')
                file.close()
            # if re.findall("家居室内装修设计_装修设计公司_星装网", title):  # 如果跳出本站则pass
            initial_links = spiderpage(visitedurl)  # 爬出该url页面中所有的链接
            right_links = url_filtrate(initial_links)  # 筛选出合格的链接
            if not right_links:
                pass
            else:
                self.linkQuence.addvisitedurl(visitedurl)  # 将该url放到访问过的url队列中
                for link in right_links:  # 将筛选出的链接放到未访问队列中
                    self.linkQuence.addunvisitedurl(link)
                x += 1
            # else:
            #     pass
        print(f"爬完了")
        return self.linkQuence.visited

def dingTalkSend(content):
    '''
    钉钉固定推送

    targetToken = 0609d4c6c66900d43ea42e1d9e6510825424171cae211c0f648a70662b807460
    :param content: 推送信息
    :return:
    '''
    url = "https://oapi.dingtalk.com/robot/send?access_token=824f9ab064def7456dcc5029b724bf16d3baeddb34f69bad93e49c0b0def05ab"
    headers = {"Content-Type": "application/json ;charset=utf-8 "}
    # content = "测试"
    msg = {
        "msgtype": "text",
        "text": {"content": content}
    }
    post_data = json.dumps(msg)  # 将Python对象编码成 JSON 字符串
    status = requests.post(url, data=post_data, headers=headers)
    msg = {
        "msgtype": "text",
        "text": {"content": content},
        "at": {
            "atMobiles": [
                "139xxxx0217",
                "189xxxx8325"],
            "isAtAll": False
        }
    }
    return status.json()
# 写文件函数
def writetofile(urllist):
    # 写入网站并计数
    # x = 1
    # for url in urllist:
    #     # Furls.txt用于保存链接
    #     file = open('Furls.txt', 'a', encoding='utf8')
    #     file.write(f'{url}\n')
    #     x += 1
    #     file.close()
    print(f'写入已完成,总计{len(urllist)*2 - 1}个网页的子链接')


# 主循环
if __name__ == '__main__':
    # url = url_get()
    # spider = Spider(url)
    # # 传入要爬取的子链接数量
    # urllist = spider.crawler(5000)
    # writetofile(urllist)

    initial_links = spiderpage("https://www.kmway.com")
    print(initial_links)