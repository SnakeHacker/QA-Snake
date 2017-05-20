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
    # result = soup.find_all(class_="result-op c-container xpath-log")

    # result = soup.find(id="1")
    for i in range(1,10):
        result = soup.find(id=i)
        [s.extract() for s in soup(['script', 'style','img'])]
        print '============='
        # print result.attrs
        # print result['class']
        # print result.get_text("|", strip=True)
        print result.get_text(strip=True)
        text += result.get_text()
        # print result
        # print result['id']
        # for r in result:
        #     print r
    return text




query = "世界上最长的河流是？"
text = generalquery(query)
qlist = T.wordSegment(query).split(" ")


# r1 = T.wordSegment(text)
r1 = T.postag(text)
# r2 = r1.split(" ")
# print r2

stopworddic = {}
fr = open('../resources/stopwords.txt')
line = fr.readline()
while line:
    stopworddic[line.strip()] = 1
    line = fr.readline()
fr.close()

dic = {}
for r3 in r1:
    if r3.flag == 'x' or stopworddic.has_key(r3.word):
        continue
    else:
        if dic.has_key(r3):
            dic[r3] +=1
        else:
            dic[r3] =1

for d in dic:
    if dic[d] >10 and d.word not in qlist:
        print d.word
        print d.flag
        print dic[d]
        print '========'