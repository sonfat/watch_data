#-*- coding:utf-8 -*-
from multiprocessing import Process

dict0 = {}
dict1 = {"水鬼":1,  "GMT":1, "日志":1}
dict2 = {"星期-日历":1}
dict3 = {"水鬼":3, "GMT":1,"星期-日历":1, "游艇名士":10}

def spl():
    print"==========================================="

def pri(dic):
    for k,v in dic.items():
        print k,v

def dict_update(dict1, dict3):
    for k3 in dict3:
        if k3 in dict1:
            dict1[str(k3)] =  dict1[str(k3)] + dict3[k3]
        else:
            dict1[str(k3)] = dict3[k3]
    return dict1

dict_update(dict0,dict1)
pri(dict0)
dict_update(dict0,dict3)
pri(dict0)