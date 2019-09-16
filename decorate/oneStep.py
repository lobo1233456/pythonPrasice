import time

from selenium import webdriver


class Test(object):
    def __init__(self, func):
        print('test init')
        print('func name is %s ' % func.__name__)
        self.__func = func

    def __call__(self, *args, **kwargs):
        print('this is wrapper'+self.er())
        self.__func()
    def __er(self):
        print('this _er')
        return  'this _er'
        # self.__func()

    def er(self):
        print('this _er')
        return 'this _er'
        self.__func()

# class Test(object):
#     def __init__(self, func):
#         print('test init')
#         print('func name is %s ' % func.__name__)
#         self.__func = func
#
#     def __call__(self, *args, **kwargs):
#         print('this is wrapper')
#         self.__func()

#
from selenium.common.exceptions import NoSuchElementException

class Test(object):
    def __init__(self, driver,n):
        self.driver = driver
        self.n = n
        print('test init')
    def __call__(self,driver, *args, **kwargs):
        self.func()
        print('call called')
    def func(self):
        for i in range(self.n):
            try:
                print("----------------%s-------------" % str(i + 1))
                self.function(self.driver)
                break
            except NoSuchElementException as e:
                pass
            finally:
                i = i + 1
                self.driver.quit()


def close_alert_and_get_its_text():
    try:
        alert = driver.switch_to_alert()
        alert_text = alert.text
        if self.accept_next_alert:
            alert.accept()
        else:
            alert.dismiss()
        return alert_text
    finally:
        self.accept_next_alert = True

driver = webdriver.Firefox()
@Test(driver,3)
def function():
    driver.get("https://www.kmway.com/")
    driver.find_element_by_xpath(u"/html/body/div[5]/div[3]/div/div[4]/table/tbody/tr[68]/td[5]/a").click()
    driver.find_element_by_name("tel").click()
    driver.find_element_by_name("tel").clear()
    driver.find_element_by_name("tel").send_keys("13764743157")
    driver.find_element_by_id("area-right-but1").click()
    time.sleep(2)
    msg = close_alert_and_get_its_text()
    assert ("检查成功提交的结果", u"呼叫成功,请等候来电" == msg)

if __name__ == '__main__':
    function()





#输出:
# test init
# func name is test 
# this is wrapper
# this is test func
