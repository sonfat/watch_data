#-*- coding:utf-8 -*-
# author : sonfatYU
# date : 2019/03/29

import jieba
from collections import Counter
from datetime import datetime


# stop_words = "F:\GitHub\watch_data\\alg_compare\stop\stop_words.txt"
# dict = "F:\GitHub\watch_data\\alg_compare\dict\dict.txt"


# 生成处理文件名称
def gen_file_name(file_no):
    file_name = "F:\GitHub\watch_data\\alg_compare\load_text\\" + str(file_no) + ".txt"
    return file_name

# 载入停用词表
# 返回停用词的list
# 维护一个list，避免多次读入
def load_stop_words(stop_words):
    stop_words_list = []
    try:
        with open(stop_words, "U") as f:
            for line in f:
                stop_words_list.append(line.strip())
    except Exception,e:
        pass
    return stop_words_list


# 分词操作  处理文件
# 返回分词后的list
def split_words(file_name, stop_words_list, dict1):
    seg_list = []
    token = []
    jieba.load_userdict(dict1)
    try:
        with open(file_name, "r") as f:
            for line in f:
                line = line.strip()
                seg_list += jieba.cut(line, cut_all=False, HMM=True)
        for item in seg_list:
            # if item.encode("utf-8") not in stop_words_list:
            #         token.append(item.encode("utf-8"))
            if len(item) !=1:
                if item.encode("utf-8") not in stop_words_list:
                    token.append(item.encode("utf-8"))
    except Exception,e:
        pass
    return token


# 更新词频字典
def dict_update(dict1, dict3):
    try:
        for k3 in dict3:
            if k3 in dict1:
                dict1[str(k3)] =  dict1[str(k3)] + dict3[k3]
            else:
                dict1[str(k3)] = dict3[k3]
    except Exception,e:
        pass
    return dict1

# 展示测试
def pri(dic):
    for k,v in dic.items():
        print k,v


if __name__ == "__main__":
    result_dict = {}
    stop_words = "F:\GitHub\watch_data\\alg_compare\stop\stop_words.txt"
    dict1 = "F:\GitHub\watch_data\\alg_compare\dict\dict.txt"
    stop_words_list = load_stop_words(stop_words)
    f = open('F:\GitHub\watch_data\\alg_compare\deiling_word\end.txt','w')

    for num in range(1,11):
        print "[*] analaising file:" + str(num) + ".txt......"
        time1 = datetime.now()

        file1 = gen_file_name(num)
        result = split_words(file1, stop_words_list ,dict1)
        # type(result)    list
        # for i in result:
        #     print type(i)   str
        data = dict(Counter(result))
        # data = dict(Counter(result).most_common(50))
        dict_update(result_dict, data)

        # for k,v in result_dict.items():
        #     f.write(k + ' -> ' + str(v) + '\n')

        time2 = datetime.now()
        zone = (time2 - time1).seconds
        print "[+] DONE! Time used: " + str(zone) + 's'
        print "====================================================================="
    be_write = dict(Counter(result_dict).most_common(50))
    for k,v in be_write.items():
        f.write(k + ' -> ' + str(v) + '\n')
    print "[!] Last Result Has Been Written!"
