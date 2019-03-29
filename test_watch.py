# -*- coding:utf-8 -*-

import requests
import re



re_item = r'</em>                                         <a href="(.*?)" onclick="atarget\(this\)" class="s xst">'


res = requests.get("http://bbs.xbiao.com/rolex/p400.html")
print res.text
req = re.findall(re_item, res.text)
# print req
for i in req:
    print i
    # #
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
