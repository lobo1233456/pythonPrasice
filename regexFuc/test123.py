import json
import re
from bs4 import BeautifulSoup

# str1 =r'"load_errors": [{"name": amed ''\n"}],'
# res = re.findall('"load_errors": \[(.*)\],',str)
# print(res)
# with open(r'C:\Users\liubo\PycharmProjects\test1\regexFuc\qta-report-wrong.js', "r") as f:
#     data_func = f.read()  # 读取js文件
# # print(data_func)
# # it = re.findall(r'"succeed": (true|false), "', data_func)
# it = re.findall(r'"load_errors": (.*?)"passed_tests"', data_func)
# print(it)
# print(bool(re.search('[a-z]', it[0])))#通过js文件中load_error中是否含有字母来判断脚本是否crash

str0 = 'asdf123'
bool(re.search('[a-z]', str0))

def judgeSuc(dir):
    '''
        判断这次构建是否成功，从构建生成的js报告开始查找,成功包含俩点，用例全部通过和用例执行过程中并未异常
    :param dir: dir的路径
    :return:
    '''
    casePassSuc,allsuc,caseCrashSuc= False,False,False
    with open(r'%s\qta-report-wrong.js' % dir, "r") as f:
        data_func = f.read()  # 读取js文件
    caseFail = re.findall(r'"succeed": (true|false), "', data_func)     #判断用了是否全部通过
    if caseFail[0] == 'true':casePassSuc = True
    enp = re.findall(r'"load_errors": (.*?)"passed_tests"', data_func)  #取得load_error中的信息
    # 通过js文件中load_error中是否含有字母来判断脚本是否crash,有则错误，没有则正常
    caseCrash = bool(re.search('[a-z]', enp[0]))
    if caseCrash == False: caseCrashSuc = True
    #俩个判断都为真，则认为脚本正常
    allsuc = casePassSuc and caseCrashSuc
    return allsuc

if __name__ == '__main__':
    # print(judgeSuc(r"C:\Users\liubo\PycharmProjects\test1\regexFuc"))
    str = '''
    <div id="bgImgProgLoad" data-ultra-definition-src="/th?id=OHR.Wachsenburg_ZH-CN5224299503_UHD.jpg&amp;rf=LaDigue_UHD.jpg&amp;pid=hp&amp;w=1920&amp;h=1080&amp;rs=1&amp;c=4" data-explicit-bing-load="false" data-dynamic-size="true"></div>
    '''
    enp = re.findall(r'data-ultra-definition-src="(.*?)"', str)
    print(enp[0])

