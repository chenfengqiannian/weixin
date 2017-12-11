#coding=utf-8
import jieba
import json
import re
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn.cluster import KMeans
from sklearn import metrics
filetxt=[]
filetxt2=[]

def Chinese_word_extraction(content_raw):
    chinese_pattern=re.compile(u"([\u4e00-\u9fa5]+)")
    re_data = chinese_pattern.findall(content_raw)
    return "".join(re_data)

def clean(content_raw):
    if filetxt:

        pass


    else:

        with open("clean.txt","r") as f:






            filetxt.extend(f.read().split("\r\n"))

            for i in filetxt:
                filetxt2.append(unicode(i,"utf-8"))





    for i in filetxt2:

        content_raw=content_raw.replace(i,"")

    content=Chinese_word_extraction(content_raw)
    return content









with open('items.json', 'r') as f:

    l=[]
    data=json.load(f)
    for i in data:


        #l.extend(jieba.cut(clean(i["content"])))
        l.append(" ".join(jieba.cut(clean(i["content"]))))





    from collections import Counter

    vectorizer = CountVectorizer()  # 该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
    transformer = TfidfTransformer()  # 该类会统计每个词语的tf-idf权值
    tfidf = transformer.fit_transform(vectorizer.fit_transform(l))

    word = vectorizer.get_feature_names()  # 获取词袋模型中的所有词语
    weight = tfidf.toarray()  # 将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重



    kmeans_model = KMeans(n_clusters=5,random_state=2).fit(tfidf)
    labels = kmeans_model.labels_
    print labels
    print metrics.silhouette_score(tfidf, labels, metric='euclidean')
    print'list_number label  '
    for i in range(0,4):
        print "\n簇:"+str(i)
        for j in range(0,len(labels)-1):
            if i==labels[j]:
                print word[j],








    #o=Counter(l)
    #print  dir(o)
    #for i in sorted(o):
     #   print i

    #print len(o)
    #print len(l)
