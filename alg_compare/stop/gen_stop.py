import datetime

list1 = []
for i in range(1,5):
    path = "stop" + str(i) + ".txt"
    try:
        with open(path, "r") as f1:
            for line in f1:
                list1.append(line)
    except Exception,e:
        pass
set1 = set(list1)
f = open("stop_words.txt", "w")
for i in set1:
    f.write(str(i))