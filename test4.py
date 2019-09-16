import random

# count = []
# for i in range(100):
#     list = [2]
#     while 1:
#         a = random.randint(0, 1)
#         list.append(a)
#         print(list[-1])
#         if a == 1 and a ==list[-1]:break
#         print(len(list))
#     count.append(len(list))
#
# # avg = sum(count)/len(count)
#
# print(count)
import time

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException


def is_alert_present():
    try:
        driver.switch_to_alert()
    except NoAlertPresentException as e:
        return False
    return True
def close_alert_and_get_its_text(driver):
    try:
        alert = driver.switch_to_alert()
        alert_text = alert.text
        if driver.accept_next_alert:
            alert.accept()
        else:
            alert.dismiss()
        return alert_text
    finally:
        driver.accept_next_alert = True
if __name__ == '__main__':
    i = 1
    for i in range(5):
        try:
            print("----------------%s-------------"%i)
            driver = webdriver.Firefox()
            driver.get("https://www.kmway.com/")
            driver.find_element_by_xpath(u"/html/body/div[5]/div[%s]/div/div[4]/table/tbody/tr[68]/td[5]/a"%i).click()
            driver.find_element_by_id("bottomTel").click()
            driver.find_element_by_id("bottomTel").clear()
            driver.find_element_by_id("bottomTel").send_keys("13764741358")
            driver.find_element_by_xpath("//div[@id='floatbottom']/div[2]/div/div").click()
            time.sleep(2)
            msg = close_alert_and_get_its_text(driver)
            log_info(msg)
            time.sleep(2)
            assert msg =="留言成功"
            break
        except NoSuchElementException as e:
            pass
        finally:
            i = i + 1
            driver.quit()




