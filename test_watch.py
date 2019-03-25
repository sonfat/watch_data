# -*- coding:utf-8 -*-

import requests
import re



re_item = r'''
<!--  -->
([\s\S]*?)
'''


res = requests.get("http://bbs.xbiao.com/871/771652.html")
req = re.findall(re_item, res.text)
print req[1]
#
# with open('test.txt', 'r') as f:
#     for line in f:
#         try:
#             print type(line)
#             res = requests.get(line.strip(' '))
#             result = re.findall(re_item, res.text)
#             print line + ' =============> ' + result[0]
#         except Exception,e:
#             pass
#
#
# indoor_url = gen_indoor(1)
# link_list = collect_links(indoor_url)
