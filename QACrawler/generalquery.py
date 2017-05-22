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
        # 只保留名词
        if k.flag.__contains__("n"):
            print k.flag
            print k.word
            keywords.append(k.word)

    answer = ''
    text = ''
    # 找到百科的答案就置1
    flag = 0
    soup_baidu = To.get_html_baidu('https://www.baidu.com/s?wd='+query)

    # 抓取百度前10条的摘要
    for i in range(1,10):
        results = soup_baidu.find(id=i)
        if results == None:
            break

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
                flag = 1
                break
            print '@@@@@@@@@@'
        # print results.get_text("",strip=True)
        text += results.get_text()
    # print text
    # print type(text)

    #bing的摘要
    soup_bing = To.get_html_bing('https://www.bing.com/search?q='+query)
    print soup_bing.prettify()
    # 抓取bing前10条的摘要
    for i in range(6,15):
        results = soup_bing.find(class_="b_xlText b_emphText")
        print "====="
        print results
        print "====="


    if flag == 0:
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

        target_list = {}
        for ks in key_sentences:
            print ks
            words = T.postag(ks)
            for w in words:
                if w.flag == ("nr"):
                    if target_list.has_key(w.word):
                        target_list[w.word] += 1
                    else:
                        target_list[w.word] = 1

        # 多搜索引擎匹配
        maxfq = 0
        for i in target_list:
            if i in keywords:
                continue
            if target_list[i]>maxfq:
                answer = i
                maxfq = target_list[i]
            print i
            print target_list[i]

    return answer




query = "谢婷婷的父亲是？"
ans = generalquery(query)
print "~~~~~~~"
print ans
print "~~~~~~~"
