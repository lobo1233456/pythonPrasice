import multiprocessing
import time
import xlrd as xlrd
from selenium import webdriver
url = 'http://60.205.200.186'
driver = webdriver.Chrome()
driver.maximize_window()
try:
    driver.get("https://" + url)
    driver.implicitly_wait(10)
    lem = driver.find_element_by_id("page-topnav").text
    assert "" in lem
except Exception:
    msg = url + " is Wrong "
    self.__edit(msg)
else:
    msg = url + " is Correct "
    self.__edit(msg)
finally:
    driver.close()