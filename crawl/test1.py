#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
import urllib.request

import requests
from bs4 import BeautifulSoup as Bs4

head_url = "http://cms.jztest.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
}
def get_first_url():
    headers = ("User-Agent",
               "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(head_url).read()
    file = file.decode('utf-8')
    pattern = '(https?://[^\s)";]+(\.(\w|/)*))'
    link = re.compile(pattern).findall(file)
    # 去重
    # link = list(set(link))
    return link


def get_next_url(urllist):
    url_list = []
    for url in urllist:
        response = requests.get(url,headers=headers)
        soup = Bs4(response.text,"lxml")
        urls = soup.find_all("a")
        if urls:
            for url2 in urls:
                url2_1 = url2.get("href")
                if url2_1:
                    if url2_1[0] == "/":
                        url2_1 = head_url + url2_1
                        url_list.append(url2_1)
                        if url2_1[0:24] == "http://cms.jztest.com":
                            url2_1 = url2_1
                            url_list.append(url2_1)
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
        else:
            pass
    url_list2 = set(url_list)
    for url_ in url_list2:
        res = requests.get(url_)
        if res.status_code ==200:
            print(url_)
    print(len(url_list2))
    get_next_url(url_list2)


if __name__ == "__main__":
    urllist = get_first_url()
    get_next_url(urllist)