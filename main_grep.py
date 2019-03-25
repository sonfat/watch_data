#-*- coding:utf-8 -*-
# author : sonfatYU
# date : 2019/03/25

import os
import requests
import re
#
# re_item = r'''
# </div>
# <!--  -->
# ([\s\S]*?)
#
# <ignore_js_op>
# <div class="igcr">
# '''

# re_item = r'''
# <!--  -->
# <div style="float:right;width:210px;" class="adareaView">
# <script>ad_script("7_26");</script>
# </div>
# <!--  -->
# ([\s\S]*?)
#
# '''

re_item = r'''
<!--  -->
([\s\S]*?)
'''


# 生成访问页
def gen_indoor(page_no):
    url_1 = "http://bbs.xbiao.com/rolex/p"
    url_2 = ".html"
    indoor_url = url_1 +  str(page_no) + url_2
    return indoor_url

# 收集各个帖子的访问链接
# 维护一个容量为1页的列表
# 一次处理1页
def collect_links(indoor_url):
    re_link = r'<a href="(.*?)" onclick="atarget\(this\)" class="s xst">'
    res = requests.get(indoor_url)
    result = re.findall(re_link, res.text)
    link_list = []
    for item in result:
        if "</em>" not in item:
            link_list.append(item.split(' ')[0].replace('"', ''))
    return link_list


# 将1个页面的访问链接写入文件
# 维护一个容量为1页的列表
# 一次处理1页
def I_file(link_list):
    with open('cache.txt','w') as f:
        try:
            for link in link_list:
                # link = str(link + '\n')
                f.write(link + '\n')
        except Exception,e:
            pass


# 获取每个页面的主要文本内容
# 维护一个容量为1页的列表
# 一次处理1页
def collect_inner_text(page_no):
    inner_list = []

    with open('cache.txt', 'r') as f:
        for line in f:
            try:
                res = requests.get(line.strip(' '))
                result = re.findall(re_item, res.text)
                # print line + ' =============> ' + result[0].replace('<br />','')
                inner_list.append(result[1].replace('<br />',''))
            except Exception, e:
                pass
    print '[+] page ' + str(page_no) + ' -> has loded'
    return inner_list

# 将每个页面的主要文本内容写入文件
# 维护一个容量为1页的列表
# 一次处理1页
def inner_in_file(inner_list):
    with open("collext.txt", "w") as f:
        f.truncate()
        for item in inner_list:
            f.write(item.encode('utf8') + '\n')
    print '[+] page ' +  ' -> has written!'




# inner_in_file()

indoor = gen_indoor(3)
link_list = collect_links(indoor)
I_file(link_list)
list2 = collect_inner_text(3)
inner_in_file(list2)
# for item in list2:
#     print item

# text_list = collect_inner_text(link_list)
# print len(text_list)




# re_item = r'''
# </div>
# <!--  -->
# ([\s\S]*?)
#
# <ignore_js_op>
# '''