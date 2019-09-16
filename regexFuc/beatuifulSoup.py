# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup

soup = BeautifulSoup(open(r"C:\Users\liubo\PycharmProjects\test1\regexFuc\qta-report.html"))
print(soup.prettify())