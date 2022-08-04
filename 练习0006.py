import os

from collections import Counter

dirs = os.listdir("D:/zhuomian/dc")

def tongji(file):#统计日记中最重要的单词
    file_txt= "D:/zhuomian/dc"+"/"+str(file)
    f = open(file_txt,"r")
    txt = f.read()
    words = txt.split()
    word_counts = Counter(words)
    top_word = word_counts.most_common(1)

    return list(top_word[0])

list_top=[] #建立空列表，后续存储每个日记最重要的单词

for i in range(0,len(dirs)):
    top_words=tongji(dirs[i])
    top_words.pop()
    top_words.append("这是第"+str(i+1)+"篇日记的关键词")
    print(top_words)