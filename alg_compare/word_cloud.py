#-*- coding:utf-8 -*-

from collections import Counter
from wordcloud import WordCloud
import os
import jieba

jieba.load_userdict("dict.txt")
f = open("4.txt").read()
words = list(jieba.cut(f, HMM=True))
words = words

data = dict(Counter(words).most_common(50))
for k,v  in data.items():
    print str(k.encode('utf-8')) + ' -> ' + str(v)