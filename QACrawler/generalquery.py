#coding:utf8

import Tools as To
import TextProcess as T
import re

'''
查询百度、Bing、（360）
'''


def generalquery(query):
    #分词 去停用词 抽取关键词
    keywords = []
    for k in T.postag(query):
        if k.flag.__contains__("n"):
            print k.flag
            print k.word
            keywords.append(k.word)

    answer = ''
    text = ''
    soup = To.get_html('https://www.baidu.com/s?wd='+query)
    # 抓取前10条的摘要
    for i in range(1,10):
        results = soup.find(id=i)
        if results == None:
            answer = 'Empty'
            break
        # 去除无关的标签
        [s.extract() for s in soup(['script', 'style','img'])]
        print '============='
        # print results.attrs
        # print type(results.attrs)
        # print results['class']
        #判断是否有mu,如果第一个是百度知识图谱的 就直接命中答案
        if results.attrs.has_key('mu') and i == 1:
            print '@@@@@@@@@@'
            # print results.attrs["mu"]
            r = results.find(class_='op_exactqa_s_answer')
            # print r
            if r == None:
                continue
            else:
                # print r.get_text()
                answer = r.get_text()
                continue
            print '@@@@@@@@@@'
        # print results.get_text("",strip=True)
        text += results.get_text()
    # print text
    # print type(text)

    #分句
    cutlist = [u"。",u".", u"_", u"-",u":",u"！",u"？"]
    temp = ''
    sentences = []
    for i in range(0,len(text)):
        if text[i] in cutlist:
            if temp == '':
                continue
            else:
                sentences.append(temp)
            temp = ''
        else:
            temp += text[i]
    key_sentences = {}
    for s in sentences:
        for k in keywords:
            if k in s:
                key_sentences[s]=1

    for ks in key_sentences:
        print ks

    return answer


query = "窦靖童的生父是谁？"
ans = generalquery(query)
print "~~~~~~~"
print ans
print "~~~~~~~"

qlist = T.wordSegment(query).split(" ")

# 找出词频最高的几个单词
# r1 = T.wordSegment(text)
r1 = T.postag(ans)
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