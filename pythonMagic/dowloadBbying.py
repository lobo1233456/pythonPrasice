import os

import requests
import re
import time
import ctypes
local = time.strftime("%Y.%m.%d")
url = 'http://cn.bing.com/'
con = requests.get(url)
content = con.text
enp = re.findall(r'data-ultra-definition-src="(.*?)"', content)
print(enp[0])
# print(reg)
picUrl = url + enp[0]
read = requests.get(picUrl)
f = open('%s.jpg' % local, 'wb')
f.write(read.content)
f.close()
proj_root = os.path.dirname(os.path.abspath(__file__))
print(proj_root)
picture_path = proj_root+r'/2019.09.16.jpg'
ctypes.windll.user32.SystemParametersInfoW(20, 0, picture_path, 3)