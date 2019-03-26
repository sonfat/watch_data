# -*- coding:utf-8 -*-
import jieba

jieba.load_userdict("dict.txt")
with open("4.txt","r") as f:
    for line in f:
        line = line.strip()
        seg_list = jieba.cut(line, cut_all=False,  HMM=True)
        print "Full Mode: " + "/ ".join(seg_list)
# seg_list = jieba.cut("4.txt", cut_all=True)
# print "Full Mode: " + "/ ".join(seg_list)