import multiprocessing
import time
import xlrd as xlrd
from selenium import webdriver

class Saaslib:
    def __init__(self):
        self.testfile = "testReporter" + self.timedir()
    def judgeMsg(self,url):
        driver = webdriver.Chrome()
        driver.maximize_window()
        try:
            driver.implicitly_wait(10)
            mobile_emulation = {"deviceName": "Galaxy S5"}
            option = webdriver.ChromeOptions()
            option.add_experimental_option('mobileEmulation', mobile_emulation)
            driver = webdriver.Chrome(chrome_options=option)
            driver.get("https://"+url)
            lem = driver.find_element_by_xpath("/html/body/div[3]/div[1]/a/p").text
            assert "首页" in lem
        except Exception:
            msg = url + " is Wrong "
            self.__edit(msg)
        else:
            msg = url+" is Correct "
            self.__edit(msg)
        finally:
            driver.quit()
    def time(self):
        ts = int(time.time())
        timeFlag = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))
        return timeFlag
    def timedir(self):
        ts = int(time.time())
        timeFlag = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(ts))
        return timeFlag
    def __edit(self,msg):
        print(msg + self.time())
        fh = open(r"C:\Users\liubo\PycharmProjects\test1\reporter\%s"%self.testfile,"a")
        fh.write(msg +  self.time() + " \n")
        fh.close()
    def read(self):
        list =[]
        inpath = r"C:\Users\liubo\PycharmProjects\test1\dataExcel.xlsx"
        data = xlrd.open_workbook(inpath, encoding_override='utf-8')
        table = data.sheets()[0]  # 选定表
        nrows = table.nrows  # 获取行号
        for i in range(0, nrows):  # 第0行为表头
            alldata = table.row_values(i)  # 循环输出excel表中每一行，即所有数据
            result = alldata[0]  # 取出表中第二列数据
            if result is not None:
                list.append(result)
        return list

if __name__ == '__main__':
    case = Saaslib()
    # 多少人去做事(processes=3)
    p = multiprocessing.Pool(processes=3)
    list = case.read()
    for i in list:
        p.apply_async(case.judgeMsg, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All processes done!')

