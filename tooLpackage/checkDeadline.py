import requests
import re
import sys

# 获取网址内容
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'}


url = 'http://www.kmstarts.com/'
# url  = input('请输入网址>>>')
r = requests.get(url)
data = r.text
print(data)
link_list = re.findall(r"\"(http\:\/\/[a-zA-Z0-9\.\/]+)\"", data)
link_list = list(set(link_list))

# # 利用正则查找所有连接
# link_list = re.findall(r"href\=\"(http\:\/\/[a-zA-Z0-9\.\/]+)\"", data)
link_list = ['http://www.kmstarts.com/detail/953.html','http://www.kmstarts.com/detail/95233.html','http://www.kmstarts.com/detail/9533.html']
for url in link_list:
    url = [url]
    length = len(url)
    url_result_success = []
    url_result_failed = []
    for i in range(0, length):
        try:
            response = requests.get(url[i].strip(), verify=False, allow_redirects=True, timeout=5)
            if response.status_code != 200:
                raise requests.RequestException(u"Status code error: {}".format(response.status_code))  # 引出请求时出现歧义异常
        except requests.RequestException as e:
            url_result_failed.append(url[i])
            result_failed_len = len(url_result_failed)
            for i in range(0, result_failed_len):
                print('URL-->  %s' % url_result_failed[i].strip() + ' -->死链接')
            continue
        url_result_success.append(url[i])
    result_success_len = len(url_result_success)
    for i in range(0, result_success_len):
        print('URL-->  %s' % url_result_success[i].strip() + ' -->活链接')
