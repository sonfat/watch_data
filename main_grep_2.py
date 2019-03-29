#-*- coding:utf-8 -*-
# author : sonfatYU
# date : 2019/03/25
# re_link = r'</em>                                         <a href="(.*?)" onclick="atarget\(this\)" class="s xst">'


#-*- coding:utf-8 -*-
# author : sonfatYU
# date : 2019/03/25

import os
import requests
import re
from datetime import datetime

re_item = r'''
<!--  -->
([\s\S]*?)
'''


# 生成访问页
def gen_indoor(page_no):
    url_1 = "http://bbs.xbiao.com/rolex/p"
    url_2 = ".html"
    indoor_url = url_1 +  str(page_no) + url_2
    print indoor_url
    return indoor_url

# 收集各个帖子的访问链接
# 维护一个容量为1页的列表
# 一次处理1页
def collect_links(indoor_url):
    re_link = r'</em>                                         <a href="(.*?)" onclick="atarget\(this\)" class="s xst">'
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
                inner_list.append(result[1].replace('<br />','').replace('&nbsp;',''))
            except Exception, e:
                pass
    print '[+] page ' + str(page_no) + ' ->  loded'
    return inner_list

# 将每个页面的主要文本内容写入文件
# 维护一个容量为1页的列表
# 一次处理1页
def inner_in_file(inner_list, page_no):
    file_name = str(page_no) + '.txt'
    with open(file_name, "w") as f:
        f.truncate()
        for item in inner_list:
            f.write(item.encode('utf8') + '\n')
    print '[+] page ' + str(page_no) +  ' -> has been written!'


if __name__ == "__main__":

    for page in range(400,402):
        time1 = datetime.now()
        indoor = gen_indoor(page)
        link_list = collect_links(indoor)
        I_file(link_list)
        list2 = collect_inner_text(page)
        inner_in_file(list2,page)
        time2 = datetime.now()
        zone = (time2 - time1).seconds
        print "Time used: " + str(zone) + 's'
