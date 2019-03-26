# -*- coding:utf-8 -*-
import jieba

jieba.load_userdict("dict.txt")
seg_list = []
stop_word = []
token = []

with open("F:\GitHub\watch_data\\alg_compare\stop\stop_words.txt","U") as f:
    for line in f:
        stop_word.append(line.strip())
# print stop_word

with open("4.txt","r") as f:
    for line in f:
        line = line.strip()
        seg_list += jieba.cut(line, cut_all=False,  HMM=True)

for item in seg_list:
    if item not in stop_word:
        token.append(item)

for i in token:
    print i

