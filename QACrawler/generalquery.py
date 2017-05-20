#coding:utf8

import Tools as To
import TextProcess as T
import re

'''
查询百度、Bing、（360）
'''
def generalquery(query):
    text = ''
    soup = To.get_html('https://www.baidu.com/s?wd='+query)
    for i in range(1,10):
        results = soup.find(id=i)
        #判断是否有mu,如果第一个是百度知识图谱的 就直接命中答案
        [s.extract() for s in soup(['script', 'style','img'])]
        print '============='
        # print results.attrs
        # print type(results.attrs)
        # print results['class']
        if results.attrs.has_key('mu') and i == 1:
            print '@@@@@@@@@@'
            print results.attrs["mu"]
            r = results.find(class_='op_exactqa_s_answer')
            print r
            if r == None:
                continue
            else:
                print r.get_text()
                break
            print '@@@@@@@@@@'

        # print results.get_text("||",strip=True)
        text += results.get_text()

    return text


query = "张柏芝的前夫是"
text = generalquery(query)
qlist = T.wordSegment(query).split(" ")

# 找出词频最高的几个单词
# r1 = T.wordSegment(text)
r1 = T.postag(text)
# r2 = r1.split(" ")
# print r2

# stopworddic = {}
# fr = open('../resources/stopwords.txt')
# line = fr.readline()
# while line:
#     stopworddic[line.strip()] = 1
#     line = fr.readline()
# fr.close()
#  dic = {}
# for r3 in r1:
#     if r3.flag == 'x' or stopworddic.has_key(r3.word):
#         continue
#     else:
#         if dic.has_key(r3):
#             dic[r3] +=1
#         else:
#             dic[r3] =1
#
# for d in dic:
#     if dic[d] >10 and d.word not in qlist:
#         print d.word
#         print d.flag
#         print dic[d]
#         print '========'